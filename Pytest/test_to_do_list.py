from selenium import webdriver
import unittest
from time import sleep

class testtodolist(unittest.TestCase):
    def setUp(self):
        self.chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.maximize_window()

    def test_click_item(self):
        self.driver.get("https://lambdatest.github.io/sample-todo-app/")
        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()


    def test_adding_item(self):
        self.driver.get("https://lambdatest.github.io/sample-todo-app/")
        self.driver.find_element_by_id("sampletodotext").send_keys("Adding Sample Item")
        sleep(5)
        self.driver.find_element_by_id("addbutton").click()
        sleep(5)
        #clicking dynamically added item
        self.driver.find_element_by_name("li6").click()
        sleep(10)

if __name__ == "__main__":
    unittest.main()

