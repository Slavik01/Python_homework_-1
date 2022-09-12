# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.


n = 3
s = sum([[i for i in range(-n, n+1)][int(p)] for p in input().split()])
print(s)

n = 3
str_pos = input()
pos = [int(item) for item in 
str_pos.split()]

li = [i for i in range(-n, n+1)]

s = 0
for p in pos:
    s += li[p]
print(s)



# n = 3
# str_pos = input()
# pos = []
# for item in str_pos.split():
#     pos.append(int(item))

# li = []
# for i in range(-n, n+1):
#     li.append(i)
# s = 0
# for p in pos:
#     s += li[p]
# print(s)


# number = int(input('Введите N: '))
# # number_list = [number]
# for i in range(-number, number +1):
#     print(i)
# number_list = [i]

# position = input('Введите номера позиций: ').split()
# prod = 1
# a, b = (int(i) for i in position)
# for i in range(a,b):
#     prod *= number_list[i]
# print(prod)