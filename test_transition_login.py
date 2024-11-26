from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

def logout(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)

def test_login_success():
    driver = webdriver.Edge()
    status_transition = []
    try:
        login(driver, "standard_user", "secret_sauce")
        status_transition.append("Logged In")
    finally:
        driver.quit()
    return status_transition

def test_login_logout():
    driver = webdriver.Edge()
    status_transition = []
    try:
        login(driver, "standard_user", "secret_sauce")
        status_transition.append("Logged In")
        logout(driver)
        status_transition.append("Logged Out")
    finally:
        driver.quit()
    return status_transition

def test_invalid_login():
    driver = webdriver.Edge()
    status_transition = []
    try:
        login(driver, "invalid_user", "invalid_password")
        status_transition.append("Login Out")
    finally:
        driver.quit()
    return status_transition

if __name__ == "__main__":
    driver = webdriver.Edge()
    print(test_login_success())
    print(test_login_logout())
    print(test_invalid_login())