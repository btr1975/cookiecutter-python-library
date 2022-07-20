@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.0
REM

IF "%1" == "coverage" (
    coverage erase
    coverage run
    coverage report
    coverage html
    GOTO END
)

IF "%1" == "pylint" (
    pylint modules\
    GOTO END
)

IF "%1" == "pytest" (
    pytest -vvv
    GOTO END
)

{% if cookiecutter.app_documents_location == 'github-pages' %}
IF "%1" == "gh-pages" (
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

@ECHO make options
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option
{% if cookiecutter.app_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}

:END
