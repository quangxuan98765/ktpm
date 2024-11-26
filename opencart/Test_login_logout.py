import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
import time

@pytest.fixture(scope="session")
def driver():
    # driver_path = r"D:\DHSG\ktpm\TestSelenium\msedgedriver.exe"
    # service = EdgeService(executable_path=driver_path)
    # driver = webdriver.Edge(service=service)  # Khởi tạo trình duyệt Edge
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver  # Trả về driver cho các test case
    driver.quit()  # Đóng trình duyệt sau khi test case hoàn thành

# Người dùng đăng nhập 
def login(driver, email, password):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(30)
    driver.find_element(By.ID, "input-email").send_keys(email)
    driver.find_element(By.ID, "input-password").send_keys(password)
    time.sleep(5) # Đợi trang tải để có thể nhấp
    # driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and text()='Login']").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and text()='Login']"))).click()
    while not "My Account" in driver.title:
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and text()='Login']"))).click()
        time.sleep(1)
    time.sleep(7)

# Người dùng đăng nhập thành công
def test_login_success(driver):
    assert "My Account" in driver.title

# Người dùng đăng nhập không thành công
def test_login_fail(driver):
    test_logout(driver)
    login(driver, "123boyzzkhoi@gmail.com", "wrongpassword")
    time.sleep(5)
    assert "Warning: No match for E-Mail Address and/or Password." in driver.page_source # Kiểm tra hiện thông báo lỗi

# Người dùng đăng xuất
def test_logout(driver):
    login(driver, "123boyzzkhoi@gmail.com", "123abc")
    time.sleep(5)

    # Logout
    # Đợi đầu link có thể nhấp
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div").click()
    time.sleep(2)  # Đợi trang tải
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()
    time.sleep(2)  # Đợi trang tải
    
    assert "Account Logout" in driver.title

# cd opencart
# pytest -v Test_login_logout.py
