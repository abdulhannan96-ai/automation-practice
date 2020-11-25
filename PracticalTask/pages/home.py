class homepage():
    def __init__(self,driver):
        self.driver = driver
        self.chapter1_linktext = "Chapter1" #located by linktext
        self.chapter4_linktext = "Chapter4" #locted by linktext

    def click_chapter1_link(self):
        self.driver.find_element_by_link_text(self.chapter1_linktext).click()

    def click_chapter4_link(self):
        self.driver.find_element_by_link_text(self.chapter4_linktext).click()
