from conftest import browser
from components.components import WebElement
from pages.webtables import Webtables

const_class_asc = "rt-th rt-resizable-header -sort-asc -cursor-pointer"
const_class_desc = "rt-th rt-resizable-header -sort-desc -cursor-pointer"
arr_table_headers_name = ["table_col_header_first_name", "table_col_header_last_name", "table_col_header_email",
                          "table_col_header_salary", "table_col_header_department", "table_col_header_action"]


def sort_checker(page_tables, page_tables_header_element: WebElement):
    assert page_tables_header_element.exist()
    page_tables_header_element.click()
    assert page_tables.table_col_header_sort_asc.exist()
    assert page_tables.table_col_header_sort_asc.get_dom_attribute('class') == const_class_asc
    page_tables_header_element.click()
    assert page_tables.table_col_header_sort_desc.exist()
    assert page_tables.table_col_header_sort_desc.get_dom_attribute('class') == const_class_desc


def test_sort(browser):
    page_tables = Webtables(browser)
    page_tables.visit()

    for elem in arr_table_headers_name:
        print(elem)
        sort_checker(page_tables, page_tables[elem])
