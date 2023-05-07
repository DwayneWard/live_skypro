# 1
# Напишите функцию `get_unique_names(names)`, которая принимает список и
# возвращает уникальные элементы из него в виде списка.
def get_unique_names(names):
    pass


names = ["Yvor", "Wendell", "Hogan", "Sadella", "Yvor", "Sadella", "Hogan"]
unique_names = get_unique_names(names)
print(unique_names)


# Пример вывода:
# ["Yvor", "Wendell", "Hogan", "Sadella"]

# 2
# Напишите функцию, которая печатает имена из списка словарей в таком формате:
# Kingsley
# Tobit
# Pace
# Andreas
# Anthia


def get_names_from_user_list(users):
    pass


# Данные:
users = [
    {
        "id": 1,
        "first_name": "Anthia",
        "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
    },
    {
        "id": 2,
        "first_name": "Tobit",
        "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
    },
    {
        "id": 3,
        "first_name": "Pace",
        "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
    },
    {
        "id": 4,
        "first_name": "Andreas",
        "url": "https://ifeng.com/morbi/vestibulum/velit.png"
    },
    {
        "id": 5,
        "first_name": "Anthia",
        "url": "https://google.com/eu/orci.aspx"
    },
    {
        "id": 6,
        "first_name": "Tobit",
        "url": "https://google.com/eu/orci.aspx"
    },
]


# 3
# Напишите функцию, которая печатает УНИКАЛЬНЫЕ имена из списка словарей в таком формате:
#
# Anthia
# Tobit
# Pace
# Andreas

# Данные:
users = [
    {
        "id": 1,
        "first_name": "Anthia",
        "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
    },
    {
        "id": 2,
        "first_name": "Tobit",
        "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
    },
    {
        "id": 3,
        "first_name": "Pace",
        "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
    },
    {
        "id": 4,
        "first_name": "Andreas",
        "url": "https://ifeng.com/morbi/vestibulum/velit.png"
    },
    {
        "id": 5,
        "first_name": "Anthia",
        "url": "https://google.com/eu/orci.aspx"
    },
    {
        "id": 6,
        "first_name": "Tobit",
        "url": "https://google.com/eu/orci.aspx"
    },
]


# 4
# Напишите функцию `get_ids(users)`, которая возвращает id из списка словарей в таком формате:
# [1,2,3,...]

def get_ids(users):
    pass


# Данные:
users = [
    {
        "id": 1,
        "first_name": "Anthia",
        "url": "https://weather.com/aliquet/at/feugiat/non/pretium.jsp"
    },
    {
        "id": 2,
        "first_name": "Tobit",
        "url": "http://pen.io/sapien/cursus/vestibulum/proin/eu/mi/nulla.json"
    },
    {
        "id": 3,
        "first_name": "Pace",
        "url": "http://ucsd.edu/justo/morbi/ut/odio/cras/mi.json"
    },
    {
        "id": 4,
        "first_name": "Andreas",
        "url": "https://ifeng.com/morbi/vestibulum/velit.png"
    },
    {
        "id": 5,
        "first_name": "Anthia",
        "url": "https://google.com/eu/orci.aspx"
    },
    {
        "id": 6,
        "first_name": "Tobit",
        "url": "https://google.com/eu/orci.aspx"
    },
]

# print(get_ids(users))
# Вернет [1,2,3,4,5]

# 5
# Напишите функцию filter_yellow_only(animals), которая выводит только тех животных, которые желтые (yellow)
# Пример вывода:

# Francolinus coqui is Yellow
# Petaurus norfolcensis is Yellow

# Данные:
animals = [
    {
        "id": 1,
        "specie": "Francolinus coqui",
        "color": "Yellow"
    },
    {
        "id": 2,
        "specie": "Petaurus norfolcensis",
        "color": "Yellow"
    },
    {
        "id": 3,
        "specie": "Pseudoleistes virescens",
        "color": "Teal"
    },
    {
        "id": 4,
        "specie": "Sula dactylatra",
        "color": "Maroon"
    },
    {
        "id": 5,
        "specie": "Echimys chrysurus",
        "color": "Teal"
    }
]


# 6 КРИВЫЕ ДАННЫЕ
# Напишите функцию  `filter_violet_only(animals)`, которая возвращает в формате
# списка id только тех животных, которые фиолетовые (`violet`)
#
# Пример ввода:

def filter_violet_only(animals):
    pass


# Вернет [1, 2, 5]

# Данные:
animals = [
    {
        "id": 1,
        "specie": "Francolinus coqui",
        "color": "Yellow"
    },
    {
        "id": 2,
        "specie": "Petaurus norfolcensis",
        "color": "Yellow"
    },
    {
        "id": 3,
        "specie": "Pseudoleistes virescens",
        "color": "Teal"
    },
    {
        "id": 4,
        "specie": "Sula dactylatra",
        "color": "Maroon"
    },
    {
        "id": 5,
        "specie": "Echimys chrysurus",
        "color": "Teal"
    }
]

# 7
# Напишите функцию  `get_names_sorted(animals)`, которая возвращает в формате
# списка строк названия всех животных отсортированных по алфавиту.

# Данные:
animals = [
    {
        "specie": "Macaca fuscata",
        "color": "Khaki"
    },
    {
        "specie": "Cygnus atratus",
        "color": "Aquamarine"
    },
    {
        "specie": "Ursus arctos",
        "color": "Yellow"
    }
]


def get_names_sorted(animals):
    pass


# print(get_names_sorted(animals))
# Должна вернуть
# ["Cygnus atratus", "Macaca fuscata", "Ursus arctos"]

# 8
# Напишите функцию  get_comments_by_post_id(comments, post_id) которая
# возврашает только те комментарии, которые к определенному посту.

# Данные:
comments = [
    {
        "author": "Werner",
        "time": "2:14 PM",
        "comment": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
        "post_id": 3
    },
    {
        "author": "Raymond",
        "time": "12:48 PM",
        "comment": "Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
        "post_id": 5
    },
    {
        "author": "Silvio",
        "time": "2:45 PM",
        "comment": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
        "post_id": 1
    },
    {
        "author": "Shelbi",
        "time": "1:29 AM",
        "comment": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.",
        "post_id": 5
    },
    {
        "author": "Barnabas",
        "time": "2:28 PM",
        "comment": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
        "post_id": 5
    },
    {
        "author": "Mariellen",
        "time": "6:51 AM",
        "comment": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
        "post_id": 1
    },
    {
        "author": "Brandon",
        "time": "1:29 AM",
        "comment": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.",
        "post_id": 2
    }
]


def get_comments_by_post_id(comments, post_id):
    pass


# Пример вызова get_comments_by_post_id(comments, 1)
#
#  [{
#   "author": "Silvio",
#   "time": "2:45 PM",
#   "comment": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
#   "post_id": 1
# },{
#   "author": "Mariellen",
#   "time": "6:51 AM",
#   "comment": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
#   "post_id": 1
# }]


# 9
# У вас есть два списка. Напишите функцию `count_common(first,second)`, которая возвращает, сколько элементов у них общие.
def count_common(first, second):
    pass


first = [1, 2, 3, 4, 5]
second = [4, 5, 6, 7]

# count_common(first, second)
# Вернет 2

# 10
# У вас есть два списка. Напишите функцию count_unique которая вернет
# количество уникальных в первом списке (входящих в первый, но не входящих во второй)
def count_unique(first, second):
    pass


first = [1, 2, 3, 4, 5]
second = [4, 5, 6, 7]

# result = count_unique(first, second)
# print(result)
# Вернет 3


# # 11
# У вас есть список всех задач, которые нужно сделать и три исполнителя,
# которые решали эти задачи, выведите задачи, которые никто не решил.

tasks = [
   "сходить в магазин" ,
   "купить гвозди",
   "полить сельдерей",
   "украсить елку",
   "нарисовать снежинку",
   "найти открытки"
]

emp_1 = ["купить гвозди", "найти открытки"]
emp_2 = ["полить сельдерей","сходить в магазин"]
emp_3 = ["найти открытки","купить гвозди"]
