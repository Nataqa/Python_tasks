# импортируем необходимые библиотеки, классы, переменные и т.д.
import telebot
from starter import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' или '/help'.
@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: " \
           "<название валюты> <в какую перевести> <сколько перевести> \n " \
           "Увидеть список всех доступных валют: /values"
    bot.reply_to(message,text)

# Обрабатывается сообщение с командой '/values'
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Валюты, которые возможно использовать:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

# Обрабатывается сообщение с валютами для конвертации и их количеством
@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        input_data = message.text.split(" ")
        if len(input_data) != 3:
            raise ConvertionException("Неверное количество параметров.")
        quote, base, amount = input_data
        response = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка ввода.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Стоимость {amount} {keys[quote]} = {round(response, 2)} {keys[base]}"
        bot.send_message(message.chat.id, text)

bot.polling()
