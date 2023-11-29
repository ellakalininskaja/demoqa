import pytest
from selenium import webdriver


@pytest.fixture(scope="session") #декоратор
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
