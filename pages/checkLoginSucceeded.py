
class Actual:
  INVENTORY_PAGE = 'https://www.saucedemo.com/inventory.html'


  def __init__(self, browser):
    self.browser = browser

  def check(self)->bool:
    curl = self.browser.current_url
    if curl == self.INVENTORY_PAGE:
        return True
    else:
       return False
    