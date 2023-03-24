@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.3
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

IF "%1" == "pdf" (
    sphinx-build -b rinoh ./docs ./docs/_build/pdf
    GOTO END
)

{% if cookiecutter.library_documents_location == 'github-pages' %}
IF "%1" == "gh-pages" (
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)
{% endif %}

@ECHO make options
@ECHO     build     To build a distribution
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option
@ECHO     pdf       To create PDF Docs
{% if cookiecutter.library_documents_location == 'github-pages' %}@ECHO     gh-pages  To create the GitHub pages{% endif %}

:END
