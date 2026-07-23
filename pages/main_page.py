from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.urls import MAIN_PAGE_URL
from locators.locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(MAIN_PAGE_URL)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))
        self._wait_overlays_gone()
        return self

    def _wait_overlays_gone(self):
        overlays = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
        for overlay in overlays:
            if overlay.is_displayed():
                self.wait.until(EC.invisibility_of_element(overlay))

    def _click(self, locator):
        self._wait_overlays_gone()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', element)

    def click_personal_account(self):
        self._click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        self._click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self._click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self._click(MainPageLocators.INGREDIENT)

    def is_modal_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(MainPageLocators.MODAL)).is_displayed()

    def close_modal(self):
        buttons = self.driver.find_elements(*MainPageLocators.MODAL_CLOSE_BUTTON)
        visible = [button for button in buttons if button.is_displayed()]
        button = visible[-1] if visible else self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        )
        try:
            button.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', button)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL))

    def get_ingredient_counter(self, ingredient_element):
        counter = ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    def add_ingredient_to_order(self):
        ingredient = self.wait.until(EC.visibility_of_element_located(MainPageLocators.BUN_INGREDIENT))
        basket = self.wait.until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BASKET))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', ingredient)

        ActionChains(self.driver).click_and_hold(ingredient).pause(0.5).move_to_element(basket).pause(0.5).release().perform()
        if self._get_counter_safe(ingredient) == 0:
            ActionChains(self.driver).drag_and_drop(ingredient, basket).perform()
        if self._get_counter_safe(ingredient) == 0:
            self.driver.execute_script(
                """
                const src = arguments[0];
                const tgt = arguments[1];
                const srcRect = src.getBoundingClientRect();
                const tgtRect = tgt.getBoundingClientRect();
                const fire = (type, el, clientX, clientY) => {
                    el.dispatchEvent(new MouseEvent(type, {
                        bubbles: true, cancelable: true, view: window,
                        clientX, clientY, buttons: 1
                    }));
                };
                const sx = srcRect.x + srcRect.width / 2;
                const sy = srcRect.y + srcRect.height / 2;
                const tx = tgtRect.x + tgtRect.width / 2;
                const ty = tgtRect.y + tgtRect.height / 2;
                fire('mousedown', src, sx, sy);
                fire('mousemove', src, sx, sy);
                fire('mousemove', tgt, tx, ty);
                fire('mouseup', tgt, tx, ty);
                const dt = new DataTransfer();
                src.dispatchEvent(new DragEvent('dragstart', {bubbles:true, cancelable:true, dataTransfer:dt}));
                tgt.dispatchEvent(new DragEvent('dragenter', {bubbles:true, cancelable:true, dataTransfer:dt}));
                tgt.dispatchEvent(new DragEvent('dragover', {bubbles:true, cancelable:true, dataTransfer:dt}));
                tgt.dispatchEvent(new DragEvent('drop', {bubbles:true, cancelable:true, dataTransfer:dt}));
                src.dispatchEvent(new DragEvent('dragend', {bubbles:true, cancelable:true, dataTransfer:dt}));
                """,
                ingredient,
                basket
            )
        self.wait.until(lambda _: self._get_counter_safe(ingredient) > 0)
        return ingredient

    def _get_counter_safe(self, ingredient_element):
        try:
            return int(ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)
        except Exception:
            return 0

    def click_place_order(self):
        self._click(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(MainPageLocators.LOADING_OVERLAY))
        except Exception:
            pass
        number = self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER))
        self.wait.until(lambda _: number.text.strip() not in ('', '9999'))
        return number.text.strip()

    def current_url_contains(self, path):
        self.wait.until(EC.url_contains(path))
        return path in self.driver.current_url
