"""
class WebDriverFactory:
    khởi tạo driver object từ các thông số config
    usage:
        wdf = WebDriverFactory(configs=configs)
        driver = wdf.getWebDriverInstance()

class WebDriverConfigs:
    chứa các config để truyền vào class trên
    vd: proxy, extensions, profile, window size,...
"""

from selenium import webdriver
from autozingmp3.log.custom_logger import CustomLogger

class WebDriverConfigs():
    def __init__(self):
        self.window_size = False
        self.window_position = False
        self.new_profile = False
        self.profile_dir = False
        self.proxy = False
        self.user_agents = False
        self.extensions = False
        self.headless = False


class WebDriverFactory():
    log = CustomLogger()
    def __init__(self, configs):
        self.config = configs

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        # options.add_argument("--incognito")
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument(
            "--disable-popup-blocking --disable-infobars --disable-notifications --disable-password-generation")
        options.add_argument('--disable-save-password-bubble')
        options.add_argument("--disable-crash-reporter")

        # adjustable options
        if self.config.window_size:
            options.add_argument("--window-size={}".format(self.config.window_size))
        if self.config.window_position:
            options.add_argument("--window-position={}".format(self.config.window_position))
        if self.config.proxy != False:
            options.add_argument('--proxy-server=socks5://{}'.format(self.config.proxy))
        if self.config.user_agents != False:
            options.add_argument("user-agent={}".format(self.config.user_agents))    
        if self.config.extensions != False:
            options.add_argument("--load-extension={}".format(self.config.extensions))

        self.driver = webdriver.Chrome(options=options)

        return self.driver