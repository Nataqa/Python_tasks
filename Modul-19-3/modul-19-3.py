import requests
import json

########## ПРОВЕРКА get-запросов со сваггера v2  ###########
####################################################################################################
# # проверка списка животных по статусам
# # status = 'available'
# # res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
# #                     headers = {'accept': 'application/json'})
# res_get1 = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus",
#                    params={'status': 'available'}, headers={'accept': 'application/json'})
# res_get2 = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus",
#                    params={'status': 'sold'}, headers={'accept': 'application/json'})
# res_get3 = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus",
#                    params={'status': 'pending'}, headers={'accept': 'application/json'})
#
# print('Статус ответа от сервера на GET-запрос выдачи списка питомцев со статусом available: ', res_get1.status_code)
# print("Карточка запроса:")
# print(res_get1.json())
# print('_____________________________________________________________________________________')
# print('Статус ответа от сервера на GET-запрос выдачи списка питомцев со статусом sold: ', res_get2.status_code)
# print("Карточка запроса:")
# print(res_get2.json())
# print('_____________________________________________________________________________________')
# print('Статус ответа от сервера на GET-запрос выдачи списка питомцев со статусом pending: ', res_get3.status_code)
# print("Карточка запроса:")
# print(res_get3.json())
# print('_____________________________________________________________________________________')

####################################################################################################

# # поиск животных по id
# # "id": 9, 155
# petId = 2222
# res_get4 = requests.get(f"https://petstore.swagger.io/v2/pet/{petId}",
#                    headers={'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос поиск питомцев по id: ', res_get4.status_code)
# print("Карточка запроса:")
# print(res_get4.json())

####################################################################################################

# # количество имеющихся статус-кодов
# res_get5 = requests.get(f"https://petstore.swagger.io/v2/store/inventory",
#                     headers = {'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос количества имеющихся статус-кодов: ', res_get5.status_code)
# print("Карточка запроса:")
# print(res_get5.json())

####################################################################################################

# # логин пользователя
# res_get6 = requests.get(f"https://petstore.swagger.io/v2/user/login",
#                         params={'username ': '1', 'password': '1'},
#                     headers={'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос логин пользователя: ', res_get6.status_code)
# print("Карточка запроса:")
# print(res_get6.json())

####################################################################################################

# # логаут пользователя
# res_get7 = requests.get(f"https://petstore.swagger.io/v2/user/logout",
#                         headers={'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос логаут пользователя: ', res_get7.status_code)
# print("Карточка запроса:")
# print(res_get7.json())

####################################################################################################

# # поиск покупки по id (5, 6, 7)
# ordId = 6
# res_get8 = requests.get(f"https://petstore.swagger.io/v2/order/{ordId}",
#                    headers={'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос поиск покупки по id: ', res_get8.status_code)
# print("Карточка запроса:")
# print(res_get8.json())

####################################################################################################

# # # поиск пользователя по имени
# userName = "1"
# res_get9 = requests.get(f"https://petstore.swagger.io/v2/user/{userName}",
#                    headers={'accept': 'application/json'})
# print('Статус ответа от сервера на GET-запрос поиск пользователя по имени: ', res_get9.status_code)
# print("Карточка запроса:")
# print(res_get9.json())

####################################################################################################
########## ПРОВЕРКА post-запросов со сваггера v2  ###########
####################################################################################################

# # добавление питомца
# info = {
# "id": 2222,
# "category": {"id": 2,"name": "Cat"},
# "name": "Qwerty",
# "photoUrls": ["string"],
# "tags": [{"id": 0,"name": "string"}],
# "status": "available"
# }
# res_post_addNewPet = requests.post(f"https://petstore.swagger.io/v2/pet",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info, ensure_ascii=False))
# print(f"Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}")
# try:
#     rez = res_post_addNewPet.json()
#     print(f"ID number добавленного питомца = {rez['id']}")
#     print(f"Имя добавленного питомца = {rez['name']}")
# except:
#     rez = res_post_addNewPet.text()
#     print("Карточка питомца:")
#     print(res_post_addNewPet.text())

####################################################################################################
# # обновление карточки питомца
#
# petId = 2222
# headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
# info = {
# "name": "Qwerty",
# "status": "available"
# }
# res_post_RedactPet = requests.post(f"https://petstore.swagger.io/v2/pet/{petId}",
#                                   headers=headers, data = info)
#
# print('Статус ответа от сервера на POST запрос изменение данных питомца: ', res_post_RedactPet.status_code)
# print("Карточка запроса:")
# print(res_post_RedactPet.json())

####################################################################################################

# # добавление заказа на покупку питомца
# info_status = {
#   "id": 3,
#   "petId": 2223,
#   "quantity": 0,
#   "shipDate": "2022-12-18T11:50:56.550Z",
#   "status": "placed",
#   "complete": True
# }
# res_post_addOrderPet = requests.post(f"https://petstore.swagger.io/v2/store/order",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info_status, ensure_ascii=False))
#
# print(f"Статус ответа от сервера на POST запрос добавление заказа: {res_post_addOrderPet.status_code}")
# try:
#     rez = res_post_addOrderPet.json()
#     print("Карточка заказа:")
#     print(res_post_addOrderPet.json())
#     print(f"ID номер заказа = {rez['id']}")
#     print(f"ID покупаемого питомца = {rez['petId']}")
# except:
#     rez = res_post_addOrderPet.text()
#     print("Карточка заказа:")
#     print(res_post_addOrderPet.text())

####################################################################################################

#создание списка данных пользователей
# info_users = [
#     {
#     "id": 111,
#     "username": "21",
#     "firstName": "31",
#     "lastName": "41",
#     "email": "51",
#     "password": "61",
#     "phone": "71",
#     "userStatus": 0
#   },
# {
#     "id": 1111,
#     "username": "211",
#     "firstName": "311",
#     "lastName": "411",
#     "email": "511",
#     "password": "611",
#     "phone": "711",
#     "userStatus": 0
#   },
#     ]
#
# res_post_UserArray = requests.post(f"https://petstore.swagger.io/v2/user/createWithArray",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info_users, ensure_ascii=False))
# print(f"Статус ответа от сервера на POST запрос добавления данных пользователя: {res_post_UserArray.status_code}")
# try:
#     rez = res_post_UserArray.json()
#     print("Карточки пользователя:")
#     print(res_post_UserArray.json())
# except:
#     rez = res_post_UserArray.text()
#     print("Карточки пользователя:")
#     print(res_post_UserArray.text())

####################################################################################################

# #создание списка данных пользователя
# info_users = [
#     {
#     "id": 444,
#     "username": "24",
#     "firstName": "34",
#     "lastName": "44",
#     "email": "54",
#     "password": "64",
#     "phone": "74",
#     "userStatus": 0
#   },
# {
#     "id": 4444,
#     "username": "244",
#     "firstName": "344",
#     "lastName": "444",
#     "email": "544",
#     "password": "644",
#     "phone": "744",
#     "userStatus": 0
#   },
#     ]
# res_post_UserList = requests.post(f"https://petstore.swagger.io/v2/user/createWithList",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info_users, ensure_ascii=False))
# print(f"Статус ответа от сервера на POST запрос добавления данных пользователя: {res_post_UserList.status_code}")
# try:
#     rez = res_post_UserList.json()
#     print("Карточки пользователя:")
#     print(res_post_UserList.json())
# except:
#     rez = res_post_UserList.text()
#     print("Карточки пользователя:")
#     print(res_post_UserList.text())

####################################################################################################

# #создание  пользователя
# info_user = {
#     "id": 333,
#     "username": "23",
#     "firstName": "33",
#     "lastName": "43",
#     "email": "53",
#     "password": "63",
#     "phone": "73",
#     "userStatus": 0
#   }
# res_post_User = requests.post(f"https://petstore.swagger.io/v2/user",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info_user, ensure_ascii=False))
# print(f"Статус ответа от сервера на POST запрос добавления пользователя: {res_post_User.status_code}")
# try:
#     rez = res_post_User.json()
#     print("Карточка пользователя:")
#     print(res_post_User.json())
# except:
#     rez = res_post_User.text()
#     print("Карточка пользователя:")
#     print(res_post_User.text())

####################################################################################################
########## ПРОВЕРКА put-запросов со сваггера v2  ###########
####################################################################################################

# # редактирование питомца
# info = {
# "id": 2223,
# "category": {"id": 2,"name": "Cat"},
# "name": "Qwerty",
# "photoUrls": ["string"],
# "tags": [{"id": 0,"name": "string"}],
# "status": "available"
# }
# res_put_redactPet = requests.put(f"https://petstore.swagger.io/v2/pet",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info, ensure_ascii=False))
# print(f"Статус ответа от сервера на PUT-запрос редактирование питомца: {res_put_redactPet.status_code}")
# try:
#     rez = res_put_redactPet.json()
#     print(f"ID номер отредактированного питомца = {rez['id']}")
#     print(f"Имя отредактированного питомца = {rez['name']}")
# except:
#     rez = res_put_redactPet.text()
#     print("Карточка питомца:")
#     print(res_put_redactPet.text())

######################################################################################################

# #редактирование  пользователя
# user_name = 23
# info_user = {
#     "id": 333,
#     "username": "23",
#     "firstName": "331",
#     "lastName": "431",
#     "email": "53",
#     "password": "63",
#     "phone": "73",
#     "userStatus": 0
#   }
# res_put_User = requests.put(f"https://petstore.swagger.io/v2/user/{user_name}",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#                                   data = json.dumps(info_user, ensure_ascii=False))
# print(f"Статус ответа от сервера на PUT запрос редактирование пользователя: {res_put_User.status_code}")
# try:
#     rez = res_put_User.json()
#     print("Карточка пользователя:")
#     print(res_put_User.json())
# except:
#     rez = res_put_User.text()
#     print("Карточка пользователя:")
#     print(res_put_User.text())

#####################################################################################################
########## ПРОВЕРКА delete-запросов со сваггера v2  ###########
####################################################################################################

# # # удаление питомца
# petId = 2223
# res_del_Pet = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId}",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
# print(f"Статус ответа от сервера на DELETE запрос удаление питомца: {res_del_Pet.status_code}")

####################################################################################################

# # удаление пользователя
# user_name = 23
# res_del_User = requests.delete(f"https://petstore.swagger.io/v2/user/{user_name}",
#                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
# print(f"Статус ответа от сервера на DELETE запрос удаление пользователя: {res_del_User.status_code}")