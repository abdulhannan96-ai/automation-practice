from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.find_element_by_id("RESULT_TextField-1").send_keys("Abdul Hannan Imtiaz")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Imtiaz")
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
# print(status)
# #driver.find_element_by_id("RESULT_RadioButton-7_0").click()
# print(status)
# driver.find_element_by_id("RESULT_CheckBox-8_1").click()
# driver.find_element_by_id("RESULT_CheckBox-8_2").click()

obj = Select(driver.find_element_by_name("RESULT_RadioButton-9"))
obj.select_by_index(3)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users/Abdul Hannan/Pictures/2018-08/car3.png")