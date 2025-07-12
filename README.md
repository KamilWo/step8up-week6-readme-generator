# Python Readme.md file generator

A Python script that prompts the user using `InquirerPy` for details about their GitHub project.

The questions include:

* [ ] Project Title
* [ ] Description
* [ ] Installation Instructions
* [ ] Usage Information
* [ ] License (choose from a dropdown list)
* [ ] Author Name
* [ ] Contact Information

The application then generates a `README.md` file using [GitHub-flavored markdown](https://github.github.com/gfm/).

## Setup

- Install Python3 based on official documentation [Setup and Usage](https://docs.python.org/3.13/using/index.html)
- Prepare virtual environment
- Install requirements:
    - `pip install -r src/requirements.txt`

## Usage

Run the program

    python3 src/main.py

Follow instructions and answer all the questions.

## Useful Resources

- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [GitHub-flavored markdown](https://github.github.com/gfm/)
- [GitHub's Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [PyInquirer Documentation](https://github.com/CITGuru/PyInquirer)
- [Creating a `requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
