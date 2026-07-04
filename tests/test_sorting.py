import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_ordenar_productos_precio_menor_a_mayor(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.sort_by("lohi")

    precios = inventory_page.get_product_prices()
    assert precios == sorted(precios), "Los precios deberían estar ordenados de menor a mayor"