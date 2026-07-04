import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_logout_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.logout()

    assert driver.current_url == "https://www.saucedemo.com/", "Debería regresar a la página de login"
