from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import lxml.html
import pytest

pf = PetFriends()

###########################################################################################################
#КЛЮЧ-АВТОРИЗАЦИИ (ПОЗИТИВНЫЙ)
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что api-запрос ключа авторизации возвращает
     код статуса 200 и в результате содержится ключевое слово key"""

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        assert status == 200
        assert 'key' in result
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"

############################################################################################################
#СПИСОК ВСЕХ ПИТОМЦЕВ (ПОЗИТИВНЫЙ)
def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос списка всех питомцев возвращает не пустой список.
        Доступное значение параметра filter - 'my_pets' либо '' """

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result, = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Сверяем полученные данные с нашими ожиданиями при успешной авторизации
        status, result = pf.get_list_of_pets(auth_key, filter)
        assert status == 200
        assert len(result['pets']) > 0
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
############################################################################################################
#СПИСОК МОИХ ПИТОМЦЕВ (ПОЗИТИВНЫЙ)
def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос списка моих питомцев возвращает не пустой список.
        Доступное значение параметра filter - 'my_pets' либо '' """

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Сверяем полученные данные с нашими ожиданиями при успешной авторизации
        status, result = pf.get_list_of_pets(auth_key, filter)
        assert status == 200
        assert len(result['pets']) > 0
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
############################################################################################################
#СПИСОК ПИТОМЦЕВ (НЕГАТИВНЫЙ ПО ФИЛЬТРУ)
def test_get_invalid_list_pets_with_valid_key(filter='mypets'):
    """ Проверяем что запрос списка моих питомцев не возвращает статус код ответа 200
        если значение параметра filter - задано не корректно """

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Сверяем полученные данные с нашими ожиданиями при успешной авторизации
        status, result = pf.get_list_of_pets(auth_key, filter)
        assert status != 200
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
# ############################################################################################################
#СПИСОК ВСЕХ ПИТОМЦЕВ (НЕГАТИВНЫЙ ПО КЛЮЧУ)
def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что запрос списка всех питомцев с не корректным значением
         почты возвращает ошибку.
        Доступное значение параметра filter - 'my_pets' либо '' """

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(invalid_email, valid_password)
    status, result = pf.get_api_key(invalid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Сверяем полученные данные с нашими ожиданиями при успешной авторизации
        status, result = pf.get_list_of_pets(auth_key, filter)
        assert status == 200
        assert len(result['pets']) > 0
    else:
        assert status != 200
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
############################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА С ФОТО (ПОЗИТИВНЫЙ)
def test_add_new_pet_with_correct_data(name='Карамелька', animal_type='котик', age='5', pet_photo='images/cat3.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Добавляем питомца, если авторизация прошла успешно
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == age
        assert result['pet_photo'] != ''
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
###########################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА БЕЗ ФОТО (ПОЗИТИВНЫЙ)
def test_add_new_pet_with_valid_data_without_photo(name='Карамелька', animal_type='Дворовая', age='5'):
    """Проверяем что можно добавить питомца с корректными данными без фото"""
    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] == ''
###########################################################################################################
#УДАЛЕНИЕ ПИТОМЦА (ПОЗИТИВНЫЙ)
def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Котофей", "кот", "2", "images/cat2.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()
###########################################################################################################
#ОБНОВЛЕНИЕ ИНФОРМАЦИИ О ПИТОМЦЕ (ПОЗИТИВНЫЙ)
def test_successful_update_self_pet_info(name='Мур-мурзик', animal_type='Котик', age='3'):
    """Проверяем возможность обновления информации о питомце"""

    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить имя, тип и возраст питомца с id=0
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и параметры питомца соответствуют заданному
        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == age
    else:
        # если список питомцев пустой, то выбрасываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

###########################################################################################################
#ДОБАВЛЕНИЕ ФОТО ПИТОМЦА (ПОЗИТИВНЫЙ)
def test_add_photo_pet_with_valid_data(pet_photo='images/cat5.jpg'):
    """Проверяем что можно добавить фото питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото питомцу с id=0 из списка
    if len(my_pets['pets']) > 0:
        # Берём id первого питомца из списка
        pet_id = my_pets['pets'][0]['id']
    # Добавляем фото питомца
    status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    # проверяем, что поле фото в ответе не пустое
    assert result['pet_photo'] != ''

###########################################################################################################
#КЛЮЧ-АВТОРИЗАЦИИ (НЕГАТИВНЫЙ ПО ПОЧТЕ)
def test_get_api_key_for_invalid_user_email(email=invalid_email, password=valid_password):
    """ Проверяем что api-запрос ключа авторизации возвращает
     код статуса 403 и ошибку в случае авторизации с несуществующей почтой"""

    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    status, result = pf.get_api_key(email, password)
    # Забираем текст ошибки из запроса
    txt_err = lxml.html.document_fromstring(result)
    error = txt_err.xpath('/html/body/p/text()')

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert error[0] == "This user wasn\'t found in database"
###########################################################################################################
#КЛЮЧ-АВТОРИЗАЦИИ (НЕГАТИВНЫЙ ПО ПАРОЛЮ)
def test_get_api_key_for_invalid_user_password(email=valid_email, password=invalid_password):
    """ Проверяем что api-запрос ключа авторизации возвращает
     код статуса 403 и ошибку в случае авторизации с неверным паролем"""

    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    status, result = pf.get_api_key(email, password)
    # Забираем текст ошибки из запроса
    txt_err = lxml.html.document_fromstring(result)
    error = txt_err.xpath('/html/body/p/text()')

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert error[0] == "This user wasn\'t found in database"
###########################################################################################################
#КЛЮЧ-АВТОРИЗАЦИИ (НЕГАТИВНЫЙ: ПУСТЫЕ ПОЧТА И ПАРОЛЬ)
def test_get_api_key_for_empty_email_password(email="", password=""):
    """ Проверяем что api-запрос ключа авторизации возвращает
     код статуса 403 и ошибку в случае авторизации с не заполненными полями почты и пароля"""

    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    status, result = pf.get_api_key(email, password)
    # Забираем текст ошибки из запроса
    txt_err = lxml.html.document_fromstring(result)
    error = txt_err.xpath('/html/body/p/text()')

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert error[0] == "This user wasn\'t found in database"
###########################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА С ФОТО (НЕГАТИВНЫЙ: ВОЗРАСТ НЕ ЧИСЛО)
def test_add_new_pet_with_incorrect_data_age(name='Кошка', animal_type='Кошка', age='Кошка', pet_photo='images/cat4.jpg'):
    """Проверяем можно ли добавить питомца с некорректными данными (возраст не число)"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Добавляем питомца, если авторизация прошла успешно
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        rez = True if status != 200 else False
        if rez:
            assert status != 200
        else:
            assert (status == 500) or (status == 400) or (status == 403)
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"

###########################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА C ФОТО (НЕГАТИВНЫЙ: ВОЗРАСТ ОТРИЦАТЕЛЬНОЕ ЧИСЛО)
def test_add_new_pet_with_incorrect_age(name='Кошатинка', animal_type='Кот', age='-5', pet_photo='images/cat4.jpg'):
    """Проверяем можно ли добавить питомца с некорректными данными (возраст не число)"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Добавляем питомца, если авторизация прошла успешно
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        rez = True if status != 200 else False
        if rez:
            assert status != 200
        else:
            assert status == 400
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
###########################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА C ФОТО (НЕГАТИВНЫЙ: ВСЕ ПУСТЫЕ ПОЛЯ КРОМЕ ФОТО)
def test_add_new_pet_with_incorrect_data_empty(name='', animal_type='', age='', pet_photo='images/cat4.jpg'):
    """Проверяем можно ли добавить питомца с пустыми полями, но с фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ авторизации и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_api_key(valid_email, valid_password)
    # Проверяем, что авторизация прошла успешно
    rez = True if (status == 200) and ('key' in result) else False
    if rez:
        # Добавляем питомца, если авторизация прошла успешно
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        rez = True if status != 200 else False
        if rez:
            assert status != 200
        else:
            assert status == 400
    else:
        txt_err = lxml.html.document_fromstring(result)
        error = txt_err.xpath('/html/body/p/text()')
        assert error[0] == "This user wasn\'t found in database"
###########################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА БЕЗ ФОТО (НЕГАТИВНЫЙ: ВОЗРАСТ НЕ ЧИСЛО)
def test_add_new_pet_with_invalid_data_without_photo(name='Карамелька', animal_type='Дворовая', age='Кошка'):
    """Проверяем можно ли добавить питомца с не корректными данными без фото"""
    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200

############################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА БЕЗ ФОТО (НЕГАТИВНЫЙ: ВОЗРАСТ ОТРИЦАТЕЛЬНОЕ ЧИСЛО)
def test_add_new_pet_with_invalid_age_without_photo(name='Карамелька', animal_type='Дворовая', age='-5'):
    """Проверяем можно ли добавить питомца с не корректными данными без фото"""
    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
#############################################################################################################
#ДОБАВЛЕНИЕ ПИТОМЦА БЕЗ ФОТО (НЕГАТИВНЫЙ: ПУСТЫЕ ПОЛЯ)
def test_add_new_pet_with_empty_data_without_photo(name='', animal_type='', age=''):
    """Проверяем можно ли добавить питомца с не пустыми полями без фото"""
    # Запрашиваем ключ авторизации и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200


