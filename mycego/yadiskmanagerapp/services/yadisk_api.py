import requests
from requests_oauthlib import OAuth2Session


class YaDiskAPI:
    API = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token: str) -> None:
        self.token = token

    def get_headers(self) -> dict:
        return {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
    
    def get_public_resources(self, public_key: str) -> tuple[dict, bool]:
        url = self.API + 'public/resources'
        headers = self.get_headers()
        params = {
            'public_key': public_key,
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json(), response.ok
