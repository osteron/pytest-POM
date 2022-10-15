import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):
    @pytest.fixture(autouse=True)
    def func_fixture(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_exist()
        assert flag

    # Positive test
    def test_login_positive(self):
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = self.loginPage.get_title(TestData.AFTER_LOGIN_PAGE_TITLE)
        assert title in TestData.AFTER_LOGIN_PAGE_TITLE

    # Negative test
    def test_login_negative(self):
        self.loginPage.do_login("123@!a.com", "123@!a.com")
        error_flag = self.loginPage.is_error_exist()
        assert error_flag
