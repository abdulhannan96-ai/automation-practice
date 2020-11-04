from selenium import webdriver
from selenium.webdriver.support.ui import Select
import  time
chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get("http://demo.automationtesting.in/Register.html")
# driver.maximize_window()
#sending First Name
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[1]/input").send_keys("Abdul Hannan")
#sending Last Name
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[2]/input").send_keys("Imtiaz")
#sendin Address
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("House no 244, Street 91, E11/2")
#sending Photo
driver.find_element_by_xpath("//*[@id='imagesrc']").send_keys("E:/Hanan Data/documents/350x350.jpg")
#sending Email
driver.find_element_by_xpath("//*[@id='eid']/input").send_keys("ahimtiaz3@gmail.com")
#sending Phone
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[4]/div/input").send_keys("03345855556")
#selecting Gender
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").click()
#selecting Hobby
driver.find_element_by_id("checkbox1").click()
driver.find_element_by_id("checkbox3").click()
#languages
driver.find_element_by_id("msdd").click()
driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li[2]").click()
driver.find_element_by_link_text("Danish").click()
driver.find_element_by_link_text("Filipino").click()
driver.find_element_by_id("basicBootstrapForm").click()
#skills
driver.find_element_by_id("Skills").click()
Select(driver.find_element_by_id("Skills")).select_by_visible_text("Oracle")
driver.find_element_by_id("Skills").click()

#country
driver.find_element_by_id("countries").click()
Select(driver.find_element_by_id("countries")).select_by_visible_text("Austria")
driver.find_element_by_id("countries").click()

#country2
# driver.find_element_by_id("select2-country-container").click()
# driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[10]/div/span/span/span").click()
# driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[10]/div/span/span/span").click()
# driver.find_element_by_xpath("//input[@type='search']").clear()
# driver.find_element_by_xpath("//input[@type='search']").send_keys("ne")

#year month date
driver.find_element_by_id("yearbox").click()
Select(driver.find_element_by_id("yearbox")).select_by_visible_text("1996")
driver.find_element_by_id("yearbox").click()
driver.find_element_by_xpath("(//select[@type='text'])[4]").click()
Select(driver.find_element_by_xpath("(//select[@type='text'])[4]")).select_by_visible_text("March")
driver.find_element_by_xpath("(//select[@type='text'])[4]").click()
driver.find_element_by_id("daybox").click()
Select(driver.find_element_by_id("daybox")).select_by_visible_text("1")
driver.find_element_by_id("daybox").click()

#




time.sleep(6)
driver.quit()
driver.close()