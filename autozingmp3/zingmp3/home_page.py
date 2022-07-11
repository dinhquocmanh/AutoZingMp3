"""
class HomePage:
    thực hiện các chức năng cơ bản trên homepage zingmp3
    như đăng nhập, tìm kiếm bài hát, xem bxh,..
"""
import time
from autozingmp3.browser.base_page import BasePage
import os 
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver, config):
        super().__init__(driver) 
        self.config = config

    def export_cookie(self):
        """
        Export cookie of the account and save in default_cookie.json
        """
        if not os.path.exists('cookies/'):
            os.mkdir('cookies')
        outputfile = self.config['cookie_file']
        self.log.info('Exporting cookie -> .json')
        cookies = self.driver.get_cookies()
        with open('cookies/'+outputfile, 'w', newline='') as outputdata:
            json.dump(cookies, outputdata,indent=4)
    
    def load_cookie(self):
        """
        Load cookie from input file
        """
        if not os.path.exists('cookies/'):
            self.log.error('Cookies folder not found!')
            return False
        inputfile = self.config['cookie_file']
        self.log.info('Loading cookie <- .json')
        cookies = self.driver.get_cookies()
        with open('cookies/'+inputfile, 'r', newline='') as inputdata:
            cookies = json.load(inputdata)
        for cookie in cookies:
            try:
                #print(cookie)
                self.driver.add_cookie(cookie)
            except Exception as e:
                pass 
        self.log.info('load cookie completed.')

    def logout(self):
        pass 

    def search_for_song(self, song_name: str) -> None:
        """
        Search for song by name,
        Return:
            List of songs
        """
        search_xpath = self.config['common']['search_bar_xpath']
        if not self.is_element_located(search_xpath):
            self.log.error('Can not find searchbar')
            return 
        search_bar = self.getElement(search_xpath) 
        search_bar.send_keys(song_name)
        search_bar.send_keys(Keys.ENTER)
    

    def play_song_in_search_result():
        """
        Play the first song in search results
        """
        pass 


    def play_song_in_bxh(self):
        """
        todo: ,,,,
        """
        top100_elements = self.getElementList("//div[@class='select-item']")
        for element in top100_elements:
            print("==========")
            print(element.text)
        # play the second song
        song_thumb = top100_elements[1].find_element(By.XPATH, ".//div[@class='song-thumb']")
        song_thumb.click()