import requests
import pytest
import json
import jsonpath


@pytest.mark.api
class ApiTests:

    global response
    api_endpoint = 'https://reqres.in/api/users?page=2'
    response = requests.get(api_endpoint)

    def test_get(self):
        print(response.content)
        print(type(response.content))
        assert response.status_code == 200
        # fetch headers
        print(response.headers)
        assert response.headers.get('Server') == 'cloudflare'
        # fetch cookies
        print(response.cookies)
        # fetch encoding
        print(response.encoding)
        # fetch elapse time - time from sending request and getting response
        print(response.elapsed)


    def test_json_path(self):
        json_response = json.loads(response.text)
        # print(json_response)
        # fetch value using json path
        pages = jsonpath.jsonpath(json_response, 'total_pages')  # will return LIST
        assert pages[0] == 2
        # advanced json path
        for i in range(0, 3):
            first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
            print(first_name[0])
        # print(jsonpath.jsonpath(json_response, 'data.first_name'))

    def test_delete(self):
        api_endpoint = 'https://reqres.in/api/users/2'
        response = requests.delete(api_endpoint)
        # print(response.status_code)
        assert response.status_code == 204

    @pytest.mark.cook
    def test_cookies(self):
        url = 'https://www.google.com/'
        response = requests.get(url)
        cookies_dict = response.cookies
        print(cookies_dict)
        s = requests.Session()
        print(s)
        # cookies_new = cookies_dict[0]
        # print(cookies_new)
        # print(cookies_dict[0])
