import re

from docutils import nodes, utils
from six import iteritems

_amp_re = re.compile(r'(?<!&)&(?![&\s])')


def menusel_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    # type: (unicode, unicode, unicode, int, Inliner, Dict, List[unicode]) ->
    # Tuple[List[nodes.Node], List[nodes.Node]]  # NOQA
    env = inliner.document.settings.env
    if not typ:
        assert env.temp_data['default_role']
        typ = env.temp_data['default_role'].lower()
    else:
        typ = typ.lower()

    text = utils.unescape(text)
    if typ == 'menuselection':
        # text = text.replace('-->', u'\N{TRIANGULAR BULLET}')
        text = text.replace('-->', u'>')
    spans = _amp_re.split(text)

    node = nodes.inline(rawtext=rawtext)
    for i, span in enumerate(spans):
        span = span.replace('&&', '&')
        if i == 0:
            if len(span) > 0:
                textnode = nodes.Text(span)
                node += textnode
            continue
        accel_node = nodes.inline()
        letter_node = nodes.Text(span[0])
        accel_node += letter_node
        accel_node['classes'].append('accelerator')
        node += accel_node
        textnode = nodes.Text(span[1:])
        node += textnode

    node['classes'].append(typ)
    return [node], []


specific_docroles = {
    'menuselection': menusel_role,
}


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    from docutils.parsers.rst import roles

    for rolename, func in iteritems(specific_docroles):
        roles.register_local_role(rolename, func)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
