"""
Holds the version information for the package
"""
__copyright__ = 'Copyright (c) {% now 'local', '%Y' %} {{ cookiecutter.full_name }}'
__status__ = 'prod'
{% set version_info = cookiecutter.library_version.split('.') %}
__version_info__ = ({{ version_info[0] }}, {{ version_info[1] }}, {{ version_info[2] }})
__version__ = '.'.join(map(str, __version_info__))
