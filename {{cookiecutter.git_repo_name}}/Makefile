# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.4
#

.PHONY: info app-run coverage pylint pytest gh-pages pdf

info:
	@echo "make options"
	@echo "    build     To build a distribution"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    pylint    To run pylint"
	@echo "    pytest    To run pytest with verbose option"
{% if cookiecutter.library_documents_location == 'github-pages' %}	@echo "    gh-pages  To create the GitHub pages"{% endif %}

build:
	@python -m build

coverage:
	@pytest --cov --cov-report=html -vvv

pylint:
	@pylint {{cookiecutter.__library_name}}/

pytest:
	@pytest --cov -vvv

{% if cookiecutter.library_documents_location == 'github-pages' %}
gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./{{cookiecutter.__library_name}}
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}
