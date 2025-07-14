"""
Markdown readme files generator.

@author: Kamil Wozniak <kamil.m.wozniak+git@gmail.com>
@license: GPLv3, in the LICENSE file

Produces Markdown readme files. Program asks user preconfigured questions,
which then are used for generating the output.

InquirerPy documentation: https://inquirerpy.readthedocs.io/en/latest/
"""

import logging
import os

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from rich.console import Console

from .constants import LICENSES, PROJECT_LANGUAGES
from .templates import template_nodejs, template_python

_logger = logging.getLogger(__name__)


class ReadmeGenerator:
    """
    ReadmeGenerator class, generates a Markdown readme file
    by interactively asking the user questions.
    """

    def __init__(self):
        self.console = Console()

    def ask_questions(self) -> dict[str, str]:
        """
        Interactively gathers information from the user and generates
        a Markdown readme file at a given location.

        :return: A dictionary containing all the user-provided answers.
        """
        self.console.print(
            "[bold green]Let's generate your README.md file![/bold green]\n"
        )

        # 1. File name
        file_name = inquirer.text(
            message="Please provide a custom name for the README file:",
            validate=EmptyInputValidator(),
            default="README.md",
        ).execute()

        # It will be faster to give options than custom paths
        # 2. File location
        file_location = inquirer.filepath(
            message="Please select the location where the file should be saved:",
            # choices=FILE_LOCATIONS,
            validate=PathValidator(is_dir=True, message="Path doesn't exist"),
            default=os.getcwd(),
        ).execute()

        # File path
        file_path = str(os.path.join(file_location, file_name))

        # 3. Project language
        project_language = inquirer.select(
            message="Please select your Project language:",
            choices=list(PROJECT_LANGUAGES),
            default="Python",
        ).execute()

        # 4. Project Title
        project_title = inquirer.text(
            message="Please provide your Project Title:",
            validate=EmptyInputValidator(),
            invalid_message="Project Title cannot be empty.",
        ).execute()

        # 5. Description
        description = inquirer.text(
            message="Please provide a brief Description of your Project:",
            long_instruction="This will be the main overview of your Project.",
            multiline=True,
        ).execute()

        # 6. Installation Instructions
        installation = inquirer.text(
            message="Please provide installation instructions:",
            long_instruction=(
                "e.g., `pip3 install your-package`, "
                "or `pip3 install -r requirements.txt`, "
                "or detailed steps."
            ),
            multiline=True,
        ).execute()

        # 7. Usage Information
        usage = inquirer.text(
            message="Please provide Usage Information:",
            long_instruction="How can users use your project? Provide examples.",
            multiline=True,
        ).execute()

        # 8. License (Dropdown)
        license_choice = inquirer.select(
            message="Please choose a License for your Project:",
            choices=list(LICENSES.values()),
            default="MIT License",
        ).execute()

        # 9. Author Name
        author_name = inquirer.text(
            message="Enter your name (Author):",
            validate=EmptyInputValidator(),
            invalid_message="Author's name cannot be empty.",
        ).execute()

        # 10. Contact Information
        contact_info = inquirer.text(
            message="Please enter contact information (e.g., email, GitHub profile, LinkedIn):",
            long_instruction="This helps users get in touch with you.",
            multiline=True,
        ).execute()
        # Add more spacing between the lines to properly show in readme
        contact_info = contact_info.replace("\n", "\n\n")

        self.console.print("\n[bold cyan]Gathered all information.[/bold cyan]")

        return {
            "file_name": file_name,
            "file_location": file_location,
            "file_path": file_path,
            "project_language": project_language,
            "project_title": project_title,
            "description": description,
            "installation": installation,
            "usage": usage,
            "license_choice": license_choice,
            "author_name": author_name,
            "contact_info": contact_info,
        }

    def generate_readme(self, user_data: dict[str, str]) -> None:
        """
        Generated the Markdown readme file from the provided data.

        :user_data: A dictionary containing the user's answers.
        :return: None
        """

        # README content template
        readme_template = ""

        match user_data["project_language"]:
            case "Python":
                readme_template = template_python(user_data)
            case "Node.js":
                readme_template = template_nodejs(user_data)
            case _:
                self.console.print("\n[bold red]Unknown project type![/bold red]")

        # Write the content to README.md
        file_path = user_data["file_path"]
        try:
            with open(file_path, "w", encoding="utf-8") as readme_file:
                readme_file.write(readme_template)
            self.console.print(
                f"\n[bold green]'{user_data["file_name"]}' generated successfully![/bold green]"
            )
            self.console.print(
                f"[yellow]You can now find the '{user_data["file_name"]}' file "
                f"in the specified location: '{user_data["file_location"]}'.[/yellow]"
            )
        except IOError as e:
            e_msg = f"[bold red]Error writing {file_path}: {e}[/bold red]"
            _logger.error(e_msg)
            self.console.print(e_msg)


def main() -> None:
    """
    Main program function.

    :return: None
    """
    while True:
        _logger.info("Starting README.md generator...")
        generator = ReadmeGenerator()

        user_data = generator.ask_questions()

        _logger.info(
            "Generating %s: %s", user_data["project_language"], user_data["file_name"]
        )

        generator.generate_readme(user_data)

        if input("Do you want to create another? (y/n) ").lower() != "y":
            break


if __name__ == "__main__":
    main()
