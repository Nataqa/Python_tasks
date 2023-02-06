import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_auth_ok(autorized):
    ''' Тест на проверку успешности авторизации в фикстуре и
        переходе на нужную страницу '''
    # Проверяем, что мы оказались на главной странице пользователя

    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


def test_show_my_pets(autorized):
    ''' Тест на проверку списка питомцев:
       1. Проверяем, что оказались на странице питомцев пользователя.
       2. Проверяем, что присутствуют все питомцы.  '''

    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    # Устанавливаем ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']")))
    pytest.driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    # Проверяем, что оказались на странице питомцев пользователя
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице
    # задаем неявное ожидание 5 сек
    pytest.driver.implicitly_wait(5)
    pets_number = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)


def test_checking_сards_pets(autorized):
   ''' Тест на проверку карточек питомцев:
   1. Проверяем, что у всех питомцев есть имя, возраст и порода.
   2. Проверяем, что хотя бы у половины питомцев есть фото.
   3. Проверяем, что у всех питомцев разные имена'''

   # получаем нужные элементы - фото, имя, порода, возраст
   # задаем неявное ожидание 5 сек
   pytest.driver.implicitly_wait(5)
   images = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/th/img')
   pytest.driver.implicitly_wait(5)
   names = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[1]')
   pytest.driver.implicitly_wait(5)
   breeds = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[2]')
   pytest.driver.implicitly_wait(5)
   ages = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[3]')

   images_count = 0
   list_names = []
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr')))
   pets_count = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

   for i in range(len(pets_count)):
       list_names.append(names[i].text) # сразу записываем имена живностей в список
       if images[i].get_attribute('src') != '':
           images_count += 1
       else:
           images_count += 0
       assert names[i].text != '' #проверяем, что имя не пустое
       assert breeds[i].text != '' #проверяем, что порода не пустая
       assert ages[i].text != '' #проверяем, что возраст не пустой
   # print(images_count)
   # проверка деления на 0
   if len(pets_count) == 0:
       print("Нет питомцев")
   else:
       assert images_count / len(pets_count) >= 0.5 #проверяем, что хотя бы у половины есть фото


   # Проверяем, что у всех питомцев разные имена.
   set_names = set(list_names) #получаем из списка множество с уникальными элементами
   assert len(set_names) == len(list_names)

def tests_duplicate_pets(autorized):
    ''' Тест на проверку дублирующихся питомцев.'''
    # Проверяем, что в списке нет повторяющихся питомцев
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pets_data = []
    for pet in all_pets:
        pets_data.append(pet.text)
    unique_pets = set(pets_data)
    assert len(pets_data) == len(unique_pets)

