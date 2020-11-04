from selenium import webdriver
import time

chromedriver_location = "Your Driver Loaction"
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(10)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element_by_id("textbox").send_keys("Generate My File")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

#downloadPDF

driver.find_element_by_id("pdfbox").send_keys("Generate my PDF")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

time.sleep(5)
