import time

from pages.alerts import Alerts
from conftest import browser


def test_check_alert(browser):
    page_alerts = Alerts(browser)

    page_alerts.visit()
    assert page_alerts.timer_alert_button.exist()
    page_alerts.timer_alert_button.click()
    time.sleep(6)
    page_alerts.alert().accept()
    assert not page_alerts.alert()
