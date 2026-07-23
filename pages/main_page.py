from data.urls import MAIN_PAGE_URL
from locators.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open(self):
        self.open_url(MAIN_PAGE_URL)
        self.wait_for_visibility(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_overlays_gone()
        return self

    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def is_modal_displayed(self):
        return self.is_element_displayed(MainPageLocators.MODAL)

    def is_modal_closed(self):
        return not self.has_visible_elements(MainPageLocators.MODAL)

    def close_modal(self):
        buttons = self.find_elements(MainPageLocators.MODAL_CLOSE_BUTTON)
        visible = [button for button in buttons if button.is_displayed()]
        button = visible[-1] if visible else self.wait_for_visibility(MainPageLocators.MODAL_CLOSE_BUTTON)
        try:
            button.click()
        except Exception:
            self.driver.execute_script('arguments[0].click();', button)
        self.wait_for_invisibility(MainPageLocators.MODAL)

    def get_ingredient_counter(self, ingredient_element=None):
        if ingredient_element is None:
            ingredient_element = self.wait_for_visibility(MainPageLocators.BUN_INGREDIENT)
        counter = ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    def add_ingredient_to_order(self):
        ingredient = self.wait_for_visibility(MainPageLocators.BUN_INGREDIENT)
        basket = self.wait_for_visibility(MainPageLocators.CONSTRUCTOR_BASKET)
        self.scroll_to_element(ingredient)
        self.drag_and_drop(ingredient, basket)
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
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number(self):
        try:
            self.wait_for_invisibility(MainPageLocators.LOADING_OVERLAY)
        except Exception:
            pass
        number = self.wait_for_visibility(MainPageLocators.ORDER_NUMBER)
        self.wait.until(lambda _: number.text.strip() not in ('', '9999'))
        return number.text.strip()

    def is_constructor_opened(self):
        current_url = self.get_current_url().rstrip('/')
        return current_url.endswith('stellarburgers.education-services.ru') or self.get_current_url().endswith('/')

    def is_order_feed_opened(self):
        return self.url_contains('feed')
