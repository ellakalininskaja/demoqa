from selenium.webdriver import Keys

from pages.slider import Slider
from conftest import browser


def test_slider(browser):
    slider_page = Slider(browser)
    slider_page.visit()

    assert slider_page.slider.exist()
    assert slider_page.slider_input.exist()

    while not slider_page.slider_input.get_dom_attribute("value") == "50": #повторяй след.дей-ие пока не будет 50
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_input.get_dom_attribute("value") == "50"