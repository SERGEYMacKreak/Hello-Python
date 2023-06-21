# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
# import random
# array_length = int (input('Какой длинны будет массив?: '))
# list_1 = [random.randint(1,9) for _ in range(array_length)]
# print("получается вот такой массив:")
# print(*list_1)    
# number = int (input('Какое число от 1 до 9 вы хотите найти?: '))
# if (number > 10) or (number < 1):
#   print("Ввели неверное число!")
# else:
#   counter = 0
#   for i in range(len(list_1)):
#     if number == list_1[i]:
#       counter += 1
#   print(f"Число {number} встречается в массиве {counter} раз")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
# import random
# array_length = int (input('Какой длинны будет массив?: '))
# list_1 = [random.randint(1,99) for _ in range(array_length)]
# print("получается вот такой массив:")
# print(*list_1)    
# number = int (input('Введите число от 1 до 99: '))
# i_max, i_min, close_number  = 100, 0, 0

# if (number > 99) or (number < 1):   # ПРОВЕРКА
#   print("Ввели неверное число!")
# else:
#   for i in range(len(list_1)):  # ИЩЕМ МАКСИМАЛЬНО БЛИЗКИЕ ЭЛЕМЕНТЫ МАССИВА
#     if list_1[i] > number:
#       if i_max > list_1[i]:
#         i_max = list_1[i]
#     if list_1[i] < number:
#       if i_min < list_1[i]:
#         i_min = list_1[i]

# if (number - i_min) > (i_max - number): # ОПРЕДЕЛЯЕМ КАКОЙ ИЗ НИХ БЛИЖЕ
#   close_number = i_max
# else: close_number = i_min

# print(f"К Числу {number} ближе всего элемент {close_number}")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\