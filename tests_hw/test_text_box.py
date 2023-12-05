import time

from pages.text_box import TextBox
from conftest import browser


def text_box_form(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys("tester")
    text_box.current_address.send_keys("Москва")
    time.sleep(2)
