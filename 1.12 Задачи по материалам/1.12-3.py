'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
'''

x, y, z = float(input()), float(input()), str(input())
if (z == "/" and y == 0) or (z == "mod" and y == 0) or (z == "div" and y == 0):
    print("Деление на 0!")
elif z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "/":
    print(x / y)
elif z == "*":
    print(x * y)
elif z == "mod":
    print(x % y)
elif z == "pow":
    print(x ** y)
elif z == "div":
    print(x // y)
