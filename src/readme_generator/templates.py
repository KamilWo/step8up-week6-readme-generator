"""
Template functions.
"""

def template_python(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    project_title: str,
    description: str,
    installation: str,
    usage: str,
    license_choice: str,
    author_name: str,
    contact_info: str,
):
    """
    Returns README template for Python project.

    :param project_title: Project Title.
    :param description: Description.
    :param installation: Installation.
    :param usage: Usage.
    :param license_choice: License choice.
    :param author_name: Author name.
    :param contact_info: Contact info.

    :return: README template.
    """

    return f"""# {project_title}

## Description
{description}

---

## Installation
{installation}

---

## Usage
{usage}

---

## License
This project is licensed under the `{license_choice}`. Please see the `LICENSE` file.

---

## Author
{author_name}

{contact_info.replace("\n", "\n\n")}

"""
