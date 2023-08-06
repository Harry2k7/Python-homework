# Задача CALC необязательная. Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Тут может помочь библиотека re

import re
 
 
actions = {
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
 
def my_evaluate(expresion: str) -> str:
 
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_evaluate(match.group(1)))
 
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
 
exp1 = "(1+4) * (5*(10-2))/(-5)"
exp2 = "100 - 2 * -33"
exp3 = "21 + 7 * 3 + 5 / -2"

print(f'{exp1} => {my_evaluate(exp1)} Проверка {eval(exp1)}')
print(f'{exp2} => {my_evaluate(exp2)} Проверка {eval(exp2)}')
print(f'{exp3} => {my_evaluate(exp3)} Проверка {eval(exp3)}')