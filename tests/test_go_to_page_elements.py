from pages.demoqa import DemoQa
from pages.elements import Elements
from conftest import browser


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)

    demo_qa_page.visit()  # посетить сайт
    assert demo_qa_page.equal_url()  # проверить урл на соответствие
    demo_qa_page.btn_elements.click()
    assert el_page.equal_url()
