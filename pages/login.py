from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:

    # URL

    URL = 'https://www.saucedemo.com/'

    # Locators
    
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT = (By.ID,'login-button')
    
    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def login(self, usr,pswd):
        user_input = self.browser.find_element(*self.USERNAME_INPUT)
        user_input.send_keys(usr)
        pass_input = self.browser.find_element(*self.PASSWORD_INPUT)
        pass_input.send_keys(pswd)
        submit = self.browser.find_element(*self.SUBMIT)
        submit.send_keys(Keys.ENTER)
        # search_input.send_keys(phrase + Keys.RETURN)

