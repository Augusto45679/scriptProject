import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ruta al módulo de selector
sys.path.append(os.path.join(os.path.dirname(__file__), 'selectors'))
from grid_selector import GridSelector

def is_logged_in(driver):
    try:
        login_btn = driver.find_elements(By.CSS_SELECTOR, '[data-testid="header-login-button"]')
        return len(login_btn) == 0
    except Exception:
        return False

def main():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Comenta esta línea si quieres ver el navegador
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0")

    try:
        # Iniciar el navegador
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        print("Abriendo página...")
        driver.get('https://key-drop.com/es/giveaways/list')

        # Espera hasta que los elementos estén presentes o imprime el HTML
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid^="giveaway-single-card"]'))
            )
            print("Página cargada correctamente.")
        except Exception as wait_error:
            print("No se encontraron elementos esperados en el tiempo definido.")
            print("HTML actual:")
            print(driver.page_source)
            driver.save_screenshot("error.png")
            driver.quit()
            return

        grid_selector = GridSelector(driver)
        items = grid_selector.get_items()
        print("Premios encontrados:", items)

        if items and items[0]:
            grid_selector.select_item(items[0])
            print(f"Seleccionado: {items[0]}")
        else:
            print("No se encontraron premios.")

        driver.quit()

    except Exception as e:
        print("Error general:", str(e))

if __name__ == "__main__":
    main()
