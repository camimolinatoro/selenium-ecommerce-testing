import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_campos_vacios_muestra_error(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.go_to_checkout()
    checkout_page.fill_info("", "", "")

    error = checkout_page.get_form_error()
    assert "First Name is required" in error

def test_cancelar_checkout_regresa_al_inventario(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.go_to_checkout()
    checkout_page.cancel()

    assert "cart" in driver.current_url, "Cancelar debería regresar al carrito"
