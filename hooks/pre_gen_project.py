"""
pre generation hooks for cookiecutter to validate data
"""
import re
import sys


def validate_git_repo_name():
    arg_regex = r'^([A-Z]|[a-z]|[0-9]|-{1})+$'
    arg_name = '{{ cookiecutter.git_repo_name }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid git_repo_name!')
        sys.exit(1)


def validate_full_name():
    arg_regex = r'^\S.*\S$'
    arg_name = '{{ cookiecutter.full_name }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid full_name only single spaces are allowed!')
        sys.exit(1)


def validate_email():
    arg_regex = r'^\S+$'
    arg_name = '{{ cookiecutter.email }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid email no spaces allowed!')
        sys.exit(1)


def validate_git_username():
    arg_regex = r'^\S+$'
    arg_name = '{{ cookiecutter.git_username }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid git_username no spaces allowed!')
        sys.exit(1)


def validate_git_url():
    arg_regex = r'^https://\S+$'
    arg_name = '{{ cookiecutter.git_url }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid git_url no spaces allowed!')
        sys.exit(1)


def validate_library_description():
    arg_regex = r'^\S.*\S$'
    arg_name = '{{ cookiecutter.library_description }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid library_description only single spaces are allowed!')
        sys.exit(1)


def validate_library_version():
    arg_regex = r'^\d+\.\d+\.\d+$'
    arg_name = '{{ cookiecutter.library_version }}'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid library_version should be semantic X.X.X!')
        sys.exit(1)


if __name__ == '__main__':
    validate_full_name()
    validate_email()
    validate_git_username()
    validate_git_repo_name()
    validate_git_url()
    validate_library_description()
    validate_library_version()
