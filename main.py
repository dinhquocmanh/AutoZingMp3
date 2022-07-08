from autozingmp3.browser.driver_factory import WebDriverFactory, WebDriverConfigs
from autozingmp3.zingmp3.home_page import HomePage
from autozingmp3.zingmp3.control_player import ControlPlayer
import sys 
import time 

if __name__ == "__main__":

    configs = WebDriverConfigs()
    wdf = WebDriverFactory(configs=configs)
    driver = wdf.getWebDriverInstance()

    # open zing mp3
    driver.get('https://zingmp3.vn/')

    # init home page object
    homepage = HomePage(driver=driver)
    # login by cookies
    homepage.load_cookie()
    driver.get('https://zingmp3.vn/')

    # search for song name
    #homepage.search_for_song('Cạn cả nước mắt')

    # get top 100
    url = 'https://zingmp3.vn/album/Top-100-Nhac-Rap-Viet-Nam-Hay-Nhat-Lil-Wuyn-Binz-Rhymastic-Phao/ZWZB96AI.html'
    driver.get(url)
    time.sleep(5)
    homepage.get_top_100_rap()

    # controls
    cp = ControlPlayer(driver=driver)
    cp.play_pause()
    time.sleep(2)
    cp.play_pause()
    time.sleep(2)
    cp.next()
    cp.next()
    time.sleep(2)
    cp.previous()
    time.sleep(2)
    cp.repeat()
    time.sleep(2)
    cp.like()
    time.sleep(2)

    while True:
        try:
            input()
        except KeyboardInterrupt:
            sys.exit()
