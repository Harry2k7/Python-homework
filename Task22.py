# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# (Попробуйте использовать множества и их пересечение)

import random


set_a = {random.randint(-10, 11) for _ in range(int(input('Введите кол-во элементов первого множества: ')))}
set_b = {random.randint(-10, 11) for _ in range(int(input('Введите кол-во элементов второго множества: ')))}
set_c = set_a.intersection(set_b)
print()
print(f'Множество 1: {set_a}')
print()
print(f'Множество 2: {set_b}')
print()
print(sorted(set_c))