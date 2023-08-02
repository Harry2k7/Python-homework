# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def arithmetic_progression(first: int, diff: int, quantity: int) -> list[int]:
    progression = []
    for i in range(1, quantity + 1):
        an = first + (i - 1) * diff
        progression.append(an)
    return progression


a1 = int(input("Введите значение 1-го элемента: "))
d = int(input("Введите разность элементов: "))
n = int(input("Введите количество элементов: "))

print(f"Арифметическая прогрессия: {arithmetic_progression(a1, d, n)}")