import json
import requests


class Requester:
    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'sec-fetch-dest': 'none',
            'accept': '*/*',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'accept-language': 'en-US'
        }

    def get(self, url, params=None):
        """
        Perform a http get request.

        :param url: str
        :param params: dict, optional

        :return: dict
            Json format
        """
        response = requests.get(url, headers=self.headers, params=params)
        data = json.loads(response.content)
        return data

    def post(self, url, params=None, body=None):
        """
        Perform a http post request.

        :param url: str
        :param params: dict, optional
        :param body: dict, optional

        :return:
        """

        algolia_headers = {
            'x-algolia-api-key': 'ZmQ1YmUxNWI0ZTRhMTQzNTYyOGQ3ZDliYzZlMjIxM2Q0MTAzZDdhZGM2NGUzOTA5NjI3MGE4MDZlZGQyZmVjNHZhbGlkVW50aWw9MTYxNzY1MDAzMA==',
            'x-algolia-application-id': 'XW7SBCT9V6'
        }
        algolia_headers.update(self.headers)

        response = requests.post(url, headers=algolia_headers, params=params, json=body)
        data = json.loads(response.content)
        return data


requester = Requester()
