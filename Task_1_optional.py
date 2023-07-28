# Задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно: Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел. Добавьте аннотацию типов где это возможно. Используйте функции

def convert_to_base(num: int, base: int) -> str:
    if num == 0:  
        return '0'
    
    digits = '0123456789ABCDEF'  # Символы для шестнадцатеричной системы счисления
    
    result = ''
    while num > 0:
        remainder = num % base  
        result = digits[remainder] + result  
        num //= base  
        
    return result


def get_binary_octal_and_hex(num: int) -> tuple[str, str]:
    binary = convert_to_base(num, 2)   # Получаем двоичное представление числа
    octal = convert_to_base(num, 8)    # Получаем восьмеричное представление числа
    hexadec = convert_to_base(num, 16) # Получаем шестнадцатеричное представление числа

    return binary, octal, hexadec



num = int(input("Введите целое число: "))
binary, octal, hexadec = get_binary_octal_and_hex(num)

print("Двоичное представление числа:", binary)
print("Восьмеричное представление числа:", octal)
print("Шестнадцатеричное представление числа:", hexadec)
print()
print("Проверка с помощью функции bin():", bin(num))
print("Проверка с помощью функции oct():", oct(num))
print("Проверка с помощью функции hex():", hex(num))