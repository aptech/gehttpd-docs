from docutils import nodes
from sphinx import addnodes
from sphinx.writers.html import HTMLTranslator


class desc_returnlist(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for a general parameter list."""
    child_text_separator = ', '


class desc_return(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    """Node for a single return."""


class GAUSSHTMLTranslator(HTMLTranslator):
    """
    Our custom GAUSS HTML translator.
    """

    def __init__(self, *args):
        super().__init__(*args)
        self.multiple_returns = False

    def unknown_visit(self, node):
        super().unknown_visit(node)

    # def visit_desc_name(self, node):
    #     # type: (nodes.Element) -> None
    #     self.body.append(self.starttag(node, 'code', '', CLASS='descname'))
    #
    # def depart_desc_name(self, node):
    #     # type: (nodes.Element) -> None
    #     self.body.append('</code>')

    def visit_desc_returnlist(self, node):
        # type: (nodes.Element) -> None

        self.first_param = 1
        self.optional_param_level = 0

        self.multiple_returns = len(node.children) > 1

        # How many required parameters are left.
        self.required_params_left = sum(
            [isinstance(c, desc_return) # source.docs.util.
             for c in node.children])

        if self.multiple_returns:
            self.body.append('<span class="sig-curly">{</span>&nbsp;')

        self.param_separator = node.child_text_separator

    def depart_desc_returnlist(self, node):
        # type: (nodes.Element) -> None
        if self.multiple_returns:
            self.body.append('&nbsp;<span class="sig-curly">}</span>')

        self.body.append('&nbsp;<span class="sig-equals">=</span>&nbsp;')

    # If required parameters are still to come, then put the comma after
    # the parameter.  Otherwise, put the comma before.  This ensures that
    # signatures like the following render correctly (see issue #1001):
    #
    #     foo([a, ]b, c[, d])
    #
    def visit_desc_return(self, node):
        # type: (nodes.Node) -> None
        if self.first_param:
            self.first_param = 0
        elif not self.required_params_left:
            self.body.append(self.param_separator)
        if self.optional_param_level == 0:
            self.required_params_left -= 1
        if not node.hasattr('noemph'):
            self.body.append('<em>')

    def depart_desc_return(self, node):
        # type: (nodes.Node) -> None
        if not node.hasattr('noemph'):
            self.body.append('</em>')
        if self.required_params_left:
            self.body.append(self.param_separator)

