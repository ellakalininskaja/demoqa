from components.components import WebElement
from pages.base_page import BasePage


class Modal_dialogs(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.accordion_menu_alerts_btns = WebElement(driver, "div.element-group:nth-child(3) > div > ul > li")
        self.all_btns = WebElement(driver, "#app > button")
        self.main_page_icon = WebElement(driver, "#app > header > a")
        self.btn_open_small_modal = WebElement(driver, "#showSmallModal")
        self.btn_open_large_modal = WebElement(driver, "#showLargeModal")
        self.btn_close_small_modal = WebElement(driver, "#closeSmallModal")
        self.btn_close_large_modal = WebElement(driver, "#closeLargeModal")
        self.small_modal_title = WebElement(driver, "#example-modal-sizes-title-sm")
        self.large_modal_title = WebElement(driver, "#example-modal-sizes-title-lg")
        self.modal_window = WebElement(driver, "body > div.fade.modal.show > div")