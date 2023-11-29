"""
post generation hooks for cookiecutter to remove unneeded files
"""
import os

REMOVE_PATHS = [
    '{% if cookiecutter.include_cli != "y" %}{{cookiecutter.__library_name}}/{{cookiecutter.__library_name}}_cli.py{% endif %}',
    '{% if cookiecutter.include_cli != "y" %}{{cookiecutter.__library_name}}/example.py{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
