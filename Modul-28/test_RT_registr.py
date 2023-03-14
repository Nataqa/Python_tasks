from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import consts
import pytest

# TC_RT-004
# Проверка загрузки страницы регистрации
def test_loading_registration(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.page_reg))).click()
    elem = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.page_title))).text
    assert elem == 'Регистрация'

# TC_RT-015
# Проверка поля "Имя" со страницы регистрации на корректность вводимых данных
def test_register_firstName(testing):
    firstNameInput = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.firstName_locator))
    firstNameInput.click()

    for i in range(len(consts.registerFormKeysFirstName)):
        login_input = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.firstName_locator))
        login_input.clear()
        login_input.send_keys(consts.registerFormKeysFirstName[i])
        # time.sleep(2)
        WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.lastName_locator)).click()

        if i < len(consts.registerFormKeysFirstName) - 1:
            if i >= 1:
                pass
            else:
                error = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.registerErrors_locator)).text

        assert error == consts.registerErrorsName
        # time.sleep(2)
        login_input.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        login_input.clear()
        # time.sleep(1)


# TC_RT-016
# Проверка поля "Фамилия" со страницы регистрации на корректность вводимых данных
def test_register_lastName(testing):
    firstNameInput = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.lastName_locator))
    firstNameInput.click()

    for i in range(len(consts.registerFormKeysLastName)):
        login_input = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.lastName_locator))
        login_input.clear()
        login_input.send_keys(consts.registerFormKeysLastName[i])
        # time.sleep(2)
        WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.firstName_locator)).click()

        if i < len(consts.registerFormKeysLastName) - 1:
            if i >= 1:
                pass
            else:
                error = WebDriverWait(pytest.driver, 10).until(
                    EC.presence_of_element_located(consts.registerErrors_locator)).text

        assert error == consts.registerErrorsName
        # time.sleep(2)
        login_input.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        login_input.clear()
        # time.sleep(1)

# TC_RT-017
# Проверка поля "Email или Мобильный телефон" со страницы регистрации
# на корректность вводимых данных

def test_register_email_and_phone(testing):

    actionChain = ActionChains(pytest.driver)
    addressNameInput = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address')))

    values = consts.registerFormKeysLogin
    actionChain.click(addressNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        pytest.driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(
                        consts.registerErrors_locator)).text
            assert error == consts.registerErrorsAddress
            time.sleep(1)
            actionChain.double_click(addressNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            time.sleep(1)

# # TC_RT-018
# # Проверка поля "Пароль" со страницы регистрации
# # на корректность вводимых данных
def test_register_password(testing):
    actionChain = ActionChains(pytest.driver)

    passNameInput = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.pass_locator_reg))
    time.sleep(2)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               consts.password_visibility))).click()

    values = consts.registerFormPassword
    actionChain.click(passNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        pytest.driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(
                        (consts.registerErrors_locator))).text

            time.sleep(1)
            actionChain.double_click(passNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            time.sleep(1)
            assert error == consts.registerErrorsPass


# TC_RT-019
# Проверка поля "Подтверждение пароля" со страницы регистрации
# на корректность вводимых данных
def test_register_passwordConfirm(testing):
    actionChain = ActionChains(pytest.driver)

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.password_visibility))).click()
    # 'section#page-right > div > div > div > form > div:nth-of-type(4) > div > div > div:nth-of-type(2) > svg'
    time.sleep(1)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('test&Tests123').perform()
    time.sleep(1)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    time.sleep(1)

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('test&Tests987').perform()
    time.sleep(1)
    pytest.driver.find_element(By.NAME, 'register').click()

    error = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Пароли не совпадают')]"))).text
    assert error == 'Пароли не совпадают'
    # скролл, для наглядности, в реальных тестах можно не делать
    pytest.driver.execute_script("return arguments[0].scrollIntoView();", pytest.driver.find_element(By.CSS_SELECTOR, consts.link_user_locator1))

    time.sleep(2)

# TC_RT-021
# Проверка на орфографические ошибки текстов плейсхолдеров полей
# на странице Регистрации
def test_spellchecking_register(testing):
    placeholderInput = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, consts.placeholderInputsId)))

    for i in range(len(placeholderInput)):
        assert placeholderInput[i].text == consts.placeholderInputs_registr[i]

