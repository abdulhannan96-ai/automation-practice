import unittest
    # def  setUpModule():
    #     print("Setting Up Module")

    # def tearDownmodule():
    #     print("Close Down Module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("Login")
    @classmethod
    def setUpClass(cls):
        print("Open Application")
    def test01_Search(self):
        print("This is test search")

    def test02_AdvanceSearch(self):
        print("This is advance search method")

    def test03_PrepaidCharge(self):
        print("This is Prepaid Charge Test")

    def test04_PostPiadcharge(self):
        print("This is PostPaid Charge Test")
    
    @classmethod
    def tearDown(self):
        print("Logging out")

    @classmethod
    def tearDownClass(cls):
        print("Closing Appliction")

if __name__ == "__main__":
    unittest.main()