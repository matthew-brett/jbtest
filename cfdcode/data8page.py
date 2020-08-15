""" data8page role
"""

from docutils.parsers.rst.roles import set_classes
from docutils import nodes, utils

from sphinx.util.nodes import split_explicit_title, set_role_source_info
from sphinx.errors import ExtensionError


def data8pagerole(name, rawtext, text, lineno, inliner, options={},
                  content=[]):
    """  Place reference to data 8 page.

    Parameters
    ----------
    name : str
        The role name used in the document.
    rawtext : str
        The entire markup snippet, including the role markup.
    text : str
        The text marked with the role.
    lineno : int
        The line number where `rawtext` appears in the input.
    inliner : object
        The inliner instance that called us.
    options : dict, optional
        Directive options for customization.
    content : content, optional
        The directive content for customization.

    Returns
    -------
    nodes : list
        list of nodes to insert into the document. Can be empty.
    messages : list
        list of system messages. Can be empty.
    """
    text = utils.unescape(text)
    node = nodes.paragraph(text, text, **options)
    return [node], []


def setup(app):
    # Add runrole roles
    app.add_role('data8page', data8pagerole)
