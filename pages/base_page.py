import logging
from components.components import WebElement

from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        # self.viewport = WebElement(driver, "head > meta")
        self.viewport = WebElement(driver, "//*[contains(@name, 'viewport')]", "xpath")

    def visit(self):
        return self.driver.get(self.base_url)

    # def find_element(self, locator):
    #    return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

# здесь храним методы для всех страниц
