from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import consts
import pytest

# TC_RT-001
# Проверка загрузки страницы авторизации
def test_loading_authorization(testing):
    elem = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.page_title))).text
    assert elem == 'Авторизация'

# TK-009 Проверка перехода по ссылке авторизации через социальную сеть Vk
def test_try_auth_with_vk(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.page_vk))).click()
    assert pytest.driver.current_url.__contains__('oauth.vk.com')
    # Переходим обратно на страницу авторизации
    pytest.driver.get(consts.baseUrl)

# TK-010 Проверка перехода по ссылке авторизации через социальную сеть Ok
def test_try_auth_with_ok(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.page_ok))).click()
    assert pytest.driver.current_url.__contains__('connect.ok.ru')
    # Переходим обратно на страницу авторизации
    pytest.driver.get(consts.baseUrl)

# TK-011 Проверка перехода по ссылке авторизации через социальную сеть Mail.ru
def test_try_auth_with_mail(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.page_mail))).click()
    assert pytest.driver.current_url.__contains__('connect.mail.ru')
    # Переходим обратно на страницу авторизации
    pytest.driver.get(consts.baseUrl)

# TK-012 Проверка перехода по ссылке авторизации через социальную сеть Google
def test_try_auth_with_google(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.page_google))).click()
    assert pytest.driver.current_url.__contains__('accounts.google.com')
    # Переходим обратно на страницу авторизации
    pytest.driver.get(consts.baseUrl)

# TK-013 Проверка перехода по ссылке авторизации через социальную сеть Yandex
@pytest.mark.xfail
def test_try_auth_with_ya(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.page_ya))).click()
    assert pytest.driver.current_url.__contains__('oauth.yandex.ru')
    # Переходим обратно на страницу авторизации
    pytest.driver.get(consts.baseUrl)


