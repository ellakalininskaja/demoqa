import pytest
from selenium import webdriver


@pytest.fixture(scope="session") #декоратор для указания фикстуры
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()
