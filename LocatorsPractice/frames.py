from selenium import webdriver
import time

chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to_default_content()
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)
driver.switch_to_default_content()
time.sleep(3)
driver.switch_to_frame("classFrame")
driver.find_elements_by_xpath('/html/body/div[1]/ul/li[5]/a').click()
