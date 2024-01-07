"""
post generation hooks for cookiecutter to remove unneeded files
"""
from typing import List
import os
import shutil

REMOVE_PATHS_NOT_CLI = [
    '{% if cookiecutter.include_cli != "y" %}{{cookiecutter.__library_name}}/'
    '{{cookiecutter.__library_name}}_cli.py{% endif %}',
    '{% if cookiecutter.include_cli != "y" %}{{cookiecutter.__library_name}}/example.py{% endif %}',
]

REMOVE_PATHS_PODMAN = [
    '{% if cookiecutter.container_runtime == "podman" %}containers/Dockerfile{% endif %}',
]

REMOVE_PATHS_DOCKER = [
    '{% if cookiecutter.container_runtime == "docker" %}containers/Containerfile{% endif %}',
]

def remove_paths(paths_to_remove: List[str]) -> None:
    """Remove files and directories

    :rtype: None
    :returns: Nothing it removes files and directories
    """
    for remove_path in paths_to_remove:
        path = remove_path.strip()
        if path and os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)

            elif os.path.isdir(path):
                shutil.rmtree(path)


if __name__ == '__main__':
    remove_paths(REMOVE_PATHS_NOT_CLI)
    remove_paths(REMOVE_PATHS_PODMAN)
    remove_paths(REMOVE_PATHS_DOCKER)
