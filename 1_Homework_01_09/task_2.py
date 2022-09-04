# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ¬ -> not
# ⋁ -> or
# ⋀ -> and
# =>
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z <=> not(X or Y or Z) = (not X) and (not Y) and (not Z)


x = input("Введите значение x: ")
y = input("Введите значение y: ")
z = input("Введите значение z: ")

a = not (x or y or z)
b = not x and not y and not z

if a == b:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")