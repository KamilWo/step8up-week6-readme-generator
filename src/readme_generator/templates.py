"""
Template functions.
"""


def template_python(user_data: dict[str, str]):
    """
    Returns README template for Python project.

    :param user_data: Data gathered from the user in form of a dict.

    :return: README template.
    """

    return f"""# {user_data["project_title"]}

## Description
{user_data["description"]}

---

## Python installation

- Ensure that a recent version of Python 3 is installed on your system (3.10+).
- If not, then install Python3 based on the official
  documentation [Setup and Usage](https://docs.python.org/3.13/using/index.html)

---

## Installation
{user_data["installation"]}

---

## Usage
{user_data["usage"]}

---

## License
This project is licensed under the `{user_data["license_choice"]}`. 
Please see the `LICENSE` file.

---

## Author
{user_data["author_name"]}

{user_data["contact_info"]}

"""


def template_nodejs(user_data: dict[str, str]):
    """
    Returns README template for NOde.js project.

    :param user_data: Data gathered from the user in form of a dict.

    :return: README template.
    """

    return f"""# {user_data["project_title"]}

## Description
{user_data["description"]}

---

## Node.js installation

- Ensure that a recent version of Node.js is installed on your system (18+).
- If not, then install Node.js based on the official
  documentation [Downloading and Installing](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

---

## Installation
{user_data["installation"]}

---

## Usage
{user_data["usage"]}

---

## License
This project is licensed under the `{user_data["license_choice"]}`. 
Please see the `LICENSE` file.

---

## Author
{user_data["author_name"]}

{user_data["contact_info"]}

"""
