import unittest
import HtmlTestRunner
from selenium import webdriver
class orangehrmlogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.chromedriver_location = "Your Driver Location"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test01_homepagetitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title, "Title does not match")

    def test02_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM",self.driver.title, "Titles does not match")

    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Path where html report should be produced'))


