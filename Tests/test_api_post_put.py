import requests
import pytest
import json
import jsonpath


@pytest.mark.api
class ApiPostPutTests:


    def test_post(self):
        api_endpoint = 'https://reqres.in/api/users'

        file = open('/Users/nick/PycharmProjects/PytestPageObjects/data.json', 'r')
        json_input = file.read()
        # print(json_input)
        request_json = json.loads(json_input)
        # response = requests.post(api_endpoint, )
        # print(response.status_code)
        # assert response.status_code == 204
        response = requests.post(api_endpoint, request_json)
        # print(response.content)


        response_json = json.loads(response.text)
        id = jsonpath.jsonpath(response_json, 'id')
        # print(id[0])

    def test_put(self):
        api_endpoint = 'https://reqres.in/api/users/2'

        with open('/Users/nick/PycharmProjects/PytestPageObjects/data.json', 'r') as myfile:
            content = myfile.read()  # we read the content as str
        print(type(content))

        request_json = json.loads(content)
        print(type(request_json))

        response = requests.put(api_endpoint, request_json)
        print(type(response.text))

        response_json = json.loads(response.text)
        updated = jsonpath.jsonpath(response_json, "updatedAt")
        print(updated[0])

    @pytest.mark.swagger
    def test_swagger(self):
        url = "http://localhost:8080/api/syncedWorkspace/9a5625c4-48a7-4be2-bbd3-1552ef07d503"

        response = requests.get(url)
        assert response.status_code == 403

        headers = {'X-AUTH-TOKEN': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI4NjI1Y2IxMy1hMmEwLTRiNjAtYmYwOS1lMjllZmVlMzYyMDAiLCJzdWIiOiJmaSIsImlhdCI6MTU5NTI1NjE1Niwicm9sZXMiOlsiUk9MRV9GSSJdLCJzY29wZXMiOltdLCJleHAiOjE2ODg1NjgxNTZ9.sTl4XZWLISdc6bbLrrM9qNeJHqNw1cvcznkv64p-HCJauxsS7B8lbA-W3r7-nJSRGllbaBaXgw7mpzTYAFU3Nw'}


        response = requests.get(url, headers=headers)

        assert response.status_code == 200











