# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A.
# . Последняя строка содержит число X
#  Если таких значений больше одного, вывести первый найденный.

# Input: число N = 5
#     массив 1 2 3 4 5
#     число x = 6
# Output: 5

import random
import math

n = int(input("Введите число элеменнов массива: \n"))
chek = int(input("Введите число: \n"))
massiv = list()
for i in range(n):
    massiv.insert(i, random.randint(0, 100))
print(massiv)
max_value = min(massiv) 
if max(massiv) < chek:
    print(f"Самый близкий по величине элемент {max(massiv)}")
else:
    for i in range(n):
        if abs(chek-massiv[i]) < abs(chek-max_value):
            max_value = massiv[i]
    print(f"Самый близкий по величине элемент {max_value}")
