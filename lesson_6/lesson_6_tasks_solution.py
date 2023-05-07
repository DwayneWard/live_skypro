# 1
with open("data.txt", "r") as f:
    text = f.readline()
    print(text)

# 2
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
        print("---")

# 3
with open("data.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    print(f"{i + 1} {line.strip()}")
# ИЛИ
with open('data.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    print(f"{i + 1} {lines[i].strip()}")

# 4
def calculate_expenses_stats(file_path):
    with open(file_path, 'r') as f:
        expenses_list = [int(line.strip()) for line in f.readlines()]
    total_expenses = sum(expenses_list)
    avg_expenses = total_expenses / len(expenses_list)
    print(f"Сумма: {total_expenses}")
    print(f"Среднее: {avg_expenses}")


# 5
def load_list_from_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        return [((line.strip() for line in lines))]


# 6
def load_dict_from_file(path):
    with open(path) as f:
        lines = f.readlines()
        dictionary = {}
        for line in lines:
            key, value = line.split()
            dictionary[int(key)] = value
        return dictionary


file_path = "data.txt"
data_dict = load_dict_from_file(file_path)
print(data_dict)

# 7
string = input("Введите строку: ")

with open("recorded.txt", "w") as f:
    f.write(string)

# 8
# Открываем файл для записи
with open("output.txt", "w") as f:
    # Получаем три строки от пользователя и записываем их в файл
    f.write(input() + "\n")
    f.write(input() + "\n")
    f.write(input() + "\n")

# 9
with open('expenses.txt', 'r') as f:
    expenses = f.read().splitlines()

expenses = [int(e) for e in expenses]
min_expense = min(expenses)
max_expense = max(expenses)
sum_expenses = sum(expenses)

with open('info.txt', 'w') as f:
    f.write(f'min: {min_expense}\n')
    f.write(f'max: {max_expense}\n')
    f.write(f'sum: {sum_expenses}\n')

# ИЛИ
with open('expenses.txt', 'r') as expenses_file:
    expenses = []
    for line in expenses_file:
        expenses.append(int(line.strip()))

min_expense = min(expenses)
max_expense = max(expenses)
sum_expense = sum(expenses)

with open('info.txt', 'w') as info_file:
    info_file.write(f"min: {min_expense}\n")
    info_file.write(f"max: {max_expense}\n")
    info_file.write(f"sum: {sum_expense}\n")

# 10
n = int(input("Введите число от 1 до 5: "))

if 1 <= n <= 5:
    for i in range(1, n + 1):
        filename = str(i) + ".txt"
        with open(filename, "w") as f:
            f.write("файл создан")
else:
    print("Ошибка: число должно быть от 1 до 5.")
