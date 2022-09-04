# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Задайте номер четверти: '))

if number == 1:
    print("Диапазон y от 0 до math.inf, x от 0 до math.inf ")
elif number == 2:
    print("Диапазон y от 0 до math.inf, x от -0 до -math.inf ")
elif number == 3:
    print("Диапазон y от -0 до -math.inf, x от -0 до -math.inf ")
elif number == 4:
    print("Диапазон y от -0 до -math.inf, x от 0 до math.inf ")
else:
    print("Вы ввели неверный номер четверти!")