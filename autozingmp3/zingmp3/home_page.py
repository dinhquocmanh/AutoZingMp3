from autozingmp3.browser.base_page import BasePage
import os 
import json

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login_to_account():
        pass 

    def get_informations():
        pass 

    def export_cookie(self):
        """
        Export cookie of the account and save in <id:username>_cookie.json
        """
        if not os.path.exists('cookies/'):
            os.mkdir('cookies')
        outputfile = f'default_cookie.json'
        self.log.info('Exporting cookie -> .json')
        #if 'coinlist.co' in self.driver.current_url:
        cookies = self.driver.get_cookies()
        with open('cookies/'+outputfile, 'w', newline='') as outputdata:
            json.dump(cookies, outputdata)
    
    def load_cookie(self):
        """
        Load cookie from input files
        """
        if not os.path.exists('cookies/'):
            self.log.error('Cookies folder not found!')
            return False
        inputfile = 'default_cookie.json'
        #if 'coinlist.co' in self.driver.current_url:
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
