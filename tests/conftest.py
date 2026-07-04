import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordChangeDetection")
    options.add_argument("--disable-save-password-bubble")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports", exist_ok=True)
            screenshot_path = f"reports/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot guardado en: {screenshot_path}")
            print(f"URL al momento del fallo: {driver.current_url}")
