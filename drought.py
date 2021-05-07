import pandas as pd
from selenium import webdriver

class Droughts:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"/home/amit/DataScienceProject/PredictDroughts/geckodriver")
        self.url = r'https://droughtmonitor.unl.edu/Data/DataTables.aspx'
        self.numberOfSates = 54
        self.week = []
        self.none = []
        self.d0 = []
        self.d1 = []
        self.d2 = []
        self.d3 = []
        self.d4 = []
        self.dsci = []

    def __exit__(self):
        self.driver.quit()

    def getStartDataDroughts(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("atype_chosen").click()
        self.driver.find_element_by_xpath("//li[@class='active-result' and text()='State']").click()
        self.driver.find_element_by_name("datatabl_length").click()
        self.driver.find_element_by_xpath("//select[@name='datatabl_length']/option[text()='All']").click()
    
    def getData():
        pass

# droughts = Droughts()
# droughts.getStartDataDroughts()