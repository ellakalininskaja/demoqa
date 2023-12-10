from components.components import WebElement
from pages.base_page import BasePage


class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        super().__init__(driver, self.base_url)

        self.yes_radio_btn = WebElement(driver, "#yesRadio")
        self.impressive_radio_btn = WebElement(driver, "#impressiveRadio")
        self.text_result = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p")
        self.no_radio_btn = WebElement(driver, "#noRadio")