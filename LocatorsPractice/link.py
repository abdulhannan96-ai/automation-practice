from selenium import webdriver

from selenium.webdriver.common.by import By
import time

chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://demo.guru99.com/test/newtours/")
links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))
print("Links Captured Successfully")
for val in links:
    print(val.text)

driver.find_element(By.LINK_TEXT,"REGISTER").click()


driver.close()
driver.quit()