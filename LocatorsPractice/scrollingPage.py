from selenium import webdriver
import time

chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)
driver.minimize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(5)
#Scroll down by Pixel

# driver.execute_script("window.scrollBy(0,1500)","")
# time.sleep(5)
# driver.close()

#scroll down till element is visible 
flag = driver.find_elements_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[35]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flag)