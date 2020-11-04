from selenium import webdriver
import time

chromedriver_location = "Your Driver Loaction"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

#Cature all cookies
cookies = driver.get_cookies()
print("Number of Total Cookies:",len(cookies))
print(cookies)
#adding new cookies to browser
cookie_var = {'name':'MyName','value':'123456789'}
print("After Adding")
driver.add_cookie(cookie_var)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

#deleting a cookie
driver.delete_cookie('MyName')
time.sleep(5)
print("After deleting")
driver.add_cookie(cookie_var)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
