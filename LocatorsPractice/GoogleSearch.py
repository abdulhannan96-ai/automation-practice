from selenium import webdriver
import unittest

#======================================================================================================================================
class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        cls.driver = webdriver.Chrome(chromedriver_location)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()

    def test_search_raghav(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")





    
    











