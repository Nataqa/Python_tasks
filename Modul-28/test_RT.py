from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
import time
import consts

# TC_RT-001
# Проверка загрузки страницы авторизации
def test_loading_authorization(testing):
    elem = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.page_title))).text
    assert elem == 'Авторизация'

# TC_RT-002
# Проверка автоматической смены плейсхолдера при выборе различных способов авторизации
# на странице Авторизации, проверка на орфографические ошибки текстов плейсхолдера
def test_correct_change_placeholder(testing):

    for i in range(len(consts.tabButtonsId)):
        pytest.driver.find_element(By.ID, consts.tabButtonsId[i]).click()
        WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.ID, consts.tabButtonsId[i])))

        placeholderInput = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.placeholderInputsId))).text
        assert placeholderInput == consts.placeholderInputsValue[i]

# TC_RT-003
# Проверка автоматического изменения вида авторизации при вводе -
# телефона/почты/лицевого счета/логина, на странице Авторизации
def test_correct_change_input(testing):
    pytest.driver.find_element(By.ID, consts.tabButtonsId[0]).click()
    tabButtons = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'rt-tab')))

    placeholderInput = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.placeholderInputsId))).text
    assert placeholderInput == consts.placeValue[0]

    for i in range(len(tabButtons)):
        login_input = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.login_locator))
        login_input.clear()
        login_input.send_keys(consts.sendKeys[i])
        time.sleep(2)
        pass_input = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(consts.pass_locator))
        pass_input.click()
        activeTabButton = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.rt-tabs .{consts.activeTab}')))
        assert activeTabButton.text == consts.tabTitlesAuth[i]
        time.sleep(2)
        login_input.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        login_input.clear()
        time.sleep(1)


# TC_RT-005
# Проверка перехода по ссылке "Забыл пароль"
def test_click_forgotPassword(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.tab_forgotPassword))).click()
    elem = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.page_forgotPassword))).text
    assert elem == 'Восстановление пароля'

# TC_RT-006
# Проверка обновление капчи на странице восстановления пароля
def test_refresh_captcha(testing):
    time.sleep(2)  # Для наглядности
    realCaptcha = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.image_captcha_locator))).get_attribute('src')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.tab_refresh_capcha))).click()
    time.sleep(2)  # Для наглядности - в реальности тестирования закоментировать
    newCaptcha = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.image_captcha_locator))).get_attribute('src')
    assert realCaptcha != newCaptcha

# TC_RT-007
# Проверка функциональности кнопки "Вернуться назад", на странице восстановления пароля
def test_back_to_authoriz(testing):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, consts.tab_return_back))).click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, consts.page_title))).text == 'Авторизация'
    time.sleep(2)  # Для наглядности



# TC_RT-008
# Проверка загрузки страницы Пользовательского соглашения
# через ссылку под кнопкой "Войти"
def test_open_agreement1(testing):
    originalWindow = pytest.driver.current_window_handle

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.link_user_locator1))).click()
    WebDriverWait(pytest.driver, 5).until(EC.number_of_windows_to_be(2))
    # делаем активной вкладку с пользовательским соглашением
    for window_handle in pytest.driver.window_handles:
        if window_handle != originalWindow:
            pytest.driver.switch_to.window(window_handle)
            break
    window_title = pytest.driver.execute_script("return window.document.title")
    time.sleep(3)
    assert window_title == 'User agreement'
    # закрываем вкладку с пользовательским соглашением
    pytest.driver.close()

