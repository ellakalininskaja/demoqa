from components.components import WebElement
from pages.base_page import BasePage


class Modal_dialogs(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.btn1 = WebElement(driver, "menu-list > #item-0")