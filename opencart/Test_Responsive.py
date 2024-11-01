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
    yield driver  # Trả về driver cho các test case
    driver.quit()  # Đóng trình duyệt sau khi test case hoàn thành

# Kiểm tra trên kích thước màn hình di động (Ví dụ: 375x667 cho iPhone X)
def test_mobile_responsive(driver):
    driver.find_element(By.XPATH, "//*[@id='logo']/a").click()
    time.sleep(2)
    # Thiết lập kích thước cửa sổ cho giao diện di động
    driver.set_window_size(375, 667)
    
    # Kiểm tra xem biểu tượng menu dành riêng cho di động có hiển thị không
    try:
        menu_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mobile-menu-icon"))
        )
        assert menu_icon.is_displayed(), "Biểu tượng menu di động phải hiển thị trên giao diện di động."
        print("Kiểm tra giao diện di động thành công.")
    except Exception as e:
        print("Kiểm tra giao diện di động thất bại:", e)

# Kiểm tra trên kích thước màn hình máy tính bảng (Ví dụ: 768x1024 cho iPad)
def test_tablet_responsive(driver):
    driver.find_element(By.XPATH, "//*[@id='logo']/a").click()
    time.sleep(2)
    # Thiết lập kích thước cửa sổ cho giao diện máy tính bảng
    driver.set_window_size(768, 1024)
    
    # Kiểm tra xem thanh điều hướng dành riêng cho máy tính bảng có hiển thị không
    try:
        navigation_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tablet-navbar"))
        )
        assert navigation_bar.is_displayed(), "Thanh điều hướng của máy tính bảng phải hiển thị trên giao diện máy tính bảng."
        print("Kiểm tra giao diện máy tính bảng thành công.")
    except Exception as e:
        print("Kiểm tra giao diện máy tính bảng thất bại:", e)

# Kiểm tra trên kích thước màn hình máy tính để bàn (Ví dụ: 1920x1080)
def test_desktop_responsive(driver):
    driver.find_element(By.XPATH, "//*[@id='logo']/a").click()
    time.sleep(2)
    # Thiết lập kích thước cửa sổ cho giao diện máy tính để bàn
    driver.set_window_size(1920, 1080)
    
    # Kiểm tra xem thanh điều hướng đầy đủ dành riêng cho máy tính để bàn có hiển thị không
    try:
        full_navbar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "desktop-navbar"))
        )
        assert full_navbar.is_displayed(), "Thanh điều hướng máy tính để bàn phải hiển thị trên giao diện máy tính để bàn."
        print("Kiểm tra giao diện máy tính để bàn thành công.")
    except Exception as e:
        print("Kiểm tra giao diện máy tính để bàn thất bại:", e)
