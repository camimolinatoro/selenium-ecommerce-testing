from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        btn.click()
        self.wait.until(EC.url_contains("checkout-step-one"))

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        continue_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_btn.click()

    def get_form_error(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        ).text

    def cancel(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "cancel")))
        btn.click()

    def finish_order(self):
        self.wait.until(EC.url_contains("checkout-step-two"))
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        btn.click()
        self.wait.until(EC.url_contains("checkout-complete"))

    def get_confirmation_message(self):
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        return element.text
