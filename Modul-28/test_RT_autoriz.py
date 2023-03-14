from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import consts
import pytest

# TC_RT-014
# Проверка авторизации пользователя c некорректным паролем
def test_authoriz_phoneNumber(testing):
    # проверяем, что находимся на страницы авторизации
    elem = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.page_title))).text
    assert elem == 'Авторизация'

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((consts.login_locator))).click()
    login_input = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.login_locator))
    login_input.click()
    login_input.clear()
    login_input.send_keys(consts.sendKeys[0])
    time.sleep(2)
    pass_input = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.pass_locator))
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys(consts.sendKeys[3])
    time.sleep(2)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((consts.tab_authoriz))).click()

    time.sleep(2)
    error = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((consts.authorizErrorID))).text
    assert error == consts.authorizError

#TC_RT-020
# Проверка на орфографические ошибки текста плейсхолдера поля "Пароль"
# на странице Авторизации
def test_spellchecking_password(testing):
    placeholderInput = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, consts.placeholderInputsId)))

    assert placeholderInput[1].text == consts.placeholderInputs_pass

