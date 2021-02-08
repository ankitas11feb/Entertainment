from selenium import webdriver
import time


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/HP4/PycharmProjects/youtube/chromedriver.exe")

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]')
        video.click()


playonl = music()
time.sleep(1)
playonl.play('dynamite by bts')
