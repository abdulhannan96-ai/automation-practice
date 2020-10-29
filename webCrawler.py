import csv
from selenium import webdriver
chromedriver_location = "C:/Users/Abdul Hannan/AppData/Local/Programs/Python/Python39/Drivers/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
MAX_PAGE_NUM = 5
MAX_PAGE_DIGIT = 3
with open('result.csv', 'w') as f:
    f.write("Buyers, Prices \n")
for i in range(1, MAX_PAGE_NUM+1):
    page_num = (MAX_PAGE_DIGIT - len(str(i)))*"0"+str(i)
    url = "http://econpy.pythonanywhere.com/ex/"+ page_num+".html"
    driver.get(url)
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    number_of_buyers_in_one_page = len(buyers)
    with open('result.csv','a') as f:
     for i in range(number_of_buyers_in_one_page):
         f.write(buyers[i].text+","+prices[i].text+"\n")



driver.close()


    


    



