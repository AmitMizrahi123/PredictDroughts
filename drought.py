import pandas as pd
import numpy as np
from selenium import webdriver
import requests
from bs4 import BeautifulSoup


class Droughts:
    states = None
    url = None
    week = []

    def __init__(self, url):
        self.url = url
        self.setUp(self.url)

    def __del__(self):
        self.driver.quit()

    def setUp(self, url):
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("atype_chosen").click()
        self.driver.find_element_by_xpath("//li[@class='active-result' and text()='State']").click()
        self.driver.find_element_by_name("datatabl_length").click()
        self.driver.find_element_by_xpath("//select[@name='datatabl_length']/option[text()='All']").click()
        selectElement = self.driver.find_element_by_id("asel")
        self.states = [x.get_attribute("textContent") for x in selectElement.find_elements_by_tag_name("option")]

    def getData(self):
        # df = pd.DataFrame()
        # isAlabama = True
        # oneTimeWeek = True

        for state in self.states:
            pass
            
        #     df = df.append(self.getDataForState(state, isAlabama, oneTimeWeek), ignore_index=True)
        #     isAlabama = False
        #     oneTimeWeek = False
        # return df

    def getDataForState(self, state, isAlabama, oneTimeWeek):
        none = []
        d0 = []
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        dsci = []
        table = self.driver.find_element_by_id("datatabl")
        tbody = table.find_element_by_tag_name('tbody')
        if not isAlabama:
            pass
        for tr in tbody.find_elements_by_tag_name('tr'):
            for index, td in enumerate(tr.find_elements_by_tag_name('td')):
                if index % 8 == 0 and oneTimeWeek:
                    self.week.append(td.text)
                elif index % 8 == 1:
                    none.append(td.text)
                elif index % 8 == 2:
                    d0.append(td.text)
                elif index % 8 == 3:
                    d1.append(td.text)
                elif index % 8 == 4:
                    d2.append(td.text)
                elif index % 8 == 5:
                    d3.append(td.text)
                elif index % 8 == 6:
                    d4.append(td.text)
                elif index % 8 == 7:
                    dsci.append(td.text)
        data = {
            'state': state,
            'week': self.week,
            'none': none,
            'd0': d0,
            'd1': d1,
            'd2': d2,
            'd3': d3,
            'd4': d4,
            'dsci': dsci,
        }
        return data
                

droughts = Droughts(r'https://droughtmonitor.unl.edu/DmData/DataTables.aspx')
df = droughts.getData()
print(df)