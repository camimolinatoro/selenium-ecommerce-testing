from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def add_product_to_cart(self, product_id):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, f"add-to-cart-{product_id}")))
        btn.click()

    def remove_product_from_cart(self, product_id):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, f"remove-{product_id}")))
        btn.click()

    def get_cart_count(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        except:
            return "0"

    def wait_for_cart_count(self, expected):
        self.wait.until(lambda d: self.get_cart_count() == expected)
        return self.get_cart_count()

    def go_to_cart(self):
        link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        link.click()
        self.wait.until(EC.url_contains("cart.html"))

    def sort_by(self, option_value):
        select = Select(self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))))
        select.select_by_value(option_value)

    def get_product_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(e.text.replace("$", "")) for e in elements]

    def logout(self):
        menu_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_btn.click()
        logout_link = self.wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        self.wait.until(EC.presence_of_element_located((By.ID, "login-button")))
