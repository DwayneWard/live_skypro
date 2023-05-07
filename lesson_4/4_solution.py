# 1
line = "13fet35kk54"
count_digits = 0
count_letters = 0

for char in line:
    if char.isdigit():
        count_digits += 1
    elif char.isalpha():
        count_letters += 1

print("Всего чисел:", count_digits)
print("Всего букв:", count_letters)

# 2
line = "13f et3 5kk54"
count_spaces = 0

for char in line:
    if char.isspace():
        count_spaces += 1

percent_spaces = (count_spaces / len(line)) * 100

print("Пробелов:", count_spaces, "это", round(percent_spaces), "%")
# ИЛИ
line = "13f et3 5kk54"
count_spaces = 0

for char in line:
    if char == ' ':
        count_spaces += 1

percent_spaces = (count_spaces / len(line)) * 100

print("Пробелов:", count_spaces, "это", round(percent_spaces), "%")

# 3
line = "сегодня #прогулка# #еда #ко#ты"

# Разбиваем строку на слова и считаем хештеги
hashtags_count = 0
words = line.split()
for word in words:
    if word.startswith("#"):
        hashtags_count += 1

print(f"Количество хештегов: {hashtags_count}")

# 4
line = "A13f et3 D 5kk54 M"

# Считаем количество заглавных букв
uppercase_count = 0
for char in line:
    if char.isupper():
        uppercase_count += 1

print(f"Количество заглавных букв: {uppercase_count}")

# 5
words = ["abcd", "ab", "bcdef"]

# Создаем словарь
length_dict = {word: len(word) for word in words}

print(length_dict)

# 6
# Получаем строку из стандартного ввода
s = input()

# Разделяем строку на две части, используя дефис как разделитель
start, end = map(int, s.split('-'))

# Извлекаем подстроку из исходной строки
result = s[start-1:end]

# Выводим результат
print(result)

# 7

words = ["Alpha", "Charlie"]
acronyms = {}

# Проходимся по всем словам из списка и добавляем их акронимы в словарь
for word in words:
    acronym = word[0]  # Получаем первую букву слова
    acronyms[word] = acronym  # Добавляем пару ключ-значение в словарь

print(acronyms)

# 8
input_str = input()  # Считываем строку со стандартного ввода
count, string = input_str.split()  # Разделяем строку на число и строку

# Проходимся по строке string count раз и выводим ее
for i in range(int(count)):
    print(string)

# 9

words = {"Alpha": "A", "Bravo": "V", "Charlie": "C", "Delta": "D", "Echo": "H"}

# Проходимся по всем ключам и значениям в словаре
for word, acronym in words.items():
    if not word.startswith(acronym):  # Если слово не начинается с соответствующего акронима
        print(f"{acronym} is not for {word}. Should start with {acronym}.")  # Выводим сообщение об ошибке

# 10
keywords = ["Желание", "Семнадцать", "Ржавый", "Пропуск", "Печь"]
word_lengths = {}  # Создаем пустой словарь

# Проходимся по всем словам в списке и добавляем их длины в словарь
for word in keywords:
    word_lengths[word] = len(word)

print(word_lengths)

# 12
shopping_list = {
  "Мандаринки": 150,
  "Шоколадные конфеты" : 200 ,
  "Гирлянда": 400,
  "Набор шаров": 300,
  "Хлопушки": 150
}

# Проходимся по всем ключам в словаре и выводим их на экран
for item in shopping_list.keys():
    print(item)

# 13

shopping_list = {
  "Мандаринки": 150,
  "Шоколадные конфеты" : 200 ,
  "Гирлянда": 400,
  "Набор шаров": 300,
  "Хлопушки": 150
}

total_cost = 0  # Создаем переменную для хранения суммы

# Проходимся по всем значениям в словаре и добавляем их к сумме
for item in shopping_list.values():
    total_cost += item

print(total_cost)

# 14

cities = {
  "Джакарта": 25,
  "Норильск" : -34 ,
  "Бангкок": 21,
  "Якутск": -52,
  "Москва": 5,
}

# Проходимся по всем ключам и значениям в словаре
for city, temperature in cities.items():
    if temperature > 10:  # Если температура больше 10 градусов
        print(city)

# 15

phrase = input("Введите фразу: ")
count = phrase.count("р")
print("Количество букв 'р':", count)

# или

phrase = input("Введите фразу: ")
count = 0
for letter in phrase:
    if letter == "р":
        count += 1
print("Количество букв 'р':", count)

# 16
code = ' ' + input()
for i in range(1, len(code)):
    if code[i] != '|':
        print(int(code[i - 1] == '|'), end='')


# Новая задача
a = "газета"
b = "загадка"
char_count = {}

for char in a:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

can_create = True

for char in b:
    if char not in char_count or char_count[char] == 0:
        can_create = False
        break
    char_count[char] -= 1

print(can_create)  # Вывод: False