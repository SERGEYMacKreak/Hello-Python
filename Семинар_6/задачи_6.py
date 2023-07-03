'''''
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод:                          Вывод:
7                              3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)

'''
# array_length_1 = int(input("Ввидите количество элементов первого массива: "))
# list_1 = [] 
# # list_1 = [3, 1, 3, 4, 2, 4, 12] 
# print ('Введите эти элемены:')
# for i in range(array_length_1): 
#   n = int(input()) 
#   list_1.append(n)
# print () 
# print (*list_1)

# array_length_2 = int(input("Ввидите количество элементов второго массива: "))
# list_2 = [] 
# # list_2 = [4, 15, 43, 1, 15, 1] 
# print ('Введите эти элемены:')
# for i in range(array_length_2): 
#   n = int(input()) 
#   list_2.append(n) 
# print ()
# print (*list_2)

# list_3 = []
# for i in range(len(list_1)):
#   if list_1[i] not in list_2:
#       list_3.append(list_1[i])

# print (*list_3)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

'''''''''''
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве выведет количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 
Ввод: 			Ввод:
5				       5
1 2 3 4 5			1 5 1 5 1

Вывод:			Вывод:
0				    2

'''
# N = int(input('Введите N: '))
# print(N)
# li1 = [int(input('Введите число: ')) for _ in range(N)]
# print(*li1)
# cooint = 0
# for i in range(1, len(li1)-1):
#     if li1[i-1] < li1[i] > li1[i+1]:
#         cooint += 1
# print(cooint)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

'''''''''''
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел.
Все числа списка находятся на разных строках.
Ввод:			       Вывод:
1 2 3 2 3			      2

'''
# решение через словарь
# N = int(input('Введите N: '))
# print(N)
# li1 = [int(input('Введите число: ')) for i in range(N)]
# print(*li1)
# n = 0
# d = {}
# for i in li1:
#     if i in d:
#         n += d[i]
#     d[i] = d.get(i, 0) + 1 # если ключ повторяется счетчик +1

# print(n)


# import random
# n = int(input("введи размер списка1: "))
# list1 = []
# for i in range(n):
#     lis1 = random.randint(1, 10)
#     list1.append(lis1)
# print(*list1)
# count = 0
# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if list1[i] == list1[j]:
#             count += 1
# print(count)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

'''''''''''
Задача №45. Решение в группах
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n)
равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
Программа получает на вход одно натуральное число k, не превосходящее 105. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод:			Вывод:
300			     220 284

'''

# k = int(input())

# array = []

# for i in range(k): 
#     summ = 0
#     for j in range(1, i):
#         if i % j == 0:
#             summ += j
#     array.append([i,summ])
# #print(array)
        
# for i in range(1,len(array)):
#     for j in range(i + 1,len(array)):
#         b = array[i]
#         c = array[j]
#         if b[0] == c[1] and b[1] == c[0]:
#             print(b)