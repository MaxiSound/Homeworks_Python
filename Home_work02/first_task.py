# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input('Введите число: \n')
sum = 0

for a in n:
    if a.isdigit():
        sum += int(a)

print(sum)