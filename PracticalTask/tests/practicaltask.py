from selenium import webdriver
import unittest
from time import sleep
from SampleProjects.PracticalTask.pages.home import homepage
from SampleProjects.PracticalTask.pages.chapter1 import Chapter1
from SampleProjects.PracticalTask.pages.chapter4 import Chapter4


class practicalTask (unittest.TestCase):
    def setUp(self):
        self.chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://book.theautomatedtester.co.uk/")

    def test1(self):
        driver = self.driver
        home = homepage(driver)
        home.click_chapter1_link()
        chapter1 = Chapter1(driver)
        self.assertTrue(chapter1.text_to_verify, driver.page_source)
        chapter1.click_homePage()
        sleep(2)

    def test2(self):
        driver = self.driver
        home = homepage(driver)
        home.click_chapter4_link()
        chapter4 = Chapter4(driver)
        chapter4.click_selectbox()
        self.assertEqual(chapter4.values_array[0], chapter4.selectFirstValue)
        self.assertEqual(chapter4.values_array[1], chapter4.selectSecondValue)
        self.assertEqual(chapter4.values_array[2], chapter4.selectThirdValue)
        self.assertEqual(chapter4.values_array[3], chapter4.selectFourthValue)
        chapter4.hoverOverElement()
        chapter4.acceptAlert()

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
