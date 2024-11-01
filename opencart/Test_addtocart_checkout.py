import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver  # Trả về driver cho các test case
    driver.quit()  # Đóng trình duyệt sau khi test case hoàn thành

def test_add_to_cart(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones & PDAs"))).click()
    time.sleep(3)
    # Chọn sản phẩm và thêm vào giỏ hàng
    driver.execute_script("window.scrollBy(0, 200);") # Cuộn 200px
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='product-list']/div[2]/div/div[2]/div/h4/a").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 200);") # Cuộn 200px
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "button-cart"))).click()
    time.sleep(2)
    assert "Success" in driver.page_source, "Product was not added to the cart successfully."
    
def test_add_to_cart_multiple(driver):
    test_add_to_cart(driver)
    time.sleep(2)
    # Chọn sản phẩm và thêm vào giỏ hàng
    driver.execute_script("window.scrollBy(0, 200);") # Cuộn 200px
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='product-list']/div[2]/div/div[2]/div/h4/a").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 200);") # Cuộn 200px
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "button-cart"))).click()
    time.sleep(2)

    # Quay lại trang danh sách sản phẩm và thêm cùng sản phẩm lần thứ hai
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='product-list']/div[2]/div/div[2]/div/h4/a").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "button-cart"))).click()
    time.sleep(2)
    
    driver.execute_script("window.scrollBy(0, -200);") # Cuộn lên 200px
    # Xác nhận sản phẩm đã được thêm hai lần (hoặc kiểm tra số lượng tăng lên)
    time.sleep(2)
    # Tìm nút giỏ hàng và lấy văn bản từ phần tử đó
    cart_button_text = driver.find_element(By.CSS_SELECTOR, "button.btn.dropdown-toggle").text
    time.sleep(1)

    # Kiểm tra xem văn bản có chứa "2 item(s)" không
    assert "2 item(s)" in cart_button_text, "Product was not added to the cart twice."

def test_remove_from_cart(driver):
    # test_add_to_cart(driver)
    # Xóa sản phẩm khỏi giỏ hàng
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, -200);") # Cuộn lên 200px
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='header-cart']/div/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/table/tbody/tr/td[5]/form/button").click()
    time.sleep(2)
    assert "Success: You have removed an item from your shopping cart!" in driver.page_source, "Product was not removed from the cart successfully."

def test_checkout_empty_cart(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[5]/a").click()
    time.sleep(2)
    assert "Your shopping cart is empty!" in driver.page_source, "Checkout allowed with empty cart, which is incorrect."

def test_checkout(driver):
    test_add_to_cart(driver)
    # Đi đến giỏ hàng và đặt hàng
    driver.execute_script("window.scrollBy(0, -200);") # Cuộn lên 200px
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='top']/div/div[2]/ul/li[4]/a"))).click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div[3]/div[2]/a"))).click()
    time.sleep(2)
    # Chọn địa chỉ
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)
    select_address = driver.find_element(By.ID, "input-shipping-address")
    select_object_1 = Select(select_address)
    select_object_1.select_by_value("1043")
    # driver.find_element(By.ID, "input-shipping-new").click()
    time.sleep(2)
    # Nhập thông tin cần thiết để đặt hàng
    # driver.find_element(By.ID, "input-shipping-firstname").send_keys("John")
    # driver.find_element(By.ID, "input-shipping-lastname").send_keys("Doe")
    # driver.find_element(By.ID, "input-shipping-address-1").send_keys("123 Street")
    # driver.find_element(By.ID, "input-shipping-city").send_keys("City")
    # time.sleep(2)
    # select_element = driver.find_element(By.ID, "input-shipping-country")
    # select_object = Select(select_element)
    # # Chọn giá trị bằng value
    # select_object.select_by_value("230")
    # time.sleep(2)

    # select_element_1 = driver.find_element(By.ID, "input-shipping-zone")
    # select_object_1 = Select(select_element_1)
    # select_object_1.select_by_value("3780")
    
    # Chọn phương thức thanh toán và giao hàng
    driver.find_element(By.XPATH, "//*[@id='alert']/div/button").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-shipping-methods").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    time.sleep(1)
    driver.find_element(By.ID, "button-shipping-method").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-payment-methods").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    time.sleep(1)
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='checkout-payment']/div").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-confirm").click()
    time.sleep(2)
    assert "Your order has been placed!" in driver.page_source, "Order was not placed successfully."
