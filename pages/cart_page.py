from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_items_count(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    def remove_item(self, product_id):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, f"remove-{product_id}")))
        btn.click()
