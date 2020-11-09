from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from time import sleep

class appointment(unittest.TestCase):
    def setUp(self):
        self.chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://katalon-demo-cura.herokuapp.com/")
        self.driver.find_element_by_id("btn-make-appointment").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("txt-username").send_keys("John Doe")
        self.driver.find_element_by_id("txt-password").send_keys("ThisIsNotAPassword")
        self.driver.find_element_by_id("btn-login").click()
        self.driver.implicitly_wait(3)

    def test_appointment(self):
        self.driver.find_element_by_id("combo_facility").click()
        Select(self.driver.find_element_by_id("combo_facility")).select_by_visible_text("Hongkong CURA Healthcare Center")
        self.driver.find_element_by_id("chk_hospotal_readmission").click()
        self.driver.find_element_by_id("radio_program_medicaid").click()
        self. driver.find_element_by_xpath("//section[@id='appointment']/div/div/form/div[4]/div/div/div").click()
        self.driver.find_element_by_xpath("//tr[3]/td[7]").click()
        self.driver.find_element_by_id("txt_comment").send_keys("I need urgent Appointment")
        self.driver.find_element_by_id("btn-book-appointment").click()
        self.driver.find_element_by_id("menu-toggle").click()
        self.driver.find_element_by_link_text("History").click()
        sleep(5)
        self.driver.save_screenshot("AppointmentBooked.png")
        sleep(5)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
