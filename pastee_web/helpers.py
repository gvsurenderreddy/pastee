import os

from .models import Language

from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import get_formatter_by_name


def write_file(content, name):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/pastee_web/pastes/'

    with open(path + name, 'w+') as f:
        f.write(content)


def prettyoutput():
    available_languages = Language.objects.all()
    return_value = []

    for language in available_languages:
        return_value.append([language.identifier, language.name])

    return tuple(return_value)


def highlightpaste(path, paste_name):

    with open(path + paste_name) as f:
        paste_content = f.read()

    lexer = guess_lexer(paste_content)
    formatter = get_formatter_by_name('html')

    return highlight(paste_content, lexer, formatter)
