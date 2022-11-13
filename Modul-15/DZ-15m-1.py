# Напишите программу, которая получает от пользователя имя файла, открывает
# этот файл в текущем каталоге, читает его и выводит два слова: наиболее
# часто встречающееся из тех, что имеют размер более трех символов, и
# наиболее длинное слово на английском языке.

#читаем файл в переменную my_File, преобразовываем в строку
with open("filename1.txt", encoding="utf-8") as myFile:
    myFile_str = myFile.read()

# Функция редактирования текста
def redact_File (text):
    text = text.lower()  # приводим все символы к нижнему регистру
    text = text.replace("\n", "")  # убираем перехода на новую строку
    for i in '!"\'#$%&()*+-—,./:;<=>?@[\\]^_{|}~':
        text = text.replace(i, ' ')
    text = text.replace("   ", " ")  # заменяем 3 пробела одним
    text = text.replace("  ", " ")  # убираем 2 пробела одним
    return text

# Функция удаления элементов по длине
def delete_elem (text, lenght):
    List_world = []
    for item in text:
        if len(item) > lenght:
            List_world.append(item)
    return List_world

# Функция определения самого длинного английского элемента
def max_angl_word (text):
    # выбираем из общего списка все английские слова
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    myFile_list_angl = []
    for item in myFile_list:
        for char in item:
            if char in alphabet:
                label = True
                continue
            else:
                label = False
                continue
        if label:
            myFile_list_angl.append(item)
    # определяем максимальные элементы
    list_max_angl = []
    word = max(myFile_list_angl, key=len)
    for i in myFile_list_angl:
        if len(i) == len(word):
            list_max_angl.append(i)

    return list_max_angl

# Функция определения максимального повторения слов
def max_count (text):
    word = {}
    max_w = {}
    for item in myFile_list:
        if item in word:
            count = word.get(item)
            word.update({item: count + 1})
        else:
            word.update({item: 1})

    # преобразуем словарь в список отображение
    key_word = word.items()
    # преобразуем отображение в список кортежей (ключ, значение)
    key_word_list = list(key_word)
    # находим пару, в которой значение максимально
    max_count_word = max(key_word_list, key=lambda i: i[1])
    tmp = max_count_word[1]

    for item in word.items():
        if item[1] == max_count_word[1]:
            ff = {item}
            max_w.update(ff)

    return max_w


# вызываем функцию редактирования текста (строки)
myFile_str = redact_File(myFile_str)
# print(myFile_str)
# преобразуем отредактированную строку в список
myFile_list = myFile_str.split()
# print(myFile_list)
# #убираем маркер начала (пробелы)
# myFile_list = [elem.strip().replace('\ufeff', '') for elem in myFile_list]
# # print(myFile_list)

# вызываем функцию удаления элементов, меньших определенной длины
myFile_list = delete_elem(myFile_list, 3)
# print(myFile_list)

# вызываем функцию определения максимального английского слова
max_angl = max_angl_word(myFile_list)
# print(max_angl)

# вызываем функцию определения слова с максимальным повторением
max_word = max_count(myFile_list)
# print(max_word)

print(f'Список самых частых слов длинной более трёх символов: {max_word}')
print(f'Список самых длинных английских слов: {max_angl}')
