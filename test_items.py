import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


def test_guest_should_see_languages(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    button.click()
    assert EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary"))

