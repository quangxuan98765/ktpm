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

def test_order_total_increase(driver):
    # Thêm sản phẩm vào giỏ hàng trên trang OpenCart
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

    # Lấy tổng đơn hàng ban đầu
    driver.execute_script("window.open('https://demo.opencart.com/admin/');")
    # Lấy tất cả các tab
    tabs = driver.window_handles
    # Chuyển sang tab mới (tab cuối cùng trong danh sách)
    driver.switch_to.window(tabs[-1])
    time.sleep(10)
    # vào trang admin và lấy tổng đơn hàng hiện tại
    # driver.find_element(By.XPATH, "//*[@id='form-login']/div[3]/button").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form-login']/div[3]/button"))).click()
    time.sleep(5)
    initial_order_count = int(driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/div[2]/h2").text)

    # Quay lại trang open cart hoàn tất đơn hàng
    driver.switch_to.window(tabs[0])
    time.sleep(2)
    driver.find_element(By.ID, "button-confirm").click()
    
    # Đợi thông báo đặt hàng thành công
    time.sleep(2)
    
    # Quay lại trang admin và refresh để kiểm tra tổng đơn hàng
    driver.switch_to.window(tabs[-1])
    time.sleep(2)

    # Làm mới (refresh) trang admin
    driver.refresh()
    time.sleep(2)
    
    # Lấy tổng đơn hàng mới
    new_order_count = int(driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/div[2]/h2").text)
    time.sleep(2)
    # Kiểm tra xem tổng đơn hàng có tăng lên không
    assert new_order_count == initial_order_count + 1, f"Tổng đơn hàng không tăng như mong đợi: {initial_order_count} -> {new_order_count}"
    
    # # Bước 4: Kiểm tra ID đơn hàng
    # driver.get("https://demo.opencart.com/admin/index.php?route=sale/order")
    # # Lấy ID đơn hàng mới nhất (có thể cần điều chỉnh XPath dựa vào cấu trúc bảng)
    # order_id = driver.find_element(By.XPATH, "//*[@id='order-list']/tbody/tr[1]/td[1]").text
    
    # # Kiểm tra ID đơn hàng trong lịch sử đặt hàng (nếu có)
    # driver.get("https://demo.opencart.com/index.php?route=account/order")
    # # Kiểm tra xem ID đơn hàng có xuất hiện trong danh sách đơn hàng không
    # assert order_id in driver.page_source, f"ID đơn hàng không được tìm thấy trong lịch sử đơn hàng: {order_id}"

