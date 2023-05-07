# 1
def get_unique_names(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names


# 2
def get_names_from_user_list(users):
    """Печатает имена из списка словарей"""
    for user in users:
        print(user["first_name"])


# 3
def print_unique_names(users):
    unique_names = set()
    for user in users:
        unique_names.add(user["first_name"])
    for name in unique_names:
        print(name)


# 4
def get_ids(users):
    return [user["id"] for user in users]


# 5
def filter_yellow_only(animals):
    for animal in animals:
        if animal["color"] == "Yellow":
            print(f"{animal['specie']} is Yellow")


# 6
def filter_violet_only(animals):
    violet_animals = []
    for animal in animals:
        if animal["color"] == "Violet":
            violet_animals.append(animal["id"])
    return violet_animals


# 7
def get_names_sorted(animals):
    return sorted([animal["specie"] for animal in animals])


# 8
def get_comments_by_post_id(comments, post_id):
    return [comment for comment in comments if comment["post_id"] == post_id]


# 9
def count_common(first, second):
    set1 = set(first)
    set2 = set(second)
    return len(set1.intersection(set2))


# 10
def count_unique(first, second):
    # Создаем множества из списков
    first_set = set(first)
    second_set = set(second)
    first_set.difference(second_set)
    # Возвращаем размер пересечения разности первого множества и второго множества с первым множеством
    return len(first_set - second_set)


# 11

def get_unresolved_tasks(tasks, emp_1, emp_2, emp_3):
    # создаем множества задач и исполнителей
    task_set = set(tasks)
    emp_1_set = set(emp_1)
    emp_2_set = set(emp_2)
    emp_3_set = set(emp_3)

    # находим задачи, которые не решали исполнители
    unresolved_tasks = task_set - emp_1_set - emp_2_set - emp_3_set
    return unresolved_tasks
