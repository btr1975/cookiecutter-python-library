# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 2.0.0
#

.PHONY: all info build build-container coverage format pylint pytest start-container stop-container remove-container \
        gh-pages check-vuln pip-export

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    check-security      To check for vulnerabilities in the code"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"
{% if cookiecutter.library_documents_location == 'github-pages' %}	@echo "    gh-pages           To create the GitHub pages"{% endif %}

{% if cookiecutter.package_manager == 'pip' %}

all: format pylint coverage check-security check-vuln

build:
	@python -m build

coverage:
	@pytest --cov --cov-report=html -vvv

format:
	@black {{cookiecutter.__library_name}}/
	@black tests/

pylint:
	@pylint {{cookiecutter.__library_name}}/

pytest:
	@pytest --cov -vvv

check-vuln:
	@pip-audit -r requirements.txt

check-security:
	@bandit -c pyproject.toml -r .

{% if cookiecutter.library_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__library_name}}
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}

{% elif cookiecutter.package_manager == 'uv' %}

all: format pylint coverage check-security check-vuln pip-export

build:
	@uv build --wheel --sdist

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black {{cookiecutter.__library_name}}/
	@uv run black tests/

pylint:
	@uv run pylint {{cookiecutter.__library_name}}/

pytest:
	@uv run pytest --cov -vvv

check-vuln:
	@uv run pip-audit -r requirements.txt

check-security:
	@uv run bandit -c pyproject.toml -r .

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

{% if cookiecutter.library_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@uv run sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__library_name}}
	@uv run sphinx-build ./docs ./docs/gh-pages
{% endif %}

{% endif %}

{% if cookiecutter.container_runtime == "podman" %}
build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t {{ cookiecutter.git_repo_name }}:latest -f Containerfile

start-container:
	@podman run -itd --name {{ cookiecutter.git_repo_name }} -p 8080:8080 localhost/{{ cookiecutter.git_repo_name }}:latest

stop-container:
	@podman stop {{ cookiecutter.git_repo_name }}

remove-container:
	@podman rm {{ cookiecutter.git_repo_name }}
{% endif %}

{% if cookiecutter.container_runtime == "docker" %}
build-container:
	@cd containers && docker build --ssh=default --build-arg=build_branch=main -t {{ cookiecutter.git_repo_name }}:latest -f Dockerfile

start-container:
	@docker run -itd --name {{ cookiecutter.git_repo_name }} -p 8080:8080 localhost/{{ cookiecutter.git_repo_name }}:latest

stop-container:
	@docker stop {{ cookiecutter.git_repo_name }}

remove-container:
	@docker rm {{ cookiecutter.git_repo_name }}
{% endif %}
