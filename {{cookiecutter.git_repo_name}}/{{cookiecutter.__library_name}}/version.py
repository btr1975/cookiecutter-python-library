"""
Holds the version information for the package
"""
__title__ = '{{ cookiecutter.git_repo_name }}'
__description__ = '{{ cookiecutter.library_description }}'
__author__ = '{{ cookiecutter.full_name }}'
__copyright__ = 'Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}'
__credits__ = None
__license__ = 'The MIT License (MIT)'
__status__ = 'prod'
{% set version_info = cookiecutter.library_version.split('.') %}
__version_info__ = ({{ version_info[0] }}, {{ version_info[1] }}, {{ version_info[2] }})
__version__ = '.'.join(map(str, __version_info__))
__maintainer__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__url__ = '{{ cookiecutter.git_url }}'
