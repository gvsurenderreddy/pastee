import os
from .models import Language


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