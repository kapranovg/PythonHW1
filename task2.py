"""Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
*** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного"""

number = int(input("Введите число: "))
summa = 0

while number > 0:
    summa = summa + number % 10
    number = number // 10

print(summa)