# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number = int(input("Введите целое число: "))
 
factorial = 1 
while number > 1:
    factorial *= number
    number -= 1
 
print(factorial)






import math
number = input("Введите целое число: ")
result = math.factorial(int(number))
print(result) 
