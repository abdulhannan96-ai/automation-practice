import unittest
class AppTesting(unittest.TestCase):
    @unittest.SkipTest
    def test01_searchTest(self):
        print("This is test search")
    @unittest.skip("Skipping this because it's not ready") 
    def test02_AdvanceSearch(self):
        print("This is advance search method")
    @unittest.skipIf(1==1,"1 is equal to 1")
    def test03_PrepaidCharge(self):
        print("This is Prepaid Charge Test")

    def test04_PostPiadcharge(self):
        print("This is PostPaid Charge Test")

    def  test05_LoginByGmail(self):
        print("This is Login by gmail Test")

    def  test06_LoginBytwitter(self):
        print("This is Login by Twitter Test")
  

if __name__ == "__main__":
    unittest.main()