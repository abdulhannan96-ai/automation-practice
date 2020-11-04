from selenium import webdriver
import Xlutils

chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get("http://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()

path = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/ExcelSheets/LoginTest.xlsx"

rows = Xlutils.getRowCount(path,'Sheet1')
print(rows)

for r in range(2,rows+1):
    user_name = Xlutils.readData(path,'Sheet1',r,1)
    password = Xlutils.readData(path,'Sheet1',r,2)
    driver.find_element_by_name("userName").send_keys(user_name)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()
    if driver.title == "Login: Mercury Tours":
        print("Test Case Passed")
        Xlutils.writeData(path,'Sheet1',r,3,"Test Passed") 
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()


    else:
        print("Test Failed")
        Xlutils.writeData(path,'Sheet1',r,3,"Test Failed") 
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()

