import sys
import os
import json
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from axe_core_python.selenium import Axe
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def run_axe_scan(driver, page_name):
    axe = Axe()
    results = axe.run(driver)

    os.makedirs("reports/accessibility", exist_ok=True)
    with open(f"reports/accessibility/{page_name}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    violations = results["violations"]
    critical = [v for v in violations if v["impact"] == "critical"]

    print(f"\n[{page_name}] Total violations: {len(violations)} | Critical: {len(critical)}")
    for v in violations:
        print(f"  - [{v['impact']}] {v['id']}: {v['description']}")

    return violations, critical


def test_accessibility_login_page(driver):
    login_page = LoginPage(driver)
    login_page.load()

    violations, critical = run_axe_scan(driver, "login_page")
    assert len(critical) == 0, f"Found {len(critical)} CRITICAL accessibility issues on login page"


@pytest.mark.xfail(reason="Known issue: SauceDemo's sort dropdown is missing an accessible name (select-name rule). Tracked, not yet fixed by the site.")
def test_accessibility_inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

    violations, critical = run_axe_scan(driver, "inventory_page")
    assert len(critical) == 0, f"Found {len(critical)} CRITICAL accessibility issues on inventory page"
