from selenium import webdriver
import unittest

class test_arby_homepage(unittest.TestCase):

    def test_title_of_page(self):
        self.chromedriver_location = "Your Driver Loaction"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.get("https://arbys.com/")
        self.assertEqual("Arby's",self.driver.title,"Title does not match")

    def test_title_of_page_updated(self):
        self.chromedriver_location = "Your Driver Loaction"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.get("https://arbys.com/")
        self.assertEqual("Arby's | We Have The Meats®",self.driver.title,"Title does not match")


if __name__ == "__main__":
    unittest.main()

