import time

import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.Smoke import Smoke
from Tests.test_base import BaseTest


class Test_Smoke(BaseTest):
    @pytest.fixture(autouse=True)
    def func_fixture(self):
        self.smokePage = Smoke(self.driver)

    # First smoke test
    def test_first_smoke(self):
        self.smokePage.products_click()
        assert TestData.HOME_SECURITY_URL in self.smokePage.get_url()
        self.smokePage.detailed_click()
        assert TestData.INTERNET_SECURITY_URL in self.smokePage.get_url()
        self.smokePage.buy_click()
        assert TestData.BASKET_URL in self.smokePage.get_url()
        self.smokePage.continue_click()
        assert TestData.ORDER_URL in self.smokePage.get_url()
        self.smokePage.send_customer_data("test@gmail.com", "Test", "Testov")
        self.smokePage.checkbox_and_submit_click()
        assert self.smokePage.is_payment_form_exist()
