import requests


def buscar_avatar(user):
    """
    Search an avatar of GitHub user

    :param user: str with a GitHub username
    :return: str contains the avatar link
    """

    url = f"https://api.github.com/users/{user}"
    resp = requests.get(url)

    return resp.json()['avatar_url']
