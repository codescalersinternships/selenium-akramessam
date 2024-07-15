from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# just commenting 

class LoginPage:

    # URL

    URL = 'https://www.saucedemo.com/'

    # Locators
    
    username_input = (By.ID, 'user-name')
    password_input = (By.ID, 'password')
    submit = (By.ID,'login-button')
    
    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def login(self, usr,pswd):
        user_input = self.browser.find_element(*self.username_input)
        user_input.send_keys(usr)
        pass_input = self.browser.find_element(*self.password_input)
        pass_input.send_keys(pswd)
        submit = self.browser.find_element(*self.submit)
        submit.send_keys(Keys.ENTER)
     
