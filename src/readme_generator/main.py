"""
README.md files generator.

@author: Kamil Wozniak <kamil.m.wozniak+git@gmail.com>
@license: GPLv3, in the LICENSE file

Produces README.md files. Program asks user questions, which then are used for generating
the output.

InquirerPy documentation: https://inquirerpy.readthedocs.io/en/latest/
"""

import logging
import os

from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator, PathValidator
from rich.console import Console

from .constants import LICENSES, TEMPLATE_TYPES
from .templates import template_python

_logger = logging.getLogger(__name__)


class ReadmeGenerator:
    """
    ReadmeGenerator class.
    """

    def __init__(self):
        self.console = Console()

    def ask_questions(self) -> list[str]:
        """
        Interactively gathers information from the user and generates a README.md file.

        :return: None
        """
        self.console.print(
            "[bold green]Let's generate your README.md file![/bold green]\n"
        )

        file_name = inquirer.text(
            message="Provide custom file name:",
            validate=PathValidator(),
            default="README.md",
        ).execute()

        project_type = inquirer.select(
            message="Please select your Project language:",
            choices=TEMPLATE_TYPES,
            default="Python",
        ).execute()

        # 1. Project Title
        project_title = inquirer.text(
            message="Please provide your Project Title:",
            validate=EmptyInputValidator(),
            invalid_message="Project Title cannot be empty.",
        ).execute()

        # 2. Description
        description = inquirer.text(
            message="Please provide a brief Description of your Project:",
            long_instruction="This will be the main overview of your Project.",
            multiline=True,
        ).execute()

        # 3. Installation Instructions
        installation = inquirer.text(
            message="Please provide installation instructions:",
            long_instruction=("e.g., `pip3 install your-package`, "
                              "or `pip3 install -r requirements.txt`, "
                              "or detailed steps."),
            multiline=True,
        ).execute()

        # 4. Usage Information
        usage = inquirer.text(
            message="Please provide Usage Information:",
            long_instruction="How can users use your project? Provide examples.",
            multiline=True,
        ).execute()

        # 5. License (Dropdown)
        licenses = list(LICENSES.values())
        license_choice = inquirer.select(
            message="Please choose a License for your Project:",
            choices=licenses,
            default="MIT License",
        ).execute()

        # 6. Author Name
        author_name = inquirer.text(
            message="Enter your name (Author):",
            validate=EmptyInputValidator(),
            invalid_message="Author's name cannot be empty.",
        ).execute()

        # 7. Contact Information
        contact_info = inquirer.text(
            message="Please enter contact information (e.g., email, GitHub profile, LinkedIn):",
            long_instruction="This helps users get in touch with you.",
            multiline=True,
        ).execute()

        self.console.print("\n[bold cyan]Generating README.md content...[/bold cyan]")

        return [
            file_name,
            project_type,
            project_title,
            description,
            installation,
            usage,
            license_choice,
            author_name,
            contact_info,
        ]

    def generate_readme(self, params: list[str]) -> None:
        """
        Interactively gathers information from the user and generates a README.md file.

        :return: None
        """
        file_path = params.pop(0)

        # README content template
        readme_template = ""

        if params[0] == "Python":
            params.pop(0)
            readme_template = template_python(*params)
        else:
            self.console.print("\n[bold red]Unknown project type![/bold red]")

        # Write the content to README.md
        try:
            with open(os.path.join(file_path), "w", encoding="utf-8") as readme_file:
                readme_file.write(readme_template)
            self.console.print(
                "\n[bold green]README.md generated successfully![/bold green]"
            )
            self.console.print(
                "[yellow]You can now find the 'README.md' file in the current directory.[/yellow]"
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

        params = generator.ask_questions()

        _logger.info("Generating %s: %s", params[0], params[1])

        generator.generate_readme(params)

        if input("Do you want to create another? (y/n) ").lower() != "y":
            break


if __name__ == "__main__":
    main()
