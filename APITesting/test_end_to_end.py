import jsonpath
import json
import requests

def test_add_new_student():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\Abdul Hannan\\AppData\\Local\\Programs\\Python\\Python39\\SampleProjects\\APITesting\\Student.json','r')
    file_input = file.read()
    request_json = json.loads(file_input)
    response = requests.post(api_url,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('C:\\Users\\Abdul Hannan\\AppData\\Local\\Programs\\Python\\Python39\\SampleProjects\\APITesting\\technicaldetails.json','r')
    file_input = file.read()
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    request_json = json.loads(file_input)
    response = requests.post(tech_url, request_json)
    print(response.text)

    address_url = "http://thetestingworldapi.com/api/addresses"
    file = open('C:\\Users\\Abdul Hannan\\AppData\\Local\\Programs\\Python\\Python39\\SampleProjects\\APITesting\\address.json','r')
    file_input = file.read()
    request_json['stId'] = id[0]
    request_json = json.loads(file_input)
    response = requests.post(address_url, request_json)
    print(response.status_code)


    final_url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_url)
    print(response.text)

