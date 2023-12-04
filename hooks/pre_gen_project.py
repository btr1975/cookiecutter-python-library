"""
pre generation hooks for cookiecutter to validate data
"""
import re
import sys


def validate_no_spaces(arg_name: str, human_readable_name: str) -> None:
    """Validate no spaces in the arg_name

    :type arg_name: str
    :param arg_name: The cookiecutter variable to validate
    :type human_readable_name: str
    :param human_readable_name: The human-readable name of the cookiecutter variable

    :rtype: None
    :return: Nothing it exits if the arg_name is invalid
    """
    arg_regex = r'^\S+$'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid {human_readable_name} no spaces allowed!')
        sys.exit(1)


def validate_no_spaces_begin_or_end(arg_name: str, human_readable_name: str) -> None:
    """Validate no spaces beginning or ending in the arg_name

    :type arg_name: str
    :param arg_name: The cookiecutter variable to validate
    :type human_readable_name: str
    :param human_readable_name: The human-readable name of the cookiecutter variable

    :rtype: None
    :return: Nothing it exits if the arg_name is invalid
    """
    arg_regex = r'^\S.*\S$'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid {human_readable_name} no spaces allowed at the beginning or ending!')
        sys.exit(1)


def validate_semantic_version(arg_name: str, human_readable_name: str) -> None:
    """Validate semantic version in the arg_name

    :type arg_name: str
    :param arg_name: The cookiecutter variable to validate
    :type human_readable_name: str
    :param human_readable_name: The human-readable name of the cookiecutter variable

    :rtype: None
    :return: Nothing it exits if the arg_name is invalid
    """
    arg_regex = r'^\d+\.\d+\.\d+$'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid {human_readable_name} should be semantic X.X.X!')
        sys.exit(1)


def validate_https_url(arg_name: str, human_readable_name: str) -> None:
    """Validate https url in the arg_name

    :type arg_name: str
    :param arg_name: The cookiecutter variable to validate
    :type human_readable_name: str
    :param human_readable_name: The human-readable name of the cookiecutter variable

    :rtype: None
    :return: Nothing it exits if the arg_name is invalid
    """
    arg_regex = r'^https://\S+$'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid {human_readable_name} should start with https://!')
        sys.exit(1)


def validate_numbers_letters_hyphens(arg_name: str, human_readable_name: str) -> None:
    """Validate numbers, letters and hyphens in the arg_name

    :type arg_name: str
    :param arg_name: The cookiecutter variable to validate
    :type human_readable_name: str
    :param human_readable_name: The human-readable name of the cookiecutter variable

    :rtype: None
    :return: Nothing it exits if the arg_name is invalid
    """
    arg_regex = r'^([A-Z]|[a-z]|[0-9]|-{1})+$'
    if not re.match(arg_regex, arg_name):
        print(f'ERROR: "{arg_name}" is not a valid {human_readable_name} should be numbers, letters and hyphens!')
        sys.exit(1)


if __name__ == '__main__':
    validate_no_spaces_begin_or_end(arg_name='{{ cookiecutter.full_name }}',
                                    human_readable_name='full_name')  # pragma: no cover
    validate_no_spaces(arg_name='{{ cookiecutter.email }}', human_readable_name='email')  # pragma: no cover
    validate_no_spaces(arg_name='{{ cookiecutter.git_username }}',
                       human_readable_name='git_username')  # pragma: no cover
    validate_numbers_letters_hyphens(arg_name='{{ cookiecutter.git_repo_name }}',
                                     human_readable_name='git_repo_name')  # pragma: no cover
    validate_https_url(arg_name='{{ cookiecutter.git_url }}',
                       human_readable_name='git_url')  # pragma: no cover
    validate_no_spaces_begin_or_end(arg_name='{{ cookiecutter.library_description }}',
                                    human_readable_name='library_description')  # pragma: no cover

    validate_semantic_version(arg_name='{{ cookiecutter.library_version }}',
                              human_readable_name='library_version')  # pragma: no cover
