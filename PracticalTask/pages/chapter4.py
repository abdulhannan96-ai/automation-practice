from selenium.webdriver.common.action_chains import ActionChains
class Chapter4():
    def __init__(self,driver):
        self.driver = driver
        self.select_box = "selecttype"
        self.values_array = ["Selenium IDE", "Selenium Core", "Selenium RC", "Selenium Grid"]
        self.selectFirstValue = self.driver.find_element_by_xpath("//*[@id='selecttype']/option[1]").text
        self.selectSecondValue = self.driver.find_element_by_xpath("//*[@id='selecttype']/option[2]").text
        self.selectThirdValue = self.driver.find_element_by_xpath("//*[@id='selecttype']/option[3]").text
        self.selectFourthValue = self.driver.find_element_by_xpath("//*[@id='selecttype']/option[4]").text
        self.hoverElement =  "hoverOver"

    def click_selectbox(self):
        self.driver.find_element_by_id(self.select_box).click()

    def hoverOverElement(self):
        element_to_hover_over = self.driver.find_element_by_id(self.hoverElement)  # going to hover element
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over) #hovering
        hover.perform() #hovered

    def acceptAlert(self):
        obj = self.driver.switch_to.alert  # switching control of driver to alert
        obj.accept() # accepting alert
