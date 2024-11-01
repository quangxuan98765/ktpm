import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    try:
        yield driver  # Trả về driver cho các test case
    finally:
        driver.quit()  # Đóng trình duyệt sau khi test case hoàn thành

def test_search(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search"))).send_keys("MacBook")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='search']/button").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    assert "MacBook" in driver.page_source, "Search failed"

def test_search_empty(driver):
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search"))).send_keys(" ")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='search']/button").click()
    time.sleep(2)
    assert "There is no product that matches the search criteria." in driver.page_source, "Search failed"

def test_search_invalid(driver):
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search"))).send_keys("123456")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='search']/button").click()
    time.sleep(2)
    assert "There is no product that matches the search criteria." in driver.page_source, "Search failed"