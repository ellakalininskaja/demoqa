import time

from conftest import browser
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys("text")
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

#необходимо сделать принудительный клик
#click_force() - кастомный метод для принудительного клика
#execute_script() - метод АПИ селениума позволяющий добавлять свой js код
#execute_script( скрипт , *аргументы )
#Синхронно выполняет JavaScript в текущем окне.
#В классе WebElement, после метода click() добавьте метод click_force()
#принимает только self
#в теле метода обратитесь к драйверу, от него вызовите метод execute_script()
#в execute_script первый аргументом передайте JS код
#"arguments[0].click();"
#вторым вызовите find_element()

