import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from settings import valid_email, valid_password
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--kiosk')
    # chrome_options.add_argument('headless') # чтобы не было видно этапы загрузки страниц
    chrome_options.add_argument("--window-size=800,600")
    return chrome_options

@pytest.fixture(scope="session", autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('D:\\QAP\\chromedriver\\chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   yield
   
   pytest.driver.quit()

@pytest.fixture(scope="session")
def autorized():
   # Вводим email
   # Устанавливаем явное ожидание   
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys(valid_email)
   # Устанавливаем явное ожидание  
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


