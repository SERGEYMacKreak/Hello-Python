""""
ФУНКЦИИ 

Создаем функцию sumNumbers(n), которая будет считать
сумму всех элементов от 1 до n.

!!! БЕЗ ВОЗВРАЩЕНИИЯ ЗНАЧЕНИЯ

# def sumNumbers(n): # название фунукци, она принемает число n // если записать (*n) это неограниченное колличество аргументов
#   summa = 0
#   for i in range(1, n + 1):
#     summa += i
#     print(summa)

# n = int(input()) # 5 # ввод числа n
# sumNumbers(n) # 15 # обращение\вызов к функции sumNumbers(n)

!!! С ВОЗВРАЩЕНИИЕМ ЗНАЧЕНИЯ 

def sumNumbers(n):
  summa = 0
  for i in range(1, n + 1):
    summa += i
    return summa # мы просто добавили return!!!

n = int(input()) # 5
print(sumNumbers(n)) # 15

"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

""""
# МОДУЛЬНОСТЬ

# в отдельном файле мы можем создать функцию (смт. функция_function_file.py)

# import function_file # с помощью import "название файла" мы вызываем функциИ из другого файла
# 5
# print(function_file.f(1)) # Целое # тут мы обращаемся к ней закладавая целое число 
#   назв. файла (function_file) и название функции (.f(1))
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None

# from function_file import f # если функций несколько либо мы не хотим постоянно прописывать название файла 
# 5
# print(f(1)) # Целое # тут мы обращаемся к ней закладавая целое число 
#   название функции (f(1))

# from function_file import* # c помощью этой строчки мы можем обращатся ко всем функциям в файле

"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

""""
# РЕКУРСИЯ
При описании рекурсии важно указать, когда функции надо остановиться и перестать вызывать саму себя. 
По-другому говоря, необходимо указать базис рекурсии

def fib(n):
  if n in [1, 2]: #базис рекурсии иначе она будет работать бесконечно
    return 1
  return fib(n - 1) + fib(n - 2)  

list_1 = []
for i in range(1, 10):
  list_1.append(fib(i - 2)) 
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

"""


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

""""
# АЛГОРИТМЫ


                    ● Быстрая сортировка (через рекурсию)

def quick_sort(array):
  if len(array) < 2: #проверка массива на длинну ана же базис рекурсии
    return array
  else:
    pivot = array[0] #сохраняем первый элемент от коророго отталкиваемся при начале сортировки
    less = [i for i in array[1:] if i <= pivot] #сохраняем элементы которые меньше первого элемента (pivot = array[0])
    greater = [i for i in array[1:] if i > pivot] #сохраняем элементы которые больше первого элемента (pivot = array[0])
    return quicksort(less) + [pivot] + quicksort(greater) #рекурсия которые сразу сортирут less и greater
print(quicksort([10, 5, 2, 3])) #вывод массива с обращение к функции (массив задан)

● 1-е повторение рекурсии:
    ○ array = [10, 5, 2, 3]
    ○ pivot = 10
    ○ less = [5, 2, 3]
    ○ greater = []
    ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
● 2-е повторение рекурсии:
    ○ array = [5, 2, 3]
    ○ pivot = 5
    ○ less = [2, 3]
    ○ greater = []
    ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что здесь помимо вызова рекурсии добавляется список [10]
● 3-е повторение рекурсии:
    ○ array = [2, 3]
    ○ return [2, 3] # Сработал базовый случай рекурсии и функция останавливается !!!!!!!!!
На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]



                 ● Сортировка слиянием (через рекурсию)

def merge_sort(nums):
  if len(nums) > 1: # проверка длинны 
    mid = len(nums) // 2 # делим массив на пополам
    left = nums[:mid] # левая часть массива
    right = nums[mid:] # правая часть массива 
    merge_sort(left) # рекурсия для левой части
    merge_sort(right) # рекурсия для правой части
    i = j = k = 0 # создаем три переменые

    while i < len(left) and j < len(right): # сам процесс сортировки
      if left[i] < right[j]:
        nums[k] = left[i]
        i += 1
      else:
        nums[k] = right[j]
        j += 1
      k += 1

    while i < len(left): # заглушка на случай если ЛЕВАЯ часть массива больше чем правая
      nums[k] = left[i]
      i += 1
      k += 1

    while j < len(right): # заглушка на случай если ПРАВАЯ часть массива больше
      nums[k] = right[j]
      j += 1
      k += 1

nums = [38, 27, 43, 3, 9, 82, 10] # массив
merge_sort(nums)# вызов функции сортировки
print(nums)

"""