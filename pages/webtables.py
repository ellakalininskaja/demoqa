from components.components import WebElement
from pages.base_page import BasePage


class Webtables(BasePage):
    def __getitem__(self, item):
        return getattr(self, item)

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)
        const_header_base = ("#app > div > div > div.row > div.col-12.mt-4.col-md-6 "
                             "> div.web-tables-wrapper > "
                             "div.ReactTable.-striped.-highlight > div.rt-table > "
                             "div.rt-thead.-header > div >")
        self.no_data = WebElement(driver, "div.rt-noData")
        self.btn_delete_row = WebElement(driver, "//*[contains(@title, 'Delete')]", "xpath")
        self.add_btn = WebElement(driver, "#addNewRecordButton")
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        self.age = WebElement(driver, "#age")
        self.salary = WebElement(driver, "#salary")
        self.department = WebElement(driver, "#department")
        self.submit_btn = WebElement(driver, "#submit")
        self.btn_edit_row = WebElement(driver, "//*[contains(@title, 'Edit')]", "xpath")
        self.table_row_first_name = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > "
                                                       "div.web-tables-wrapper > div.ReactTable.-striped.-highlight > "
                                                       "div.rt-table > div.rt-tbody > div:nth-child(1) > div > "
                                                       "div:nth-child(1)")
        self.table_col_header_sort_asc = WebElement(driver, "//*[contains(@class, 'rt-th rt-resizable-header -sort-asc "
                                                            "-cursor-pointer')]", "xpath")
        self.table_col_header_sort_desc = WebElement(driver, "//*[contains(@class, 'rt-th rt-resizable-header "
                                                             "-sort-desc -cursor-pointer')]", "xpath")
        self.table_col_header_first_name = WebElement(driver, f"{const_header_base} div:nth-child(1)")
        self.table_col_header_last_name = WebElement(driver, f"{const_header_base} div:nth-child(2)")
        self.table_col_header_email = WebElement(driver, f"{const_header_base} div:nth-child(3)")
        self.table_col_header_salary = WebElement(driver, f"{const_header_base} div:nth-child(4)")
        self.table_col_header_department = WebElement(driver, f"{const_header_base} div:nth-child(5)")
        self.table_col_header_action = WebElement(driver, f"{const_header_base} div:nth-child(6)")
