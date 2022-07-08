"""
Class ControlPlayer(BasePage)
Có các chức năng điều khiển các button của player
Next, previous, pause, Like, Suffle, repeat
"""

from autozingmp3.browser.base_page import BasePage
from autozingmp3.log.custom_logger import CustomLogger
from selenium.webdriver.common.by import By

class ControlPlayer(BasePage):
    log = CustomLogger()

    def __init__(self, driver):
        super().__init__(driver)
    
    def is_player_showing(self) -> bool:
        if self.is_element_located("//div[@class='player-controls clickable']"): 
            return True
        else:
            return False

    def next(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click next
        self.elementClick("//button[contains(@class,'zm-tooltip-btn btn-next')]")
    
    def previous(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click previous
        self.elementClick("//button[contains(@class,'zm-tooltip-btn btn-pre')]")

    def play_pause(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click play/pause
        self.elementClick("//button[contains(@class,'zm-tooltip-btn btn-play')]")

    def shuffle(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click shuffle
        self.elementClick("//button[contains(@class,'zm-tooltip-btn btn-shuffle')]")

    def repeat(self):
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        # click repeat
        self.elementClick("//button[contains(@class,'zm-tooltip-btn btn-repeat')]")

    def like(self):
        """
        .//button[contains(@class,'zm-tooltip-btn animation-like')]
        """
        if not self.is_player_showing(): 
            self.log.debug('Can not find player.')
            return False 
        try:
            player = self.getElement("//div[@class='player-controls clickable']")
            like_btn = player.find_element(By.XPATH, ".//button[contains(@class,'zm-tooltip-btn animation-like')]")
            like_btn.click()
        except:
            self.log.error('Click like failed')