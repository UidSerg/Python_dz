# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# import random
# x = random.randint(0,1000)
# y = random.randint(0,1000)
# sum = x+y
# pow = x*y
# print (f'Подсказка: x+y = {sum}\n \t x*y = {pow}')
# # решим систему уравнений выразим x через y
# #x1= sum - y1
# #pow = (sum -y1) y1
# #y1^2-sum*y1+pow
# d=(sum)**2-4*1*pow
# y1=int((-1*sum +((sum)**2-4*1*pow)**0.5)/-2)
# x1= int(sum-y1)
# print (f'{x},{y}|{y1},{x1}')

x = int(input("Введите сумму чисел:"))
y = int(input("Произведение чисел:"))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(f"Загаданные цифры: {i}, {j}")