import requests
import pytest
import json
import jsonpath


@pytest.mark.api
class ApiPatchTests:

    def test_put(self):
        api_endpoint = 'https://reqres.in/api/users/2'

        resp = requests.get(api_endpoint)
        res = json.loads(resp.text)
        json_res = jsonpath.jsonpath(res, "data.first_name")
        print(json_res[0])

        # with open('/Users/nick/PycharmProjects/PytestPageObjects/data.json', 'r') as myfile:
        #     content = myfile.read()  # we read the content as str

        # request_json = json.loads(content)  # here we transform to the dict (json)

        response = requests.patch(api_endpoint, data={'first_name': 'Nick'})

        print(response.text)

        # response_json = json.loads(response.text)
        # updated = jsonpath.jsonpath(response_json, "data")
        # print(updated)
