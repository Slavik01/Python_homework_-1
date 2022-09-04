# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import math
max_number = math.inf # положительное бесконечное число
min_number = -math.inf # отрицательное бесконечное число

y = float(input('Введите число y: '))
x = float(input('Введите число x: '))

if (y < max_number and y >= 1) and (x < max_number and x >= 1):
    print("1 плоскость")

elif ((y < max_number and y >= 1) and (x > min_number and x <= -1)):
    print("2 плоскость")

elif ((y > min_number and y <= -1) and (x > max_number and x <= -1)):
    print("3 плоскость")

elif ((y > min_number and y <= -1) and (x < max_number and x >= 1)):
    print("4 плоскость")
else:
    y == 0 and x == 0
    print("x и y не равны нулю!")


# if ((y > 40 and x < 40) or (x > 40 and y < 40) or (y < -40 and x > 1) or (y > 40 and x > 40) or (y < -40 and x < -40)):
#     print("Вы ввели неверный диапозон чисел!")

# elif (y < 40 and y > 1) and (x < 40 and x > 1):
#     print("1 плоскость")

# elif ((y < 40 and y > 1) and (x > - 40 and x < -1)):
#     print("2 плоскость")

# elif ((y > -40 and y < -1) and (x > -40 and x < -1)):
#     print("3 плоскость")

# elif ((y > -40 and y < - 1) and (x < 40 and x > 1)):
#     print("4 плоскость")
