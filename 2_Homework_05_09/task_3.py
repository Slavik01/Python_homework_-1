# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму. (1 + 1 \ k) and k 



number = int(input("Введите число k: "))
summa = 0
for i in range(1,number+1):
    summa += (1+1/i)**i
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(summa,2)}")