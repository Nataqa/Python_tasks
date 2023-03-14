from selenium import webdriver
import consts
import pytest

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--kiosk')
    # chrome_options.add_argument('headless') # чтобы не было видно этапы загрузки страниц
    chrome_options.add_argument("--window-size=800,600")

    return chrome_options

@pytest.fixture(scope="session", autouse=True)
def testing():
    # options = webdriver.ChromeOptions()
    pytest.driver = webdriver.Chrome('D:\\QAP\\chromedriver\\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get(consts.baseUrl)
    yield

    pytest.driver.quit()