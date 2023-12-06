from components.components import WebElement
from pages.base_page import BasePage


class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"

        super().__init__(driver, self.base_url)

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
