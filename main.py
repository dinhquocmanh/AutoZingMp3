from autozingmp3.browser.driver_factory import WebDriverFactory, WebDriverConfigs
from autozingmp3.log.custom_logger import CustomLogger
from autozingmp3.zingmp3.home_page import HomePage
from autozingmp3.zingmp3.control_player import ControlPlayer
from autozingmp3.zingmp3.director import Director
import sys 
import time 
import json 
import subprocess

log = CustomLogger()


def load_config(): 
    """
    Load config from file to a dictionary
    Return:
        <dict> configs
    """
    configs = {}
    configs = json.load(open('configs/config.json',mode='r',encoding='utf-8')) 
    return configs

def kill_all_driver():
    subprocess.run(['pkill chromedriver'],shell=True) 


if __name__ == "__main__":

    # clean cpu before doing something to prevent errors
    kill_all_driver()
    log.info('[+] Killed all chromedriver')

    # load config main
    config = load_config()

    # select
    select_site = "zingmp3.vn"
    config = config[select_site]

    # config and start the web driver
    wdconfig = WebDriverConfigs()
    wdf = WebDriverFactory(configs=wdconfig)
    driver = wdf.getWebDriverInstance()
    log.info('[+] Init webdriver success.')

    # go to homepage
    driver.get(config['home_page'])
    time.sleep(5)

    # Khởi tạo lớp director tự động tạo kịch bản và thực hiện kịch bản
    step_limit = 10 
    director = Director(config=config,driver=driver,step_limit=step_limit)
    for i in range(0,step_limit):
        action_name = director.get_random_action()
        director.perform_action(action_name=action_name)
        time.sleep(5)
    
    while True:
        try:
            input()
        except KeyboardInterrupt:
            sys.exit()
