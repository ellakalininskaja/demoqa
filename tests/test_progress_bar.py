import time

from pages.progress_bar import ProgressBar
from conftest import browser


def test_progress_bar(browser):
    progress_bar_page = ProgressBar(browser)
    progress_bar_page.visit()
    time.sleep(2)

    assert progress_bar_page.start_stop_btn.exist()
    progress_bar_page.start_stop_btn.click()

    while True:
        if progress_bar_page.progress_bar.get_dom_attribute("aria-valuenow") == "51":
            progress_bar_page.start_stop_btn.click()
            break