# У вас есть следующие требования к ответу:
#   timestamp: int                                             item_id: string
#   referer: string (url)                                      item_price: int
#   location: string (url)                                     item_url: string (url)
#   remoteHost: string                                         basket_price: string
#   partyId: string                                            detectedDuplicate: bool
#   sessionId: string                                          detectedCorruption: bool
#   pageViewId: string                                         firstInSession: bool
#   eventType: string (itemBuyEvent или itemViewEvent)         userAgentName: string

# проверить, что каждый объект в JSON:
# Содержит все перечисленные в требованиях поля. Не имеет других полей.
#Все поля имеют именно тот тип, который указан в требованиях:
#int — целое число;
#string — произвольная строка;
#string (url) — это строка с url. В рамках этого задания проверяем, # что url начинается c http:\\ или https:\\;
#string (itemBuyEvent или itemViewEvent) — строка, в которой могут быть только эти конкретные два значения и никакие другие;
#bool — булево значение, то есть True или False.
# Тест должен вернуть Pass или список значений, которые тест посчитал ошибочными, и причину, почему они ошибочные.

import json
import re

standart_list_items = {'timestamp': 'int', 'referer': 'url', 'location': 'url', 'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'eventType': 'val', 'item_id': 'str', 'item_price': 'int', 'item_url': 'url', 'basket_price': 'str', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool', 'firstInSession': 'bool', 'userAgentName': 'str'}
item_val = {'itemBuyEvent', 'itemViewEvent'}
base_len =int(len(standart_list_items))

# открываем файл и переводим в список в виде строки
with open('tmp_base2.json', 'r', encoding='utf8') as f:
    data_base_tmp = f.read()
    data_base_list = json.loads(data_base_tmp)
    # print(data_base_list)
# проходим по каждому объекту (словарю) в нашей базе данных
count = 0
# object - словарь, ключ - название поля, значение - какой может быть тип
flag = True
for object in data_base_list:
    # print(object)
    # print(type(object))
    count += 1
    # получаем список ключей объекта (словаря)
    base_keys = object.keys()
    label = True if len(base_keys) == base_len else False
    if not label:
        print(f"Ошибка - {count}й объект БД: количество ключей не совпадает с шаблоном")
        flag = False
        continue

# перебрать в цикле каждую пару ключ-значение
    for item in object.items():
        # print(item[0], item[1])
        # проверяем к какому классу (виду) полей должен относиться каждый ключ
        item_type = standart_list_items.get(item[0])
        # print(item_type)
        if item_type is None:
            print(f"Элемент с именем {item[0]} в {count}м объекте БД не найден в шаблоне")
            flag = False
        else:
            if not((item_type == 'int' and type(item[1]) is int) \
                    or (item_type == 'str' and type(item[1]) is str) \
                    or (item_type == 'bool' and type(item[1]) is bool) \
                    or (item_type == 'val' and type(item[1]) is str and item[1] in item_val) \
                    or ((item_type == 'url' and type(item[1]) is str) and (re.match(r'^https{0,1}://.+$', item[1])))):
                print(f"Элемент с именем {item[0]} в {count}м объекте БД должен иметь тип {item_type}")
                flag = False

if flag:
    print("Pass")
