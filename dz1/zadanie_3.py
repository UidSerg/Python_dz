# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
print('Введите номер билета:')
bilet = int(input())
bil = int(bilet / 1000)
let = int(bilet % 1000)
sum_bil = 0
sum_let = 0
while bil / 10 > 0:
    sum_bil += bil % 10
    bil = int(bil / 10)
while let / 10 > 0:
    sum_let += let % 10
    let = int(let / 10)
if sum_bil == sum_let:
    print('УРА,Ура, счастливый билет!!!:)))')
else:
    print('Печалька, билет не счастливый:(')