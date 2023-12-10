import pytest

from conftest import browser
from pages.Radio import Radio
from pages.demoqa import DemoQa


# @pytest.mark.skip
def test_decor_3(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ""


# @pytest.mark.skipif(True, reason="просто пропуск")
def test_decor_4(browser):
    radio_page = Radio(browser)

    radio_page.visit()
    radio_page.yes_radio_btn.click_force()
    assert radio_page.text_result.get_text() == "You have selected Yes"

    radio_page.impressive_radio_btn.click_force()
    assert radio_page.text_result.get_text() == "You have selected Impressive"

    assert "disabled" in radio_page.no_radio_btn.get_dom_attribute("class")
