# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.2
#

.PHONY: info app-run coverage pylint pytest gh-pages pdf word

info:
	@echo "make options"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    pylint    To run pylint"
	@echo "    pytest    To run pytest with verbose option"
	@echo "    pdf       To create PDF Docs"
{% if cookiecutter.library_documents_location == 'github-pages' %}	@echo "    gh-pages  To create the GitHub pages"{% endif %}

coverage:
	@pytest --cov --cov-report=html -vvv

pylint:
	@pylint {{cookiecutter.__library_name}}/

pytest:
	@pytest --cov -vvv

pdf:
	@sphinx-build -b rinoh ./docs ./docs/_build/pdf

{% if cookiecutter.library_documents_location == 'github-pages' %}
gh-pages:
	@sphinx-build ./docs ./docs/gh-pages
{% endif %}
