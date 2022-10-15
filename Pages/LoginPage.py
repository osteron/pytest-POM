import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    EMAIL = (By.XPATH, '//*[@type="email"][@class="u-inputField__control"]')
    PASSWORD = (By.XPATH, '//*[@type="password"][@class="u-inputField__control u-inputField__control-icon"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@omniturectaname="Sign in"]')
    SIGN_UP = (By.XPATH, '//*[@data-at-selector="welcomeSignInTab"][@data-at-active="true"]')
    LOGIN_ERROR_TEXT_LOCATOR = (By.XPATH, "//*[@data-at-error]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_PAGE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_exist(self):
        return self.is_visible(self.SIGN_UP)

    def do_login(self, login, password):
        self.do_send_keys(self.EMAIL, login)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def is_error_exist(self):
        return self.is_visible(self.LOGIN_ERROR_TEXT_LOCATOR)
