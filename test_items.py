import pytest
import time
from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(7)
    button = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, 'Кнопки нет'

if __name__ == "__main__":
    pytest.main()