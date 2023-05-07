count_scores = 0
count_questions = 0

# Приветствие
print('''Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут.''')
name_user = (input())
print(f"Привет, {name_user} начинаем тренировку!")
print("Let\'s begin")

# Тест
answer_1 = (input("My name ___ Vova. "))
if answer_1 == "is":
    print('''Ответ верный!
Вы получаете 10 баллов!''')
    count_scores += 10
    count_questions += 1
else:
    print('''Неправильно.
Правильный ответ: is''')

answer_2 = (input("I ___ a coder. "))
if answer_2 == "am":
    print('''Ответ верный!
Вы получаете 10 баллов!''')
    count_scores += 10
    count_questions += 1
else:
    print('''Неправильно.
Правильный ответ: am''')

answer_3 = (input("I live ___ Moscow. "))
if answer_3 == "in":
    print('''Ответ верный!
Вы получаете 10 баллов!''')
    count_scores += 10
    count_questions += 1
else:
    print('''Неправильно.
Правильный ответ: in''')

# Процент правильных ответов
percent = round(count_questions / 3 * 100)

# Результат
print(f'''Вот и всё, {name_user}!
Вы ответили на {count_questions} вопросов из 3 верно.
Вы заработали {count_scores} баллов.
Это {percent} процентов.''')
