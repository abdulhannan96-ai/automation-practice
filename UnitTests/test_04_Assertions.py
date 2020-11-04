from selenium import webdriver
import unittest

class testAssertions(unittest.TestCase):
    def test01_search(self):
        self.chromedriver_location = "Your Driver Loaction"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.get("https://google.com")
        self.titleOfWebPage  = self.driver.title
        #Positive Condition
        #self.assertEqual("Google",titleOfWebPage,"Webpage title is not same")
        #Negative Condition
        self.assertNotEqual("Google123",self.titleOfWebPage)
        self.driver.close()
    def test02_searchAsserttrueFalse(self):
        self.chromedriver_location = "Your Driver Loaction"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.get("https://google.com")
        self.titleOfWebPage  = self.driver.title
        #for positive condition
        self.assertTrue(self.titleOfWebPage=="Google")
        #for negative condition
        #self.assertNotEqual(self.titleOfWebPage=="Google")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
