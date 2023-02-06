from selenium import webdriver
import re

class inflow():
    def __init__(self):
        driver_path = r"C:\Users\aryan\Desktop\5th Sem\MY\Projects\Voice_Assistant\imp\chromedriver.exe"
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    def get_info(self, query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath", '/html/body/div[3]/form/fieldset/div/input')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '/html/body/div[3]/form/fieldset/button')
        enter.click()
        text = self.driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/p[2]').text
        if text == '':
            text = self.driver.find_element("xpath", '//*[@id="mw-content-text"]/div[1]/p[3]').text
        text = re.sub("[\(\[].*?[\)\]]", "", text)
        count = text.find('.', text.find('.'))
        txt = text[0:count+1]
        return txt
        
