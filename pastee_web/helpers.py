import os


def write_file(content, name):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/pastee_web/pastes/'

    with open(path + name, 'w+') as f:
        f.write(content)

