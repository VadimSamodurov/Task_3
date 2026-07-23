from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный')]")
    INGREDIENT = (By.CSS_SELECTOR, "a[href*='/ingredient/']")
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@href,'/ingredient/') and contains(.,'булка')]")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__num']")
    CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket__list']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal_opened']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'text_type_digits-large')] | //p[contains(@class,'text_type_digits-large')] | //*[contains(@class,'Modal_modal__title') and contains(@class,'text_type_digits-large')]")
    LOADING_OVERLAY = (By.XPATH, "//img[@alt='loading animation']")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")


class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div[class*='input__icon']")
    ACTIVE_PASSWORD_FIELD = (By.CSS_SELECTOR, "div[class*='input_status_active']")


class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class OrderHistoryPageLocators:
    ORDER_NUMBER = (By.XPATH, "//p[starts-with(text(),'#')]")


class FeedPageLocators:
    ORDER_LINK = (By.CSS_SELECTOR, "a[href*='/feed/']")
    MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal_opened']")
    TOTAL_COMPLETED = (By.CSS_SELECTOR, "[class*='OrderFeed_number']")
    TOTAL_COMPLETED_TODAY = (By.XPATH, "(//p[contains(@class,'OrderFeed_number')])[2]")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::ul[1]/li")
    ORDER_NUMBER_IN_FEED = (By.XPATH, "//a[contains(@href,'/feed/')]//p[starts-with(text(),'#')]")
