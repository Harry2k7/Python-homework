# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

num = int(input("Введите целое число больше 1: "))
k = 1
while k <= num:
    print(k, end =' ')
    k = k * 2