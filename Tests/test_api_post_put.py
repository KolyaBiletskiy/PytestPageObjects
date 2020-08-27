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
    def test_join_synced_session(self):
        url = "http://localhost:8080/api/notifications/fi/session/5b6827ac-e91b-405e-ac45-ff5cff8a57dd/syncedWorkspace"

        headers = {'X-AUTH-TOKEN': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJmZGNlMjg0Ni1hZGU1LTQ2NTItODUyMi1hOTJjYTQ2NDg2YTIiLCJzdWIiOiJndWVzdC1lMDk5ZTRmZS0wYWU4LTQ5MTctYTRlMS1mZDYxMzY3YjYyNzAiLCJpYXQiOjE1OTQyODYzMDQsInJvbGVzIjpbIlJPTEVfR1VFU1QiXSwic2NvcGVzIjpbXSwiZXhwIjoxNjg3NTk4MzA0fQ.6cdslUTRmSnkwfNuP1tbhcAM3rY6qAug6mhm1HVbAaPWHQa06GOuPImREm-nrEvC6QMnO6d-26o9IYw8sbm-rw'
                   }
        file = open('/Users/nick/PycharmProjects/PytestPageObjects/data.json', 'r')
        json_input = file.read()
        request_json = json.loads(json_input)

        response = requests.post(url, json=request_json, headers=headers)
        print(response.status_code)












