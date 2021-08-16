"""
@title
@description

https://develop.battle.net/access/clients/8f05c6d37b8a487bba64e650b7248057

"""
import argparse

import requests

CLIENT_ID = '8f05c6d37b8a487bba64e650b7248057'
CLIENT_SECRET = '22ChQKmIEtwbx94JjcXsVDf1b9oAH4zW'


class WowClient:
    """
    Client to authenticate and handle API requests to the WoW developer portal.

    Attributes:
        client_id: String client id supplied by Blizzard.
        client_secret: String client secret supplied by Blizzard.

        api_url_fmt: String url format used to call the API endpoints.
        oauth_url: String url used to call the OAuth API endpoints.

        access_token: String access token that is used to access Blizzard's API.
        session: Open requests.Session instance.
    """

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.api_url_fmt = 'https://{0}.api.blizzard.com{1}'
        self.oauth_url = 'https://us.battle.net/oauth/token'

        self.access_token = None
        self.ttl = None
        self.session = requests.Session()
        return

    def authenticate(self):
        query_params = {'grant_type': 'client_credentials'}
        response = self.session.post(self.oauth_url, params=query_params, auth=(self.client_id, self.client_secret))
        json_response = response.json()
        self.access_token = json_response['access_token']
        self.ttl = json_response['expires_in']
        return json_response

    def ping_api(self):
        return


def main(main_args):
    test_client = WowClient(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    auth_resp = test_client.authenticate()
    print(auth_resp)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')

    args = parser.parse_args()
    main(vars(args))
