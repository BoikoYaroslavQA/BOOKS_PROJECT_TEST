import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager.Install())
    driver.maximize_window()
    yield driver
    driver.quit()
