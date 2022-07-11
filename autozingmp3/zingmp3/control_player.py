"""
Class ControlPlayer(BasePage)
    Có các chức năng điều khiển các button của player
    Next, previous, pause, Like, Suffle, repeat
"""

from turtle import width
from autozingmp3.browser.base_page import BasePage
from autozingmp3.log.custom_logger import CustomLogger
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ControlPlayer(BasePage):
    log = CustomLogger()

    def __init__(self, driver,config):
        super().__init__(driver)
        self.config = config 
    
    def is_player_showing(self) -> bool:
        if self.is_element_located(self.config['player']['is_showing_xpath']): 
            return True
        else:
            return False

    def next(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click next
        self.elementClick(self.config['player']['next_xpath'])
    
    def previous(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click previous
        self.elementClick(self.config['player']['previous_xpath'])

    def play(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click play/pause
        self.elementClick(self.config['player']['play_xpath'])

    def pause(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click play/pause
        self.elementClick(self.config['player']['pause_xpath'])

    def shuffle(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click shuffle
        self.elementClick(self.config['player']['shuffle_xpath'])

    def repeat(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click repeat
        self.elementClick(self.config['player']['repeat_xpath'])

    def like(self):
        """
        .//button[contains(@class,'zm-tooltip-btn animation-like')]
        """
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        self.elementClick(self.config['player']['like'])

    def change_volume(self, percent=10):
        en =  self.getElement("//div[@class='zm-player-volume']/div/div")
        height = en.size['height']
        width = en.size['width']
        print("off set: ", percent * width / 100)
        move = ActionChains(self.driver)
        move.click_and_hold(en).move_by_offset(percent * width / 100, 0).release().perform()

    def get_length(self):
        """
        Get length of playing song, 
        return length in seconds
        """

    def forward_to(self, percent):
        "Tua bài hát đến giây thứ bao nhiêu"
        en =  self.getElement("//div[@class='zm-slider-bar']")
        height = en.size['height']
        width = en.size['width']
        #width =50
        print("off set max: ",width)
        move = ActionChains(self.driver)
        move.move_to_element_with_offset(en,0,0)
        move.move_by_offset(50 * width / 100, 0).click().perform()

    def forward_random(self):
        pass  