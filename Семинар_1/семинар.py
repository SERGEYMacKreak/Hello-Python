# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# import math
# n = int(input('Введите км '))
# m = int(input('Введите кол-во км за день '))

# print(math.ceil (n / m))

# /////////////////////////////////////////////////////////////////////////////

# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть два учащихся. Известно 
# количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# import math
# first_class = 20
# second_class = 21
# third_class = 22

# table = 2

# all_students = first_class + second_class + third_class
# count_tables_first = first_class // table + first_class % table
# count_tables_second = math.ceil(second_class / table)
# count_tables_third = math.ceil(third_class / table)

# all_count = count_tables_first + count_tables_second + count_tables_third
# print(all_count)


# /////////////////////////////////////////////////////////////////////////////


# Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
#  это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, 
# сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без 
# дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = 3
# j = 4

# if(i == j):
#     print('Введите дополнительное условие')
# else:
#     print('Кол-во вагонов = ' + str(i + j - 1))


# /////////////////////////////////////////////////////////////////////////////


# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с 
# григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а 
# также если он кратен 400.
# Input: 2016
# Output: YES

# year = 2015

# if(year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')
