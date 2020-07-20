import requests
import pytest
import json
import jsonpath
from requests.auth import HTTPBasicAuth as bas_auth

@pytest.mark.api
class ApiAuthTests:

    global api_endpoint
    api_endpoint = 'https://api.github.com/user'


    def test_basic(self):
        response = requests.get(api_endpoint, auth=bas_auth('biletskiy.mykola@gmail.com', 'somepass'))
        print(response.text)

    def test_oauth(self):
        token_url = 'http://thetestingworldapi.com/Token'
        data = {'grant_type': 'password', 'username': 'admin', 'password': 'adminpass'}
        response = requests.post(token_url, data)
        print(response.text)
        token_value = json.loads(response.text)
        access_token = jsonpath.jsonpath(token_value, 'access_token')
        access_token = access_token[0]

        auth = {'Authorization': 'Bearer ' + access_token}


        api_endpoint = 'http://thetestingworldapi.com/api/StDetails/1104'

        response = requests.get(api_endpoint, headers=auth)
        print(response.text)








