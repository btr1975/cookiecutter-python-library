@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.4
REM

IF "%1" == "build" (
    python -m build
    GOTO END
)

IF "%1" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    pylint {{cookiecutter.__library_name}}\
    GOTO END
)

IF "%1" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

{% if cookiecutter.library_documents_location == 'github-pages' %}
IF "%1" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__library_name}}
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

@ECHO make options
@ECHO     build     To build a distribution
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option
{% if cookiecutter.library_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}

:END
