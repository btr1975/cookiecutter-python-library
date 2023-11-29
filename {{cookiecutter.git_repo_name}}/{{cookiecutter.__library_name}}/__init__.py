"""
init for {{ cookiecutter.__library_name }}
"""
{% if cookiecutter.include_cli == 'y' %}from {{ cookiecutter.__library_name }}.{{ cookiecutter.__library_name }}_cli import cli{% endif %}
