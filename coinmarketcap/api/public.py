import requests


class Public:
    __DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/v1/'
    __DEFAULT_TIMEOUT = 120

    def __init__(self, base_url=__DEFAULT_BASE_URL, request_timeout=__DEFAULT_TIMEOUT):
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.session = requests.session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })

    def __request(self, endpoint, params):
        return self.session.get(
            url=self.base_url + endpoint,
            params=params,
            timeout=self.request_timeout
        ).json()

    def get_tickers(self, coin="", **kwargs):
        params = {}
        params.update(kwargs)

        if coin:
            coin += '/'

        return self.__request(
            endpoint='ticker/' + coin,
            params=params
        )
