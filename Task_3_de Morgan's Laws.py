# задача Де моргана необязательная.
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически  в цикле 100 раз прогоняем каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением и засекаем общее время выполнения программы юзаем библиотеки random и time предикаты НЕ ЗАДАЕМ как целое число!

import random
import time

def check_statement():
    
    num_predicates = random.randint(3, 15)

    predicates = [random.choice([True, False]) for _ in range(num_predicates)]  # Генерация случайных булевых значений для каждого предиката

    left_side = any(predicates)  # Вычисление левой части утверждения

    right_side = all(not p for p in predicates)  # Вычисление правой части утверждения

    statement = not left_side == right_side # Проверка истинности утверждения

    return statement

start_time = time.time()

for _ in range(100):
    statement_result = check_statement()

end_time = time.time()

print(f"Время выполнения программы: {end_time - start_time} секунд.")