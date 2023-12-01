from conftest import browser
from pages.demoqa import DemoQa
from pages.elements import Elements
from tests_hw.utils.text_equals import text_equals

const_footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
const_elements_empty_page_text = 'Please select an item from left to start practice.'


def test_check_text_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    assert text_equals(demo_qa_page.footer.get_text(), const_footer_text)


def test_check_text_elements(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    assert text_equals(el_page.elements_empty_page_text.get_text(), const_elements_empty_page_text)

def test_page_elements(browser):
    el_page = Elements(browser)
    el_page.visit()

    assert el_page.text_elements.get_text() == "Elements"

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()

