import pandas as pd
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup


class Droughts:
    states = None
    url = None
    iterState = None

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
        fipsDf = pd.read_csv('files/fips.csv')
        for state in self.states:
            self.changeState()
            data.append(self.getDataForState(fipsDf))
            self.iterState += 1
        return data

    def getDataForState(self, fipsDf):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.select_one("#datatabl")
        table = pd.read_html(str(div))[0]
        table.insert(0, 'State', self.states[self.iterState], True)
        table.insert(1, 'Postal code', fipsDf['postal code'][self.iterState], True)
        table.insert(2, 'Fips', fipsDf['fips'][self.iterState], True)
        return table

dataframe = pd.DataFrame()
droughts = Droughts(r'https://droughtmonitor.unl.edu/DmData/DataTables.aspx')
dfList = droughts.getData()
for df in dfList:
    dataframe = dataframe.append(df)
dataframe.reset_index(drop=True, inplace=True)

dataframe['LEVEL'] = dataframe['DSCI'] // 100

dataframe.to_csv('files/drought.csv')