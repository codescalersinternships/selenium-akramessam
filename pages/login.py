from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# just commenting 

class LoginPage:

    # URL

    base_url = 'https://www.saucedemo.com/'

    # Locators
    
    username_input = (By.ID, 'user-name')
    password_input = (By.ID, 'password')
    submit = (By.ID,'login-button')
    
    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.base_url)

    def login(self, usr,pswd):
        self.enter_username(usr)
        self.enter_password(pswd)
        self.submit_form()
     

    def enter_username(self,usr):
        user_input = self.browser.find_element(*self.username_input)
        user_input.send_keys(usr)
        
    def enter_password(self,pswd):
        pass_input = self.browser.find_element(*self.password_input)
        pass_input.send_keys(pswd)
        
    def submit_form(self):
        submit = self.browser.find_element(*self.submit)
        submit.send_keys(Keys.ENTER)
     