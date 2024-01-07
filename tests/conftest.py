import os
import sys
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def bake_project_cli_podman_data() -> dict:
    options = {
        'git_repo_name': 'python-with-cli',
        'include_cli': 'y',
        'email': 'name@example.com',
        'git_username': 'some-username',
        'git_url': 'https://github.com/some-username/python-with-cli',
    }

    return options


@pytest.fixture
def bake_project_cli_docker_data() -> dict:
    options = {
        'git_repo_name': 'python-with-cli',
        'include_cli': 'y',
        'email': 'name@example.com',
        'git_username': 'some-username',
        'git_url': 'https://github.com/some-username/python-with-cli',
        'container_runtime': 'docker',
    }

    return options


@pytest.fixture
def bake_project_no_cli_podman_data() -> dict:
    options = {
        'git_repo_name': 'python-no-cli',
        'include_cli': 'n',
        'email': 'name@example.com',
        'git_username': 'some-username',
        'git_url': 'https://github.com/some-username/python-no-cli',
    }

    return options


@pytest.fixture
def bake_project_no_cli_docker_data() -> dict:
    options = {
        'git_repo_name': 'python-no-cli',
        'include_cli': 'n',
        'email': 'name@example.com',
        'git_username': 'some-username',
        'git_url': 'https://github.com/some-username/python-no-cli',
        'container_runtime': 'docker',
    }

    return options
