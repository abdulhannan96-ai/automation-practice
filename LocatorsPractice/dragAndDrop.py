from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_location = "Your Driver Loaction"
driver = webdriver.Chrome(chromedriver_location)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element_by_id("box1")
target_Drop = driver.find_element_by_id("box101")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

source_element = driver.find_element_by_id("box2")
target_Drop = driver.find_element_by_id("box102")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

source_element = driver.find_element_by_id("box3")
target_Drop = driver.find_element_by_id("box103")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

source_element = driver.find_element_by_id("box4")
target_Drop = driver.find_element_by_id("box104")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

source_element = driver.find_element_by_id("box5")
target_Drop = driver.find_element_by_id("box105")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

source_element = driver.find_element_by_id("box6")
target_Drop = driver.find_element_by_id("box106")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

source_element = driver.find_element_by_id("box7")
target_Drop = driver.find_element_by_id("box107")
actions =ActionChains(driver)
actions.drag_and_drop(source_element,target_Drop).perform()

