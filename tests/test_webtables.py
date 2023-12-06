import time

from conftest import browser
from pages.webtables import Webtables

const_first_name_text = 'tester222222'


def test_webtables(browser):
    page_tables = Webtables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    assert page_tables.no_data.exist()

    page_tables.add_btn.click()
    page_tables.first_name.send_keys('tester')
    page_tables.last_name.send_keys('testerovich')
    page_tables.user_email.send_keys('test@ttt.tt')
    page_tables.age.send_keys('30')
    page_tables.salary.send_keys('1111')
    page_tables.department.send_keys('department2222')
    page_tables.submit_btn.click()
    assert page_tables.btn_edit_row.exist()
    page_tables.btn_edit_row.click()
    page_tables.first_name.clear()
    page_tables.first_name.send_keys(const_first_name_text)
    page_tables.submit_btn.click()
    assert page_tables.table_row_first_name.get_text() == const_first_name_text
    page_tables.btn_delete_row.click()
    assert not page_tables.btn_delete_row.exist()