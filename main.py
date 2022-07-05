from autozingmp3.browser.driver_factory import WebDriverFactory, WebDriverConfigs
from autozingmp3.zingmp3.home_page import HomePage
import sys 
import time 

if __name__ == "__main__":

    configs = WebDriverConfigs()
    wdf = WebDriverFactory(configs=configs)
    driver = wdf.getWebDriverInstance()

    # Send a get request to the url
    driver.get('https://zingmp3.vn/')

    # home page auto
    homepage = HomePage(driver=driver)
    #time.sleep(60)
    homepage.load_cookie()

    while True:
        try:
            input()
        except KeyboardInterrupt:
            sys.exit()
