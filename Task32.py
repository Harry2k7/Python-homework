# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

def find_indices(lst: list[int], min_value: int, max_value: int) -> list[int]:
    indices = []
    for i in range(len(lst)):
        if lst[i] >= min_value and lst[i] <= max_value:
            indices.append(i)
    return indices


my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = 3
max_value = 15

result = find_indices(my_list, min_value, max_value)
print("Индексы элементов, удовлетворяющих условию:")
print(result)