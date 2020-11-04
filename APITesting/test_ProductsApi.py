import unittest
import requests
import json

class productapitest(unittest.TestCase):
    def test_write_csv_file(self):
        r = requests.get("https://chercher.tech/sample/api/product/read")
        print(r.json())
        print(r.status_code)

    def test_create_product(self):
        api_url = "https://chercher.tech/sample/api/product/create"
        data = json.dumps({'name':'product1','description':'This is description for product1'})
        resp = requests.put(api_url,data)
        print(resp)
    def test_edit_product(self):
        api_url = "https://chercher.tech/sample/api/product/update"
        data = json.dumps({'id':'3828','name':'Product1edited','description':'This is edited description of product1','price':'10000'})
        resp  = requests.post(api_url,data)
        print(resp)
    def test_read_specific(self):
        r = requests.get("https://chercher.tech/sample/api/product/read?id=3829")
        print(r.json())
        print(r.status_code)
    def test_delete_specific(self):
        api_url = "https://chercher.tech/sample/api/product/delete?id=3829"
        resp = requests.delete(api_url)
        print(resp)


if __name__ == "__main__":
    unittest.main()