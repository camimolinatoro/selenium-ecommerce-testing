import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_usuario_bloqueado(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_message()
    assert error is not None
    assert "locked out" in error.lower()

def test_login_campos_vacios(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "")

    error = login_page.get_error_message()
    assert error is not None
    assert "Username is required" in error