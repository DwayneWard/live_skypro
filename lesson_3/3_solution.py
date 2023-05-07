# 1

numbers = [4, 5, 7, 8, 10]
num = int(input("Введите число: "))
if num in numbers:
    print("Число есть")
else:
    print("Числа нет")

# 2

numbers = [4, 5, 7, 8, 10]

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 in numbers and num2 in numbers:
    print("Оба числа есть")
elif num1 in numbers or num2 in numbers:
    print("Одно из чисел есть")
else:
    print("Ни одного из чисел нет")

# 3

numbers = [10, 4, 5, 10, 7, 8, 10]
sum_numbers = 0
for number in numbers:
    if number < 10:
        sum_numbers += number
print(sum_numbers)

# 4

numbers = [10, 4, 5, 1, 2, 10, 7, 8, 1, 2, 10]
count = 0
for num in numbers:
    if num == 1 or num == 2:
        count += 1
print(count)

# 5

numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [8, 9, 10, 11, 12]

avg_1 = sum(numbers_1) / len(numbers_1)
avg_2 = sum(numbers_2) / len(numbers_2)

if avg_1 > avg_2:
    print("Первое среднее больше")
elif avg_2 > avg_1:
    print("Второе среднее больше")
else:
    print("Средние одинаковые")

# 6

words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
lengths = [len(word) for word in words]
print(lengths)

# 7
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

even = []  # список для четных элементов
odd = []  # список для нечетных элементов

for i in range(len(letters)):
    if i % 2 == 0:
        odd.append(letters[i])
    else:
        even.append(letters[i])

# выводим результат
print("Нечетные\n")
for item in odd:
    print(item)

print("\nЧетные\n")
for item in even:
    print(item)

# 8

words = [letter for letter in letters if letter not in vowels]
print(words)

# 9
a = int(input())
b = int(input())

result = []

for i in range(a + 1, b):
    if i % 2 == 0:
        result.append(i)

print(*result, sep="\n")

# 10
items = [7, 62, 1, 3, 1, 2, 0, 1]

indices = []
for i in range(len(items)):
    if items[i] in [0, 1]:
        indices.append(i)

print(indices)

# 11

positions = []
for i in range(len(items)):
    if items[i].isdigit():
        positions.append(i)

print(positions)

# 12

for keyword in keywords:
    if keyword != "Пропуск":
        print(keyword, end=" ")

# 13
message = ""
for word in list_w_spaces:
    if word == "тчк":
        message += "."
    elif word == "зпт":
        message += ","
    else:
        message += word
    message += " "

message = message.rstrip()  # удалить пробел в конце строки

print(message)

# 14

score = 0
misses = 0
for throw in throws:
    if throw != 0:
        score += throw
    else:
        misses += 1
        score -= misses * 10

print(score)

# 15

sum_age = 0
for age in residents:
    sum_age += age

average_age = sum_age / len(residents)

print(int(average_age))

# 16

powers_of_two = []
result = 1
for i in range(8):
    powers_of_two.append(result)
    result *= 2

print(*powers_of_two)

# 17

numbers_with_one = []
for i in range(1, 120):
    if "1" in str(i):
        numbers_with_one.append(i)

print(*numbers_with_one)

# 18

for i in range(len(sequence)):
    if sequence[i] == 0:
        print(i)

# 19
for letter in reversed(letters):
    print(letter, end=" ")

# ИЛИ

for letter in letters[::-1]:
    print(letter, end=" ")

# 20

for i in range(len(en)):
    print(en[i], "-", ru[i])

# 21

while True:
    answer = input("Ты сделал домашку?\n> ")
    if answer.lower() == "да":
        print("Какой ты молодец")
        break
    else:
        print("Ты должен сделать домашку!")

# 22

i = 1
while i <= 5:
    print(i)
    i += 1

# 23

i = 0
while i < len(keywords):
    if keywords[i] != "Пропуск":
        print(keywords[i], end=" ")
    i += 1

# 24
restricted = [7, 17, 21, 40, 50, 60, 70, 100]

for i in range(101):
    if i not in restricted:
        print(i, end=" ")

# 25
i = 0
while letters[i] != "stop":
    print(letters[i], end=" ")
    i += 1

shopping_list = []

# 26
while True:
    item = input("Введите покупку (или 'хватит', чтобы закончить): ")
    if item == "хватит":
        break
    else:
        shopping_list.append(item)

print("Список покупок:")
for item in shopping_list:
    print(item)

# 27
expenses = []

while True:
    expense = input("Введите трату (или 'хватит', чтобы закончить): ")
    if expense == "хватит":
        break
    else:
        expenses.append(expense)

print("Список трат:")
for expense in expenses:
    print(expense)

# --------------------------------
# Задачи для 9.1 потока
# 1
n = int(input("Введите количество элементов ряда: "))

a, b = 0, 1
print(a)
print(b)

for i in range(3, n+1):
    c = b
    b = a + b
    a = c
    print(b)
# ------
n = int(input("Введите количество элементов ряда: "))

a, b = 0, 1
print(a)
print(b)

for i in range(3, n+1):
    a, b = b, a+b
    print(b)

# 2

n = abs(int(input("Введите целое число, состоящее из разных цифр: ")))
max = 0

while n > 0:
    digit = n % 10
    if digit > max:
        max = digit
    n //= 10

print("Наибольшая цифра числа:", max)

# 3

n = int(input("Введите число: "))
m = 0

while n > 0:
    a = n % 10
    m = m * 10 + a
    n //= 10

print("Число с обратным порядком цифр:", m)

# 4
for n in range(20, 31):
    print("Начальное число:", n)
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
            n //= 2
        steps += 1
    print("Число шагов:", steps)
