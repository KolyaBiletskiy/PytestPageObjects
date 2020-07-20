import requests
import pytest
import json
import jsonpath


@pytest.mark.api
class ApiPatchTests:


    def test_put(self):
        api_endpoint = 'https://reqres.in/api/users/2'

        with open('/Users/nick/PycharmProjects/PytestPageObjects/data.json', 'r') as myfile:
            content = myfile.read()  # we read the content as str

        request_json = json.loads(content)  # here we transform to the dict (json)

        response = requests.put(api_endpoint, request_json)

        response_json = json.loads(response.text)
        updated = jsonpath.jsonpath(response_json, "updatedAt")
        print(updated[0])












