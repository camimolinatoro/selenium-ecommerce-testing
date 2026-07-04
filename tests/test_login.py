import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "El login no llevó al inventario"

def test_login_fallido_password_incorrecta(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "password_incorrecta")

    error = login_page.get_error_message()
    assert error is not None, "Debería mostrar un mensaje de error"
    assert "Username and password do not match" in error