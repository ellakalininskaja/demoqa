import time

import pytest

from conftest import browser
from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


def test_seo(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert browser.title == "DEMOQA"


# запускает тест столько раз сколько указано параметров
# "pages" - название аргумента в функции
@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == "DEMOQA"
