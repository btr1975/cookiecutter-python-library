@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.8
REM

SET option=%1

IF "%option%" == "" (
    GOTO BAD_OPTIONS
)

IF "%option%" == "all" (
    black {{cookiecutter.__library_name}}/
    black tests/
    pylint {{cookiecutter.__library_name}}\
    pytest --cov --cov-report=html -vvv
    bandit -c pyproject.toml -r .
    pip-audit -r requirements.txt
    GOTO END
)

IF "%option%" == "build" (
    python -m build
    GOTO END
)

IF "%option%" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%option%" == "pylint" (
    pylint {{cookiecutter.__library_name}}\
    GOTO END
)

IF "%option%" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%option%" == "format" (
    black {{cookiecutter.__library_name}}/
    black tests/
    GOTO END
)

IF "%option%" == "check-vuln" (
    pip-audit -r requirements.txt
    GOTO END
)

IF "%option%" == "check-security" (
    bandit -c pyproject.toml -r .
    GOTO END
)

{% if cookiecutter.library_documents_location == 'github-pages' %}
IF "%option%" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__library_name}}
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

:OPTIONS
@ECHO make options
@ECHO     all             To run coverage, format, pylint, and check-vuln
@ECHO     build           To build a distribution
@ECHO     coverage        To run coverage and display ASCII and output to htmlcov
@ECHO     check-vuln      To check for vulnerabilities in the dependencies
@ECHO     check-security  To check for vulnerabilities in the code
@ECHO     format          To format the code with black
@ECHO     pylint          To run pylint
@ECHO     pytest          To run pytest with verbose option
{% if cookiecutter.library_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}
GOTO END

:BAD_OPTIONS
@ECHO Argument is missing
@ECHO Usage: make.bat option
@ECHO.
GOTO OPTIONS

:END
