# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Input 7 2 5
# Ounput 7 9 11 13 15

first_namber = int(input("Введите первый член арифметической прогрессии:"))
razn = int(input("Введите разность арифметической прогрессии:"))
count = int(input("Введите количество членов арифметической прогрессии:")) 

result = list()
for i in range(count):
    result.append(first_namber+razn*i)
print(result)

# эталонное решение
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d) # Ну да можно и сразу печать)