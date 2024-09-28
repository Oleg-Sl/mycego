from requests_oauthlib import OAuth2Session


AUTH_URL = "https://oauth.yandex.ru/authorize"
TOKEN_URL = "https://oauth.yandex.ru/token"


def get_authorization_url(client_id: str) -> str:
    oauth = OAuth2Session(client_id=client_id)
    authorization_url, state = oauth.authorization_url(AUTH_URL, force_confirm="true")
    return authorization_url


def get_token(client_id: str, client_secret: str, code: int) -> dict:
    oauth = OAuth2Session(client_id=client_id)
    token = oauth.fetch_token(
        token_url=TOKEN_URL,
        code=code,
        client_secret=client_secret
    )
    return token
