
from pages.login import LoginPage
from pages.actual import Actual
import pytest

# USERNAME = 'standard_user'
# PASS = 'secret_sauce'

@pytest.mark.parametrize('usr,pswd', [('',''),('standard_user','secret_sauce'),('problem_user',''),('visual_user','secret_sauce')])
def test_basic_login(browser,usr,pswd):

    login_page = LoginPage(browser)    
    login_page.load()
    login_page.login(usr,pswd)
    
    actual = Actual(browser)

    assert actual.check() == True
  