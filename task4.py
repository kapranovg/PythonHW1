"""Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
******Рассмотрите вариант, что он также делают журавлики в момент подсчета 
и известно только число уже полностью готовых"""

S = int(input("Введите количество корабликов: "))

petya_ship = serezha_ship = S // 6
katya_ship = (petya_ship + serezha_ship) * 2

print(f"Петя сделал {petya_ship} кораблей, Сережа сделал {serezha_ship} кораблей, Катя сделала {katya_ship} кораблей,")

