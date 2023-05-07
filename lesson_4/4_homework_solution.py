# словари по уровням сложности
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# словарь ранга пользователя
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# счетчик ранга
count = 0

# словарь уровней сложности
words = {
    "легкий": words_easy,
    "средний": words_medium,
    "сложный": words_hard
}

# словарь с записями о верных и неверных ответах.
answers = {}

# Выбор уровня сложности
choice = input("""Выберите уровень сложности.
Легкий, средний, сложный.""").lower()
if choice in words:
    selected_dict = words[choice]

    # # словарь от выбранного уровня
    # selected_dict = words[choice]

    # Перебор вопросов
    for k, v in selected_dict.items():
        answer = input(f"{k}, {len(v)} букв, начинается на {v[0]}     Ответ:   ").lower()
        if answer == v:
            print(f"Верно, {k} - это {v}")
        else:
            print(f"Неверно. {k} — это {v}.")
        answers[k] = answer == v

    # вывод правильных ответов
    print()
    print("Правильно отвечены слова:")
    for word, bool_v in answers.items():
        if bool_v == True:
            print(word)
            count += 1

    # вывод неправильных ответов
    print()
    print("Неправильно отвечены слова:")
    for word, bool_v in answers.items():
        if bool_v != True:
            print(word)

    # вывод ранга
    print()
    print(f"""Ваш ранг:
{levels[count]}""")

else:
    print("Нет такой сложности")

