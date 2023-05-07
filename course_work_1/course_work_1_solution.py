import random

words_to_encode = ["code", "bit", "list", "soul", "next"]

morse_dictionary = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

answers = []

#
# def morse_encode(word):
#     """
#     Кодирует слово на английском в азбуку Морзе.
#     :param word: Слово для кодирования
#     :return: Строку, содержащую закодированное слово
#     """
#     encode_word = []
#     for letter in word:
#         encode_word.append(morse_dictionary[letter])
#     encode_word_string = ' '.join(encode_word)
#     return encode_word_string
#
#
# def get_word():
#     """
#     Выбираем случайное слово из списка.
#     :return: Случайное слово
#     """
#     random_word = random.choice(words_to_encode)
#     return random_word
#
#
# def print_statistic(user_answers):
#     """
#     Распечатывает в консоль статистику работы программы и ответы пользователя.
#     :param user_answers: Список с ответами пользователя, содержащий булевые значения
#     :return: Не возвращает значение, а распечатывает текст в консоль
#     """
#     print(f'Всего задачек: {len(user_answers)}\n'
#           f'Отвечено верно: {user_answers.count(True)}\n'
#           f'Отвечено неверно: {user_answers.count(False)}\n'
#           )
#
#
# print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
#
#
# while True:
#     user_input = input('Нажмите Enter и начнем\n')
#     if user_input == '':
#         break
#
#
for task_number in range(1, 6):
    random_word = get_word()
    encode_task_word = morse_encode(random_word)

    print(f"Слово {task_number}: {encode_task_word}\n")

    user_answer = input('Введите перевод слова: ')

    if user_answer.lower() == random_word.lower():
        print(f"Верно, {random_word}!")
        answers.append(True)
    else:
        print(f"Неверно. Верный ответ: {random_word}!")
        answers.append(False)

#
# print_statistic(answers)
