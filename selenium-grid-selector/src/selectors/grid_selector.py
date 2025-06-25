from selenium.webdriver.common.by import By

class GridSelector:
    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        cards = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid^="giveaway-single-card"]')
        items = []
        for card in cards:
            try:
                name = card.find_element(By.CSS_SELECTOR, '[data-testid^="giveaway-single-card-prize-name"]').text
                price = card.find_element(By.CSS_SELECTOR, '[data-testid^="giveaway-single-card-price"]').text
                price_value = float(price.replace('$', '').replace(',', '').strip())
                items.append({"name": name, "price": price_value, "element": card})
            except Exception:
                continue
        return items

    def get_cheapest_item(self):
        items = self.get_items()
        if not items:
            return None
        return min(items, key=lambda item: item['price'])

    def click_join_button(self, card_element):
        try:
            join_button = card_element.find_element(By.CSS_SELECTOR, '[data-testid^="giveaway-single-card-join-button"]')
            join_button.click()
        except Exception as e:
            raise RuntimeError("No se pudo hacer clic en el botón de unir: " + str(e))
