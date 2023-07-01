"""""
Задача №31. Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak  = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""""

# def fibonach(N):
#     if(N <= 1):  # !!! в С# if(n == 1 || n == 2) return 1;
#         return 1
#     return fibonach(N-1) + fibonach(N-2)

# N = int(input("Введите номер числа которое вас интересует: "))
# if (N <= 0):
#     print("Ввели не верный номер!")
# else:
#     print (f"  Это чило: {fibonach(N)}")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""""
Задача №33. Общее обсуждение
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки
на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот:
все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""""
# import random 

# def replacement (arr): # функция которая меняет высокие оценки на низкие в случ.порядке
#     for i in range(a):
#         if arr [i] > 3:
#             arr [i] = random.randint(1,3)

# a = int(input("Сколько всего оценок?: "))
# arr = [random.randint(1,5) for i in range(a)] # вызываю функцию питона рандомные номера
# print()
# print("Они выгледят вот так:")
# print(*arr)
# print()
# print("Заменим их на такие:")
# replacement(arr)
# print(*arr)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""""
Задача №35. Общее обсуждение
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""""

# def check (nomber):
#     j = 0
#     if (nomber == 2) or (nomber == 3):
#         return print("Число простое")
#     if (nomber % 2 == 0) or (nomber < 2):
#         return print("Число не является простым")
#     for i in range(3, int (nomber ** 0.5) + 1, 2):
#             if (nomber % i == 0):
#                 return print("Число не является простым")
#     return print("Число простое")

# nomber = int(input("Введите число: "))
# check(nomber)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""""
Задача №37. 
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""""
# def d (nomber):
#     if (nomber > 0):
#         return (nomber + d(nomber - 1))
#     return 0

# def dddddd (list_2):
#     if not list_2:
#         return []
#     return [list_2.pop()] + dddddd(list_2)

# nomber = int(input("Введите число: "))

# # list_2 = int(input("Введите список чисел, разделенных запятой: "))
# list_2 = [3, 4, 5, 6, 7]
# # print (*list_2)
# dddddd(list_2)
# print (*list_2)