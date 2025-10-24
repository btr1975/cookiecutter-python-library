@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.1
REM

IF "%1" == "all" (
    uv run black hooks\
    uv run black tests\
    uv run pylint hooks\
    uv run pytest --cov --cov-report=html -vvv
    uv run bandit -c pyproject.toml -r .
    uv run pip-audit -r requirements.txt
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
	uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%1" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    uv run pylint hooks\
    GOTO END
)

IF "%1" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%1" == "black" (
    uv run black hooks\
    uv run black tests\
    GOTO END
)

IF "%1" == "secure" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%1" == "vulnerabilities" (
    uv run pip-audit -r requirements.txt
    GOTO END
)

IF "%1" == "pip-export" (
	uv export --no-dev --no-emit-project --no-editable > requirements.txt
	uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

@ECHO make options
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     black     To format the code with black
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option

:END
