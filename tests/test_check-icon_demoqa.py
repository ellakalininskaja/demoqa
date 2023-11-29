import time

from pages.demoqa import DemoQa
from conftest import browser


def test_check_icon(browser):
    demo_qa_page: DemoQa = DemoQa(browser)

    demo_qa_page.visit()
    # time.sleep(3)
    demo_qa_page.icon.click()
    # demo_qa_page.click_on_the_icon()
    assert demo_qa_page.equal_url()
    time.sleep(3)
    assert demo_qa_page.icon.exist()
