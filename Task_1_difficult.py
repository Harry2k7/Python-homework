# задача 1 сложная необязательная. Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

def sum_of_digits(num):
    integer_part = int(num)
    fractal_part = round(num % 1, 6)
    total_sum = 0

    while integer_part > 0:
        digit = integer_part % 10
        total_sum += digit
        integer_part //= 10

    for _ in range(6):
        fractal_part *= 10
        digit = int(fractal_part) % 10
        total_sum += digit
        fractal_part -= digit

    return total_sum

num = float(input("Введите любое число: "))
print(f"Сумма цифр числа {num} равна {sum_of_digits(num)}")