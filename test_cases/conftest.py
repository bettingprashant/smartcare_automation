import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture()
def setup():
    options = Options()
    # Make sure headless is not enabled
    # options.add_argument('--headless')  # REMOVE or COMMENT THIS LINE

    # Optional: Disable GPU (for some systems)
    # options.add_argument('--disable-gpu')

    service = Service()  # Let it use default chromedriver in PATH
    driver = webdriver.Chrome(service=service, options=options)

    # Maximize the browser window to ensure visibility
    driver.maximize_window()

    yield driver

    # Pause to visually inspect browser before it closes (during debugging)
    time.sleep(5)

    driver.quit()












# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver