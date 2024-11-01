import pytest
import time
from Test_login_logout import login

# tự động chạy một lần khi bắt đầu phiên kiểm thử (theo scope="session")
# Pytest tự động phát hiện các fixtures trong conftest.py và chia sẻ chúng giữa các file test trong cùng thư mục.
@pytest.fixture(scope="session", autouse=True)
def logged_in_driver(driver):
    # Đăng nhập một lần trong suốt phiên kiểm thử
    login(driver, "123boyzzkhoi@gmail.com", "123abc")
    time.sleep(1)