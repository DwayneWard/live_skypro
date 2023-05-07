# 1
class Room:
    def __init__(self, number, type, price):
        self.number = number
        self.type = type
        self.price = price

rooms = {
    12: Room(12, 'standard', 2000),
    13: Room(13, 'standard', 2000),
    14: Room(14, 'joint', 2500),
    15: Room(15, 'suite', 3000)
}

number = 13
room = rooms[number]

print(f"Номер: {room.number}")
print(f"Тип номера: {room.type}")
print(f"Цена за сутки: {room.price}")


# 2

class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print(f"Газировка и {self.addition}")
        else:
            print("Обычная газировка")

# 3
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        elif type(self.a) != int or type(self.b) != int or type(self.c) != int:
            return "Нужно вводить только числа!"
        elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return "Жаль, но из этого треугольник не сделать."
        else:
            return "Ура, можно построить треугольник!"

# 4


# 5
class Student:
    def __init__(self, name='Ivan', group_number='10A', age=18):
        self.name = name
        self.group_number = group_number
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name_age(self, name, age):
        self.name = name
        self.age = age

    def set_group_number(self, group_number):
        self.group_number = group_number


# Создаем 5 экземпляров класса Student с разными параметрами
student1 = Student(name='Alex', group_number='11B', age=19)
student2 = Student(name='Kate', group_number='12C', age=20)
student3 = Student(name='John', group_number='13D', age=21)
student4 = Student(name='Anna', group_number='14E', age=22)
student5 = Student(name='Peter', group_number='15F', age=23)

# Получаем данные об имени, возрасте и номере группы для каждого студента
print(student1.get_name(), student1.get_age(), student1.get_group_number())
print(student2.get_name(), student2.get_age(), student2.get_group_number())
print(student3.get_name(), student3.get_age(), student3.get_group_number())
print(student4.get_name(), student4.get_age(), student4.get_group_number())
print(student5.get_name(), student5.get_age(), student5.get_group_number())

# Изменяем данные для студента 1
student1.set_name_age('Max', 20)
student1.set_group_number('11A')

# Получаем измененные данные для студента 1
print(student1.get_name(), student1.get_age(), student1.get_group_number())


# 6
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return "Ошибка: деление на ноль"
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

# 7
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведен")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color
