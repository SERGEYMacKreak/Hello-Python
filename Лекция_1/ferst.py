# n = 5 \\ аналог int в С#, если надол рисвоить пустое значение пишим "None"
# print(n)

# n = 1.89 \\ аналог dooble в С#
# print(n)

# n = 'привет' \\ аналог string в С#
# n = "привет"
# n = 'привет"мир"' \\ если нам надо вывести несколько типов даных внутри используем ковычки
# print(n)

# print(type(n)) \\ выводит тип используемых данных


# a = 5
# b = 5.45
# c = "Привет"
# print(a, ' - ', b, ' - ', c) вывод нескольких данных в строке
# print(a, b, c) 
# print(f"{a} - {b} - {c}") 
# print("{} - {} - {}".format(a,b,c)) 

# print('введите значение: ')
# a = input() # ввод даннх через консоль 
# a = int(a) # приведенние данных к нужному типу
# b = int (input('введите значение два: ')) # сразу перевод данных в нужный нам формат
# print(a, ' + ', b, ' = ', a + b) # сложение данных

# a = 7.878777
# b = 8.45454
# print(round(a*b, 3)) # функция round сокращает ввыодимое чило на количество узазанное после запятой


# username = input('Введите имя: ') # Ещё один вариант использования операторов else-if → в связке с elif (else if)
# if username == 'Маша':
#   print('Ура, это же МАША!')
# elif username == 'Марина':
#   print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#   print('Ильнар - топ)')
# else:
#   print('Привет, ', username)

# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9


# i = 0
# while i < 5:
#   if i == 3:
#     break
#   i = i + 1
# else:
#   print('Пожалуй')
#   print('хватит )')
# print(i)


# for i in 1, -2, 3, 14, 5: #ПРИНЦИП РАБОТЫ ЦИКЛА for где i это перебор массива
# print(i)
# # 1 -2 3 15 5


# Range ФУНКЦИЯ
# ● Range выдает значения из диапазона с шагом 1.
# ● Если указано только одно число — от 0 до заданного числа.
# ● Если нужен другой шаг, третьим аргументов можно задать приращение.
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# ПРИМЕР 
# for i in r:
#   print(i)
#   # 100 80 60 40 20
# for i in range(5):
#   print(i)
#   # 0 1 2 3 4


# a = 'qwerty'
# print[0] # вывод конкретной позиции 
# for i in 'qwerty':
#   print(i) # вывод всех позиций построчно спомощью цикла
# # q
# # w
# # e
# # r
# # t
# # y


# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39 \\Определить количество символов в строке
# print('ещё' in text) # True \\Проверить наличие символа в строке (in)
# print(text.lower()) # съешь ещё этих мягких французских булок \\Функция, которая делает все буквы строки маленькими
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК \\Функция, которая делает все буквы строки большими
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок \\Заменить слово на другое



# Срезы ФУНКЦИИ
# ● Мы представляем строку в виде массива символов. Значит мы можем
# обращаться к элементам по индексам.
# ● Отрицательное число в индексе — счёт с конца строки
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
