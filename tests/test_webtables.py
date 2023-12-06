import time

from conftest import browser
from pages.webtables import Webtables


def test_webtables(browser):
    page_tables = Webtables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(3)
    assert page_tables.no_data.exist()