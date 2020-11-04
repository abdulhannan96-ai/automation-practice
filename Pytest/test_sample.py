import pytest
from selenium import webdriver
import time  
def test_setup():
    global driver
    chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_location)
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

def test_logout():
    print("logging out")


def test_teardown():
    driver.close()
    driver.quit()
    print("test completed")