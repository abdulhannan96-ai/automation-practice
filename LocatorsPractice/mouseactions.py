from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_location = "Your Driver Loaction"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
userManagement= driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()
addBtn = driver.find_elements_by_name("btnAdd")
actions.move_to_element(addBtn).click().perform()

driver.find_elements_by_name("systemUser_employeeName_empName").send_keys("Luke Wright")
driver.find_elements_by_id("systemUser_userName").send_keys("luke_wright@gmail.com")
driver.find_elements_by_id("systemUser_password").send_keys("Kaleemullah1")
driver.find_elements_by_id("systemUser_confirmPassword").send_keys("Kaleemullah1")
driver.find_elements_by_name("btnSave").click()

driver.quit()
