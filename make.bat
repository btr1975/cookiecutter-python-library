@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.0
REM

IF "%1" == "all" (
    black hooks\
    black tests\
    pylint hooks\
    pytest --cov --cov-report=html -vvv
    bandit -c pyproject.toml -r .
    GOTO END
)

IF "%1" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    pylint hooks\
    GOTO END
)

IF "%1" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%1" == "black" (
    black hooks\
    black tests\
    GOTO END
)

IF "%1" == "secure" (
    bandit -c pyproject.toml -r .
    GOTO END
)

@ECHO make options
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     black     To format the code with black
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option

:END
