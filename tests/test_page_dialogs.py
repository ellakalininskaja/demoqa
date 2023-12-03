from conftest import browser
from pages.demoqa import DemoQa
from pages.modal_dialogs import Modal_dialogs

const_main_page_title = 'DEMOQA'


def test_find_modal_elements(browser):
    modal = Modal_dialogs(browser)
    modal.visit()

    assert modal.accordion_menu_alerts_btns.check_count_elements(count_items=5)
    modal.all_btns.find_elements()


def test_navigation_modal(browser):
    modal = Modal_dialogs(browser)
    demo_qa_page: DemoQa = DemoQa(browser)

    modal.visit()
    modal.refresh()

    browser.refresh()

    modal.main_page_icon.click()

    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert demo_qa_page.equal_url()
    assert browser.title == const_main_page_title
    browser.set_window_size(1000, 1000)
