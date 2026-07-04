import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_multiples_productos_al_carrito(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")

    assert inventory_page.get_cart_count() == "3"

def test_remover_producto_del_carrito(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_items_count() == 2

    cart_page.remove_item("sauce-labs-backpack")
    assert cart_page.get_items_count() == 1