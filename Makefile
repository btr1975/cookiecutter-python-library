# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.0
#

.PHONY: all info coverage pytest black

info:
	@echo "make options"
	@echo "    black     To format code with black"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    pytest    To run pytest with verbose option"

all: coverage black pylint

coverage:
	@pytest --cov --cov-report=html -vvv

pytest:
	@pytest --cov -vvv

pylint:
	@pylint hooks/

black:
	@black hooks/
	@black tests/
