import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    yield driver
    driver.quit()


def test_valid_login(setup):
    driver = setup
    driver.find_element(By.ID, "email").send_keys("valid_email")
    driver.find_element(By.ID, "pass").send_keys("valid_password")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    assert "Facebook" in driver.title


def test_invalid_password(setup):
    driver = setup
    driver.find_element(By.ID, "email").send_keys("valid_email")
    driver.find_element(By.ID, "pass").send_keys("wrong_password")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    error = driver.page_source
    assert "incorrect" in error.lower()


def test_empty_fields(setup):
    driver = setup
    driver.find_element(By.NAME, "login").click()
    time.sleep(2)

    assert "Facebook" in driver.title
