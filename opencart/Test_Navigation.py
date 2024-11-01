from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navigation(driver):
    time.sleep(5)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.(...), ""))).click(): Đợi cho đến khi link có thể nhấp được
    # Điều hướng đến danh mục Desktops
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Desktops"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/div/a"))).click()
    time.sleep(3)
    assert "Desktops" in driver.title

    # Điều hướng đến danh mục Laptops & Notebooks
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops & Notebooks"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='narbar-menu']/ul/li[2]/div/a"))).click()
    time.sleep(13)
    assert "Laptops & Notebooks" in driver.title

    # Điều hướng đến danh mục Components
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Components"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='narbar-menu']/ul/li[3]/div/a"))).click()
    time.sleep(3)
    assert "Components" in driver.title

    # Điều hướng đến danh mục Tablets
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tablets"))).click()
    time.sleep(3)
    assert "Tablets" in driver.title

    # Điều hướng đến danh mục Software
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Software"))).click()
    time.sleep(3)
    assert "Software" in driver.title

    # Điều hướng đến danh mục Phones & PDAs
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones & PDAs"))).click()
    time.sleep(3)
    assert "Phones & PDAs" in driver.title

    # Điều hướng đến danh mục Cameras
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Cameras"))).click()
    time.sleep(3)
    assert "Cameras" in driver.title

    # Điều hướng đến danh mục Contact Us
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Cuộn trang để đảm bảo phần tử nằm trong vùng hiển thị
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact Us"))).click()
    time.sleep(3)
    assert "Contact Us" in driver.title

    # Điều hướng đến danh mục My Account
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/footer/div/div/div[4]/ul/li[1]/a"))).click()
    time.sleep(3)
    assert "My Account" in driver.title

