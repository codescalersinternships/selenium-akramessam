
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
  # Initialize the ChromeDriver instance with options
  options = webdriver.ChromeOptions()
  #options.add_extension('extension.crx')  # For Adding Extension
  driver = webdriver.Chrome(options=options)

  # Make its calls wait up to 30 seconds for elements to appear
  driver.implicitly_wait(30)


  # Return the WebDriver instance for the setup
  yield driver

  # Quit the WebDriver instance for the cleanup
  driver.quit()