@ECHO OFF
REM Makefile for container needs
REM Author: Ben Trachtenberg
REM Version: 1.0.0
REM

SET option=%1
SET build_branch=%2

IF "%option%" == "" (
    GOTO BAD_OPTIONS
)

IF "%build_branch%" == "" (
    GOTO BAD_OPTIONS
)

{% if cookiecutter.container_runtime == "podman" %}
IF "%option%" == "build-container" (
    @ECHO "Building the container with build_branch=%build_branch%"
    podman build --ssh=default --build-arg=build_branch=%build_branch% -t {{ cookiecutter.git_repo_name }}:latest -t {{ cookiecutter.git_repo_name }}:%build_branch% -f Containerfile
    GOTO END
)
{% endif %}

{% if cookiecutter.container_runtime == "docker" %}
IF "%option%" == "build-container" (
    @ECHO "Building the container with build_branch=%build_branch%"
    docker build --ssh=default --build-arg=build_branch=%build_branch% -t {{ cookiecutter.git_repo_name }}:latest -t {{ cookiecutter.git_repo_name }}:%build_branch% -f Containerfile
    GOTO END
)
{% endif %}


@ECHO make options
@ECHO     build-container             To build the container
GOTO END

:BAD_OPTIONS
@ECHO Argument is missing
@ECHO Usage: moo.bat option build_branch
@ECHO.
GOTO END

:END
