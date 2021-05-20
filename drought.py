import pandas as pd
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
from fips import returnFipsDataFrame


class Droughts:
    states = None
    url = None
    iterState = None
    # week = None

    def __init__(self, url):
        self.url = url
        self.setUp(self.url)

    def __del__(self):
        self.driver.quit()

    def setUp(self, url):
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.driver.find_element_by_id("atype_chosen").click()
        self.driver.find_element_by_xpath("//li[@class='active-result' and text()='State']").click()
        self.driver.find_element_by_name("datatabl_length").click()
        self.driver.find_element_by_xpath("//select[@name='datatabl_length']/option[text()='All']").click()
        selectElement = self.driver.find_element_by_id("asel")
        self.states = [elem.get_attribute("textContent") for elem in selectElement.find_elements_by_tag_name("option")]
    
    def changeState(self):
        dropDownSelect = self.driver.find_element_by_id("asel_chosen")
        dropDownSelect.click()
        dropDownUl = dropDownSelect.find_element_by_class_name("chosen-results")
        dropDownLis = dropDownUl.find_elements_by_class_name('active-result')
        dropDownLis[self.iterState].click()

    def getData(self):
        self.iterState = 0
        data = []
        for state in self.states:
            self.changeState()
            data.append(self.getDataForState())
            self.iterState += 1
        return data

    def getDataForState(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.select_one("#datatabl")
        table = pd.read_html(str(div))[0]
        table.insert(1, 'State', self.states[self.iterState], True)
        return table

    # def getData(self):
    #     df = pd.DataFrame()
    #     isAlabama = True
    #     oneTimeWeek = True
    #     x = 0

    #     for state in self.states:
    #         elem = self.driver.find_element_by_id("asel_chosen")
    #         elem.click()
    #         ul = elem.find_element_by_class_name("chosen-results")
    #         lis = ul.find_elements_by_class_name('active-result')
    #         for i in range(x, len(lis)):
    #             if lis[i].text == state:
    #                 lis[i].click()
    #                 df = df.append(self.getDataForState(state, isAlabama, oneTimeWeek), ignore_index=True)
    #                 isAlabama = False
    #                 oneTimeWeek = False
    #                 x += 1
    #                 break
    #     return df

    # def getDataForState(self, state, isAlabama, oneTimeWeek):
    #     none = []
    #     d0 = []
    #     d1 = []
    #     d2 = []
    #     d3 = []
    #     d4 = []
    #     dsci = []
    #     table = self.driver.find_element_by_id("datatabl")
    #     tbody = table.find_element_by_tag_name('tbody')
    #     tr = tbody.find_elements_by_tag_name('tr')
    #     tds = tr.find_elements_by_tag_name('td')
    #     for index, td in enumerate(tds):
    #         if index % 8 == 0 and oneTimeWeek:
    #             self.week.append(td.text)
    #         elif index % 8 == 1:
    #             none.append(td.text)
    #         elif index % 8 == 2:
    #             d0.append(td.text)
    #         elif index % 8 == 3:
    #             d1.append(td.text)
    #         elif index % 8 == 4:
    #             d2.append(td.text)
    #         elif index % 8 == 5:
    #             d3.append(td.text)
    #         elif index % 8 == 6:
    #             d4.append(td.text)
    #         elif index % 8 == 7:
    #             dsci.append(td.text)
    #     data = {
    #         'state': state,
    #         'week': self.week,
    #         'none': none,
    #         'd0': d0,
    #         'd1': d1,
    #         'd2': d2,
    #         'd3': d3,
    #         'd4': d4,
    #         'dsci': dsci,
    #     }
    #     return data
                

droughts = Droughts(r'https://droughtmonitor.unl.edu/DmData/DataTables.aspx')
# df = droughts.getData()
# print(df)

dataframe = pd.DataFrame()
dfList = droughts.getData()
for df in dfList:
    dataframe = dataframe.append(df)
dataframe.reset_index(drop=True, inplace=True)