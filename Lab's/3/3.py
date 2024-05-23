from math import sqrt
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))
с = [] # - список чтобы вывести числа как в задании

if x > 0:
    с.append(x) # - .append добавляет в конец списка число

if y > 0:
    с.append(y)

if z > 0:
    с.append(z)

print("Положительные числа:")
for number in с:
    print(number)

print("Количество положительных чисел:", len(с)) # - len(c) считает количество переменных в списке C