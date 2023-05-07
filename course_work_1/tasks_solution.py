# 1
def count_for_true(elements):
    count = 0
    for element in elements:
        if element:
            count += 1
    return count


print(count_for_true([True, True, True]))  # вернет 3
print(count_for_true([False, True, False]))  # вернет 1
