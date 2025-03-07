# Makefile for container needs
# Author: Ben Trachtenberg
# Version: 1.0.0
#

.PHONY: build-container

info:
	@echo "make options"
	@echo "    build-container             To build the container"

{% if cookiecutter.container_runtime == "podman" %}
build-container:
	@echo "Building the container with build_branch=$(build_branch)"
{% if cookiecutter.container_git_protocol == "https" %}
	@podman build --build-arg=build_branch=$(build_branch) -t {{ cookiecutter.git_repo_name }}:latest -t {{ cookiecutter.git_repo_name }}:$(build_branch) -f Containerfile
{% else %}
	@podman build --ssh=default --build-arg=build_branch=$(build_branch) -t {{ cookiecutter.git_repo_name }}:latest -t {{ cookiecutter.git_repo_name }}:$(build_branch) -f Containerfile
{% endif %}
{% endif %}

{% if cookiecutter.container_runtime == "docker" %}
build-container:
	@echo "Building the container with build_branch=$(build_branch)"
{% if cookiecutter.container_git_protocol == "https" %}
	@docker build --build-arg=build_branch=$(build_branch) -t {{ cookiecutter.git_repo_name }}:latest -t {{ cookiecutter.git_repo_name }}:$(build_branch) -f Dockerfile
{% else %}
	@docker build --ssh=default --build-arg=build_branch=$(build_branch) -t {{ cookiecutter.git_repo_name }}:latest -t {{ cookiecutter.git_repo_name }}:$(build_branch) -f Dockerfile
{% endif %}
{% endif %}
