import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, "https://www.google.pl/?hl=pl&pli=1" )
    page.open()
    time.sleep(5)
