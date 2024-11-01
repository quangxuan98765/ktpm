from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def fill_form(driver, name, email, enquiry):
    driver.get("https://demo.opencart.com/index.php?route=information/contact")
    driver.find_element(By.ID, "input-name").clear()
    driver.find_element(By.ID, "input-name").send_keys(name)
    driver.find_element(By.ID, "input-email").clear()
    driver.find_element(By.ID, "input-email").send_keys(email)
    driver.find_element(By.ID, "input-enquiry").send_keys(enquiry)
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='form-contact']/div/button").click()
    time.sleep(3)

# Kiểm thử khi điền thông tin hợp lệ
def test_form_submission_success(driver):
    fill_form(driver, "Khoi", "123boyzzkhoi@gmail.com", "Hello store owner!")
    assert "Your enquiry has been successfully sent to the store owner!" in driver.page_source

# Kiểm thử khi bỏ trống các trường bắt buộc
def test_form_submission_fail(driver):
    fill_form(driver, "Khoi", "123boyzzkhoi@gmail.com", "Hello")
    assert "Enquiry must be between 10 and 3000 characters!" in driver.page_source

def test_form_submission_fail2(driver):
    fill_form(driver, "", "123boyzzkhoi@gmail.com", "Hello store owner!")
    assert "Name must be between 3 and 32 characters!" in driver.page_source

def test_form_submission_fail3(driver):
    fill_form(driver, "Khoi", "invalid email", "Hello store owner!")
    assert "E-Mail Address does not appear to be valid!" in driver.page_source

# cd opencart
# pytest -v Test_Form_Submission.py