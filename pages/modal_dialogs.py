from components.components import WebElement
from pages.base_page import BasePage


class Modal_dialogs(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.accordion_menu_alerts_btns = WebElement(driver, "div.element-group:nth-child(3) > div > ul > li")
        self.all_btns = WebElement(driver, "#app > button")
        self.main_page_icon = WebElement(driver, "#app > header > a")