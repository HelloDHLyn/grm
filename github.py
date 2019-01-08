import os
import requests

_GITHUB_API_ENDPOINT = 'https://api.github.com/graphql'
_GITHUB_ACCESS_TOKEN_ENV_KEY = 'GREPO_ACCESS_TOKEN'


def _github_token() -> str:
    token = os.environ.get(_GITHUB_ACCESS_TOKEN_ENV_KEY)
    if token is None:
        raise Exception('Cannot get access token.')
    return token


def query(query: str) -> dict:
    res = requests.post(
        _GITHUB_API_ENDPOINT,
        json={'query': query},
        headers={'Authorization': "Bearer {}".format(_github_token())},
    )
    if res.status_code != 200:
        raise Exception("GitHub return invalid response: {}".format(res.status_code))

    return res.json()
