# Python Readme.md file generator

A Python script that prompts the user with `InquirerPy` for details about their GitHub project and generates a
professional `README.md` file.

The program uses InquirerPy's [Alternate Syntax](https://inquirerpy.readthedocs.io/en/latest/#alternate-syntax) which is
> more flexible, easier to customise and also provides IDE type hints/completions.

## Features

The script will prompt the user for the following:

* [X] File Name
* [X] File Location
* [X] Project Language
* [X] Project Title
* [X] Description
* [X] Installation Instructions
* [X] Usage Information
* [X] License (choose from a dropdown list)
* [X] Author Name
* [X] Contact Information

The application then generates a `README.md` file using [GitHub-flavored markdown](https://github.github.com/gfm/).

## Installation

- Ensure that a recent version of Python 3 is installed on your system (3.10+).
- If not, then install Python3 based on official
  documentation [Setup and Usage](https://docs.python.org/3.13/using/index.html)
- Prepare virtual environment.
- Activate virtual environment and then install the application directly from the Github repository:
```shell
pip install git+https://github.com/KamilWo/step8up-week6-readme-generator
```
- You can also clone the repository to your local machine:
```shell
git clone https://github.com/KamilWo/step8up-week6-readme-generator
cd step8up-week6-readme-generator
pip3 install -r requirements.txt
```


## Usage

Once installed, a new command `generate-readme` will be available in your terminal.
Simply run it to start the generator.

```shell
generate-readme
```

You can also run the program manually:
```shell
cd step8up-week6-readme-generator
# Activate your environment, e.g.
source venv/bin/activate
# Run the script
python3 src/readme_generator/main.py
```

Follow the on-screen prompts to create your `README.md` file by answering all the questions.

Video showing usage:

[![Watch the video](https://github.com/KamilWo/step8up-week6-readme-generator/blob/main/video/generate-readme.png)](https://youtu.be/kspucmBjIOs)


## For Developers

If you want to contribute to the project, you can set up an editable installation.
This allows you to modify the source code and have the changes immediately reflected
when you run the command.

1. Clone the repository
```shell
git clone https://github.com/KamilWo/step8up-week6-readme-generator
```
2. Activate virtual environment
```shell
cd step8up-week6-readme-generator
# Activate your environment, e.g.
source venv/bin/activate
```
3. Install the package using `pip` or `pip3`. This will automatically handle all dependencies, e.g.
```shell
pip3 install -r requirements.txt
```

If you have any questions, please submit issues:

https://github.com/KamilWo/step8up-week6-readme-generator/issues

## Useful Resources

- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [GitHub-flavored markdown](https://github.github.com/gfm/)
- [GitHub's Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [PyInquirer Documentation](https://github.com/CITGuru/PyInquirer)
- [Creating a `requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
- [Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
