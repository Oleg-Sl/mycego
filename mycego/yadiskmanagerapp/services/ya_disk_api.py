from requests_oauthlib import OAuth2Session

# https://oauth.yandex.ru/client/7a477dfee8fe4bf79e5349aff963389e
# https://education.yandex.ru/handbook/python/article/modul-requests
client_id = '7a477dfee8fe4bf79e5349aff963389e'
client_secret = '94cf003c71c845788e2bb06c1f79c245'
token = 'y0_AgAEA7qj8UkqAAyDBgAAAAESTEIXAABHfKNWH8RAP4OHIhc8yD6FsaRRYA'


class YaDiskAPI:
    def __init__(self, token):
        self.token = token


if __name__ == '__main__':
    # ya_api = YaDiskAPI(token)
    auth_url = "https://oauth.yandex.ru/authorize"
    token_url = "https://oauth.yandex.ru/token"
    oauth = OAuth2Session(client_id=client_id)
    # authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
    # print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
    code = input("Вставьте одноразовый код: ")
    token = oauth.fetch_token(token_url=token_url,
                            code=code,
                            client_secret=client_secret)
    access_token = token["access_token"]
    print(access_token)
