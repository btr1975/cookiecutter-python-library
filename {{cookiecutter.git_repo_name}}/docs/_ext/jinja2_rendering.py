"""
Sphinx extension to render Jinja2 in .rst files.

This will render Jinja2 BEFORE .rst files are parsed.
"""
from sphinx.application import Sphinx


def jinja2_rendering(app: Sphinx, docname: str, source: list) -> None:
    """Render Jinja2 in .rst files before the Sphinx magic.
    THIS ONLY WORKS IN HTML RENDERING

    :type app: sphinx.application.Sphinx
    :param app: Sphinx application context
    :type docname: String
    :param docname: Name of the document being rendered
    :type source: List
    :param source: Source of the document being rendered

    :rtype: None
    :return: Nothing
    """
    if app.builder.format != 'html':
        return

    source_file = source[0]
    rendered = app.builder.templates.render_string(source_file, app.config.html_context)
    source[0] = rendered


def setup(app: Sphinx) -> None:
    """Setup the Jinja2 rendering extension.

    :type app: sphinx.application.Sphinx
    :param app: Sphinx application context

    :rtype: None
    :return: Nothing
    """
    app.connect('source-read', jinja2_rendering)
