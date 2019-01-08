import subprocess

from giturlparse import parse


def current_repo():
    res = subprocess.run(['git', 'remote', 'get-url', 'origin'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.stderr:
        raise Exception('Invalid repository url.')

    return parse(res.stdout.decode('utf-8'))
