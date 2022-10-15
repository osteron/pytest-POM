import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    request.cls.driver = web_driver
    request.cls.driver.maximize_window()
    yield
    web_driver.close()
