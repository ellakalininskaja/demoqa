import time

from pages.text_box import TextBox
from conftest import browser


def test_box_form(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys("tester")
    text_box.current_address.send_keys("SPb")
    text_box.btn_submit.click_force()
    time.sleep(2)
    assert text_box.name_after_submit.get_text() == "Name:tester"
    assert text_box.current_address_after_submit.get_text() == "Current Address :SPb"


