# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print("Введите число сделанных журавливков:")
birds = int(input())  # bird = (S+P)*2+S+P=3S+3P=6S
if birds % 6 != 0:
    print("Не возможно посчитать!")
else:
    serg = int(birds/6)
    petr = serg
    katya = 2*(serg+petr)
    print(f"Катя сделала {katya} журавликов, Сергей и Петя по {serg} журавликов")