# Задача 2: Найдите сумму цифр трехзначного числа.

print("Введите 3х значное число:")
value = int(input())
result = 0
while value / 10 > 0:
    result += value % 10
    value = int(value / 10)
print(f"Cумму цифр трехзначного числа = {result} ")
