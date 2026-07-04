import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_flujo_completo_de_compra(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Agregar producto al carrito
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1", "El contador del carrito debería mostrar 1"

    # Ir al carrito y checkout
    inventory_page.go_to_cart()
    checkout_page = CheckoutPage(driver)
    checkout_page.go_to_checkout()
    checkout_page.fill_info("Camila", "Molina", "12345")
    checkout_page.finish_order()

    # Verificar confirmación
    mensaje = checkout_page.get_confirmation_message()
    assert "Thank you for your order" in mensaje, f"Mensaje inesperado: {mensaje}"