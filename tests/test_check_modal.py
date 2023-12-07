from pages.modal_dialogs import Modal_dialogs
from conftest import browser


def test_check_modal(browser):
    modal_page = Modal_dialogs(browser)
    modal_page.visit()

    assert modal_page.btn_open_small_modal.exist()
    modal_page.btn_open_small_modal.click()
    assert modal_page.modal_window.exist()
    assert modal_page.small_modal_title.get_text() == "Small Modal"
    modal_page.btn_close_small_modal.click()
    assert not modal_page.modal_window.exist()

    assert modal_page.btn_open_large_modal.exist()
    modal_page.btn_open_large_modal.click()
    assert modal_page.modal_window.exist()
    assert modal_page.large_modal_title.get_text() == "Large Modal"
    modal_page.btn_close_large_modal.click()
    assert not modal_page.modal_window.exist()

