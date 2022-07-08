import time
from autozingmp3.browser.base_page import BasePage
import os 
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver) 

    def export_cookie(self):
        """
        Export cookie of the account and save in default_cookie.json
        """
        if not os.path.exists('cookies/'):
            os.mkdir('cookies')
        outputfile = f'default_cookie.json'
        self.log.info('Exporting cookie -> .json')
        if 'zingmp3.vn' in self.driver.current_url:
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
        inputfile = 'default_cookie.json'
        if 'zingmp3.vn' in self.driver.current_url:
            self.log.info('Loading cookie <- .json')
            cookies = self.driver.get_cookies()
            with open('cookies/'+inputfile, 'r', newline='') as inputdata:
                cookies = json.load(inputdata)
            for cookie in cookies:
                try:
                    print(cookie)
                    self.driver.add_cookie(cookie)
                except Exception as e:
                    pass 
            self.log.info('load cookie completed.')
        return

    def search_for_song(self, song_name: str) -> None:
        """
        Search for song by name,
        xpath: //input[contains(@placeholder,'Tìm kiếm bài hát')]
        Return:
            List of songs
        """
        search_xpath = "//input[contains(@placeholder,'Tìm kiếm bài hát')]"
        if not self.is_element_located(search_xpath):
            self.log.error('Can not find searchbar')
            return 
        search_bar = self.getElement(search_xpath) 
        search_bar.send_keys(song_name)
        search_bar.send_keys(Keys.ENTER)
        
    def search_for_song_method2(self, song_name: str):
        """
        https://zingmp3.vn/tim-kiem/bai-hat?q=L%E1%BB%91i%20nh%E1%BB%8F
        """
        pass 

    def play_song():
        """
        Play the first song in search results
        """

    def get_top_100_rap(self):
        """
        """
        top100_elements = self.getElementList("//div[@class='select-item']")
        for element in top100_elements:
            print("==========")
            print(element.text)
        # play the second song
        song_thumb = top100_elements[1].find_element(By.XPATH, ".//div[@class='song-thumb']")
        song_thumb.click()