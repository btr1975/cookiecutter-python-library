# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.0
#

.PHONY: info app-run coverage pylint pytest gh-pages

info:
	@echo "make options"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    pylint    To run pylint"
	@echo "    pytest    To run pytest with verbose option"
{% if cookiecutter.app_documents_location == 'github-pages' %}	@echo "    gh-pages  To create the GitHub pages"{% endif %}

coverage:
	@coverage erase
	@coverage run
	@coverage report
	@coverage html

pylint:
	@pylint modules/

pytest:
	@pytest -vvv

{% if cookiecutter.app_documents_location == 'github-pages' %}
gh-pages:
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}
