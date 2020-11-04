import requests
import unittest
import json
import jsonpath

class test_users_api(unittest.TestCase):

    def test_get_users(self):
        self.get_url = "https://reqres.in/api/users?page=2"
        self.response = requests.get(self.get_url)
        print(self.response.content)

    def test_get_users_jsonpath(self):
        self.get_url = "https://reqres.in/api/users?page=2"
        self.response = requests.get(self.get_url)
        self.json_response = json.loads(self.response.text)
        # print(self.response.text)
        self.pages = jsonpath.jsonpath(self.json_response, 'total_pages')
        print(self.pages[0])
        #getting all first names
        for i in range(0, 6):
            emails = jsonpath.jsonpath(self.json_response, 'data['+str(i)+'].email')
            print(emails[0])

    def test_delete_user(self):
        self.delete_url= "https://reqres.in/api/users/2"
        self.response = requests.delete(self.delete_url)
        print(self.response.status_code)
        assert self.response.status_code == 204

    def test_create_new_user(self):
        self.create_url = "https://reqres.in/api/users"
        file = open('create User Json file locatio here','r')
        json_input = file.read()
        request_json = json.loads(json_input)
        print(request_json)
        self.response = requests.post(self.create_url,request_json)
        print(self.response.content)
        assert self.response.status_code == 201
        #get the id
        response_json = json.loads(self.response.text)
        id = jsonpath.jsonpath(response_json,'id')
        print(id[0])

    def test_update_user(self):
        self.update_url = "https://reqres.in/api/users/2"
        file = open('createuser.json location here','r')
        json_input = file.read()
        request_json = json.loads(json_input)
        self.response = requests.put(self.update_url,request_json)
        assert self.response.status_code ==200
        #parse content to fetch from result data
        response_json = json.loads(self.response.text)
        updated_li= jsonpath.jsonpath(response_json,'updatedAt')
        print(updated_li[0])


if __name__ == "__main__":
    unittest.main()
