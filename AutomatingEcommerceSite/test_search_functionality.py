from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from time import sleep

class search_and_add(unittest.TestCase):

    def setUp(self):
        self.chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # def test_search_category(self):
    #     self.driver.get("http://automationpractice.com/index.php")
    #     self.driver.find_element_by_name("search_query").send_keys("Printed")
    #     sleep(3)
    #     self.driver.find_element_by_name("submit_search").click()
    #     self.driver.execute_script("window.scrollBy(0,525)", "")
    #     sleep(4)
    #     image = "2"
    #     element_to_hover = self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li["+image+"]/div/div[1]/div/a[1]/img")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element_to_hover).perform()
    #     sleep(5)
    #     self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[2]/div[2]/a[1]/span").click()
    #     sleep(10)
    #
    # def test_validate_cart(self):
    #     self.test_search_category()
    #     self.driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a").click()
    #     sleep(5)

    def test_add_with_different_categories(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.execute_script("window.scrollBy(0,1200)", "")
        element_to_hover = self.driver.find_element_by_xpath("//*[@id='homefeatured']/li[6]/div/div[1]/div/a[1]/img")
        action = ActionChains(self.driver)
        action.move_to_element(element_to_hover).perform()
        self.driver.find_element_by_xpath("//*[@id='homefeatured']/li[6]/div/div[2]/div[2]/a[2]/span").click()
        sleep(2)
        self.driver.find_element_by_id("quantity_wanted").clear()
        self.driver.find_element_by_id("quantity_wanted").send_keys("3")
        obj = Select(self.driver.find_element_by_name("group_1"))
        obj.select_by_visible_text("M")
        self.driver.find_element_by_name("White").click()
        self.driver.find_element_by_xpath("//*[@id='add_to_cart']/button").click()
        self.driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a").click()
        sleep(10)




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
