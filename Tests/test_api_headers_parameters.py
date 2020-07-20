import requests
import pytest
import json
import jsonpath


@pytest.mark.api
class ApiHeadersTests:

    global api_endpoint
    api_endpoint = 'https://httpbin.org/get'


    def test_header(self):


        header_data = {'first': 'first_value', 'second': 'second_value'}
        response = requests.get(api_endpoint, headers = header_data)
        print(response.text)

    def test_parameters(self):
        param = {'name': 'nick', 'age': '24'}

        response = requests.get(api_endpoint, params=param)
        print(response.text)


