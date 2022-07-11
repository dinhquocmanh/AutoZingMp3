"""
class Director: 
    sinh ra kịch bản để chạy chương trình
    sẽ stop sau bao nhiêu step (default 100)
    scan trong file config xem có bao nhiêu xpath xuất hiện trong trang
    sau đó chọn một random trong đó để click.
    director: đạo diễn
"""


from autozingmp3.browser.base_page import BasePage
from autozingmp3.log.custom_logger import CustomLogger
from autozingmp3.zingmp3.home_page import HomePage
from autozingmp3.zingmp3.control_player import ControlPlayer
import random

class Director(BasePage):
    
    log = CustomLogger()

    def __init__(self, config, driver, step_limit=100 ) -> None:
        self.step_limit=100
        self.step = 0
        self.config = config 
        self.driver= driver
        
    def scan_for_actions(self):
        """
        scan xpaths in configs for available actions
        """
        available_actions = {
            'go_to_homepage' : False,
            'go_to_bxh' : False,
            'login': False,
            'logout': False,
            'search_for_song': False,
            'play_song_in_search_result': False,
            'play_song_in_bxh': False,
            'play': False,
            'pause': False,
            'next': False,
            'previous': False,
            'shuffle': False,
            'like': False,
            'change_volume': False,
            'forward_song': False
        }

        if self.config['home_page']: available_actions['go_to_homepage'] = True 
        if self.config['bxh_url']: available_actions['go_to_bxh'] = True 
        if self.config['cookie_file']: available_actions['login'] = True 
        
        # commons actions in homepage
        if self.config['common']['logout_xpath']: 
            if self.is_element_located(self.config['common']['logout_xpath']):
                available_actions['logout'] = True  
        if self.config['common']['search_bar_xpath']:
            if self.is_element_located(self.config['common']['search_bar_xpath']):
                available_actions['search_for_song'] = True 

        if self.config['common']['play_song_in_search_result']:
            if self.is_element_located(self.config['common']['play_song_in_search_result']):
                available_actions['play_song_in_search_result'] = True 

        if self.config['common']['play_song_in_bxh']:
            if self.is_element_located(self.config['common']['play_song_in_bxh']):
                available_actions['play_song_in_bxh'] = True 
        
        # nếu trình nghe nhạc đang hiện trên trang web thì mới có thể thực hiện các actions sau:
        if self.config['player']['is_showing_xpath']:
            if self.is_element_located(self.config['player']['is_showing_xpath']):
                # player is showing, can pause, stop song,...
                if self.is_element_located(self.config['player']['next_xpath']):
                    available_actions['next'] = True 
                if self.is_element_located(self.config['player']['previous']):
                    available_actions['previous'] = True 
                if self.is_element_located(self.config['player']['shuffle']):
                    available_actions['shuffle'] = True 
                if self.is_element_located(self.config['player']['like']):
                    available_actions['like'] = True 
                if self.is_element_located(self.config['player']['change_volume']):
                    available_actions['change_volume'] = True 
                if self.is_element_located(self.config['player']['forward_song']):
                    available_actions['forward_song'] = True 

        return available_actions

    def get_random_action(self):
        """ 
        khởi tạo biến action list, sau đó gọi lại hàm scan actions để
        xem có bao nhiêu actions có thể thực hiện trên page hiện tại
        sau đó dùng random chọn một actions trong đó
        """
        actions_list = [] 
        available_actions= self.scan_for_actions()
        for k, v in available_actions.items():
            if v: 
                actions_list.append(k)
        
        self.log.info('[+] ActionList: ')
        self.log.info(actions_list)
        # chọn một action random trong list
        choose_action = random.choice(actions_list)
        return choose_action

    def perform_action(self, action_name):
        """
        available_actions = {
            'go_to_homepage' : False,
            'go_to_bxh' : False,
            'login': False,
            'logout': False,
            'search_for_song': False,
            'play_song_in_search_result': False,
            'play_song_in_bxh': False,
            'play': False,
            'pause': False,
            'next': False,
            'previous': False,
            'shuffle': False,
            'like': False,
            'change_volume': False,
            'forward_song': False
        }
        """
        self.step+=1 
        if self.step > self.step_limit:
            self.step = 0
            self.log.info('Completed total: {} steps'.format(str(self.step_limit)))

        self.log.info('[+] Performing action number: {} | name: {}'.format(str(self.step), action_name))
        
        if action_name == 'go_to_homepage':
            self.driver.get(self.config['home_page']) 

        if action_name == 'go_to_bxh':
            try:
                self.driver.get(self.config['bxh_url'])  
            except:
                pass 

        if action_name == 'login':
            homepage= HomePage(driver=self.driver,config=self.config) 
            homepage.load_cookie()
            self.driver.get(self.config['home_page']) 

        if action_name == 'logout':
            homepage = HomePage(driver=self.driver,config=self.config) 
            homepage.logout()

        if action_name == 'search_for_song':
            homepage = HomePage(driver=self.driver,config=self.config) 
            homepage.search_for_song('Tình đầu')

        if action_name == 'play_song_in_search_result':
            homepage = HomePage(driver=self.driver,config=self.config) 
            homepage.play_song_in_search_result()

        if action_name == 'play_song_in_bxh':
            homepage = HomePage(driver=self.driver,config=self.config) 
            homepage.play_song_in_bxh() 

        if action_name == 'play':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.play()
        if action_name == 'pause':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.pause()
        if action_name == 'next':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.next()
        if action_name == 'previous':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.previous()
        if action_name == 'shuffle':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.shuffle() 
        if action_name == 'like':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.like() 
        if action_name == 'change_volume':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.change_volume() 
        if action_name == 'forward_song':
            cp = ControlPlayer(driver=self.driver,config=self.config) 
            cp.forward_random() 
        
        self.log.info('[+] Completed action number: {}'.format(self.step))