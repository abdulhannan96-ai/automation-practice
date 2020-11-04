import unittest
from selenium import webdriver

class searchEngines(unittest.TestCase):
    def test_searchGoogle(self):
        self.path = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://google.com")
        print("The title of page is:"+ self.driver.title)
        self.driver.close()

    def test_searchBing(self):
        self.path = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://bing.com")
        print("The title of page is:"+ self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



