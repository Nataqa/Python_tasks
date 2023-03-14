Для корректной работы тестов необходимо скопировать драйвер для вашей версии браузера Crome и расположить его по следующему пути:
D:\QAP\chromedriver\chromedriver.exe
Тесты запускаются при помощи стандартного запуска IDE или при помощи соответствующей комбинации горячих клавиш (например, в PyCharm это shift + F10).


conftest.py - файл, содержащий основные настройки для запуска тестов
consts.py - файл с переменными, требуемыми для запуска тестов, в том числе и со входными данными
test_RT.py - тесты, относящиеся к странице авторизации (часть 1)
test_RT_registr.py - тесты, относящиеся к странице регистрации
test_RT_autoriz_SS.py - тесты, относящиеся к авторизации через соцсети
test_RT_autoriz.py - тесты, относящиеся к странице авторизации (часть 2)


В связи с ограниченностью времени работы над проектом реализована только малая часть ТК (21 ТК) и автотестов к ним.
В реализованных ТК проверяются поля на наличие орфографических ошибок, изменение плейсхолдера при переключении типа логина, 
изменение типа авторизации при вводе логинов различного вида, возможность перейти на форму регистрации и восстановления пароля, 
обновление капчи на форме восстановления пароля, возможность прочитать пользовательское соглашение, 
возможность перейти на страницу авторизации через социальные сети, 
вывод соответствующих сообщений об ошибках при вводе в поля некорректных данных и др.