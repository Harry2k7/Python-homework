# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X, Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int(input('Введите сумму чисел: '))
prod = int(input('Введите произведение чисел: '))

X = (sum - int((sum ** 2 - 4 * prod) ** 0.5)) // 2
Y = sum - X
if X <= 1000 and Y <= 1000:
    print('Петя обманул')
print(f'числа задуманные Петей{X, Y}')
