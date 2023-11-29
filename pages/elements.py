from components.components import WebElement
from pages.base_page import BasePage


class Elements(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.elements_empty_page_text = WebElement(driver, "div.col-12.mt-4.col-md-6")

