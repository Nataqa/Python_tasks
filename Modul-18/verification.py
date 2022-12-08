# импортируем необходимые библиотеки, переменные и т.д.
import requests
import json
from starter import keys

class ConvertionException(Exception):
    pass
# класс для отлавливания ошибок пользователя и конвертации валют
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException("Невозможно перевести в ту же самую валюту.")
        try:
            quote_label = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не верно задана валюта {quote}")
        try:
            base_label = keys[base]
        except KeyError:
            raise ConvertionException(f"Не верно задана валюта {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не верно задано количество конвертируемой валюты {amount}")
        #используем сторонний ресурс с актуальными курсами валют
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        valuta_dict_all = json.loads(response.content)['Valute']
        for object in valuta_dict_all:
            if quote == 'рубль':
                quote_value = 1
            else:
                quote_value = valuta_dict_all[quote_label]['Value']
            if base == 'рубль':
                base_value = 1
            else:
                base_value = valuta_dict_all[base_label]['Value']
        #вычисляем значение, результат конвертации
        response = float(amount) * quote_value / base_value
        return response
