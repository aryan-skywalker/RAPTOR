from selenium import webdriver
import re
import pywhatkit


class play_video():
    def __init__(self):
        driver_path = r"C:\Users\aryan\Desktop\5th Sem\MY\Projects\Voice_Assistant\imp\chromedriver.exe"
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        self.driver = webdriver.Chrome(
            executable_path=driver_path, chrome_options=option)

    def play_vid(self, query):
        self.query = query
        url = "https://www.youtube.com/watch?v="+query
        pywhatkit.playonyt(url)
