class Chapter1():
    def __init__(self,driver):
        self.driver  = driver
        self.text_to_verify = "Assert that this text is on the page" #text to check
        self.homepage_linktext = "Home Page"

    def click_homePage(self):
        self.driver.find_element_by_link_text(self.homepage_linktext).click()




