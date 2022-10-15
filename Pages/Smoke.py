import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class Smoke(BasePage):

    FOR_HOME = (By.XPATH, '//*[text()="Для дома"][@class="AccesibilityButton_button__2QjPj MenuItem_title__3qHBO"]')
    PRODUCTS = (By.XPATH, '//*[text()="Продукты"]')
    DETAILED_BUTTON = (By.XPATH, '//a[@href="/internet-security"][@data-at-selector="link-button"]')
    BUY_BUTTON = (By.XPATH, '//*[text()="Купить"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@value="ПРОДОЛЖИТЬ"]')
    EMAIL = (By.XPATH, '//*[@type="email"]')
    NAME = (By.XPATH, '//*[@placeholder="Введите имя"]')
    LAST_NAME = (By.XPATH, '//*[@placeholder="Введите фамилию"]')
    CHECKBOX = (By.NAME, "order_type[personalDataConfirmed]")
    SUBMIT_BUTTON = (By.XPATH, '//*[@value="Перейти к оплате"]')
    PAYMENT_FORM = (By.CLASS_NAME, 'payment_block')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    def products_click(self):
        self.do_click(self.FOR_HOME)
        self.do_click(self.PRODUCTS)

    def detailed_click(self):
        self.do_click(self.DETAILED_BUTTON)

    def buy_click(self):
        self.do_click(self.BUY_BUTTON)

    def continue_click(self):
        self.do_click(self.CONTINUE_BUTTON)

    def send_customer_data(self, email, name, lastname):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.LAST_NAME, lastname)

    def checkbox_and_submit_click(self):
        # при стандартном вызове do_click не находит чекбокс
        # пришлось сделать "костыль" do_click_without_wait
        self.do_click_without_wait(By.NAME, "order_type[personalDataConfirmed]")
        self.do_click(self.SUBMIT_BUTTON)

    def is_url_exist(self):
        self.get_url()

    def is_payment_form_exist(self):
        return self.is_visible(self.PAYMENT_FORM)
