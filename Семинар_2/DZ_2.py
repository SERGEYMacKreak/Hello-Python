# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# import array as arr
# import random
# sum = int (input('Сколько монеток лежит на столе?: '))
# total_coins = [random.randint(0,1) for _ in range(sum)]
# print(f"это выгледит вот так: {total_coins}")
# i = 0
# con = 0
# while i < sum:
#   if total_coins[i] == 0:
#     con += 1
#     i += 1
#   else:
#     i += 1 
# print(f"нужно перевернуть {con} монеток")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# S = int (input('Введите сумму чисел: '))
# P = int (input('Введите произведение чисел: '))

# for i in range(S):
#   for y in range(P):
#     if S == i + y and P == i * y:
#       print(f"Петя задумал числа {i} и {y}")
#       break


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# nomber = int (input('Введите число: '))
# i = 1
# print(i)
# while i < nomber:
#   if(i < nomber):
#     if (i * 2 > nomber):
#       break
#     else:
#       i = i * 2
#       print(i)
# ВЕРНОЕ
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1