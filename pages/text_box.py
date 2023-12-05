from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)
        self.name = WebElement(driver, "#userName")
        self.current_address = WebElement(driver, "#currentAddress")
        self.btn_submit = WebElement(driver, "#submit")
        self.current_address_after_submit = WebElement(driver, "#currentAddress.mb-1")
        self.name_after_submit = WebElement(driver, "#name")



