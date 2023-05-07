# import random
#
# questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
# answers = ["is", "am", "in"]
#
# print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать!")
# ready = input()
#
# if ready == "ready":
#     print("Отлично! Начинаем!")
#     num_questions = len(questions)
#     correct_answers = 0
#     for i in range(num_questions):
#         question = questions[i]
#         answer = answers[i]
#         print("Вопрос номер", i + 1)
#         print(question)
#         user_answer = input().strip()
#         if user_answer == answer:
#             print("Ответ верный!")
#             correct_answers += 1
#         else:
#             print("Неправильно. Правильный ответ:", answer)
#     print("Вот и все! Вы ответили на", num_questions, "вопросов из", num_questions, "верно, это", round(correct_answers / num_questions * 100, 1), "процентов.")
# else:
#     print("Кажется, вы не хотите играть. Очень жаль.")



# *

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать!")
ready = input()
if ready != "ready":
    print("Кажется, вы не хотите играть. Очень жаль.")
else:
    total_questions = len(questions)
    score = 0
    for i in range(total_questions):
        attempts = 3
        print(questions[i])
        while attempts > 0:
            answer = input("Введите ответ: ")
            if answer.lower() == answers[i]:
                if attempts == 3:
                    score += 3
                elif attempts == 2:
                    score += 2
                elif attempts == 1:
                    score += 1
                print("Ответ верный!")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Осталось попыток: {attempts}, попробуйте еще раз!")
                else:
                    print(f"Увы, но нет. Верный ответ: {answers[i]}")

    print(f"Вот и все! Вы ответили на {total_questions} вопросов из {total_questions} верно, вы набрали {score} баллов.")
