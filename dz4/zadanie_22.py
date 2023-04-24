# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
import math
n = int(input("Введите число элеменнов массива 1: \t"))
m = int(input("Введите число элеменнов массива 2: \t"))
massiv1 = list()
massiv2 = list()
for i in range(n):
    elemen = int(input(f"Введите {i+1}: элемент массива 1 \t"))
    massiv1.append(elemen)
for i in range(m):
    elemen = int(input(f"Введите {i+1}: элемент массива 2 \t"))
    massiv2.append(elemen)
print(massiv1)
print(massiv2)
result = {}
result = set(massiv1).intersection(set(massiv2))
print(sorted(result))