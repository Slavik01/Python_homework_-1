# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# встроенная функция
# print(bin(45))

# 2
n = int(input('Введите десятичное число: '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f'Двоичное число : {b}')