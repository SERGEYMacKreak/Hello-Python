#  Функции высшего порядка, работа с файлами

# - Анонимные, lambda-функции:

# придание переменной тип функции
# Теперь в контексте этого приложения g может использоваться точно так же, как и f.
# g — это переменная, которая хранит в себе ссылку на функцию.
# def f(x) # <- функция
#   return x ** 2
# g = f # <- придание переменной тип функции
# print(f(4)) # 16
# print(g(4)) # 16

# В Python есть механизм, который позволяет превратить подобный вызов во что-то
# более красивое — "lambda".
# def sum(x, y): # <- функция     ⇔         sum = lambda x, y: x + y   # <- запись этой же функция через "lambda", 
#   return x + y              (равносильно)                                   где : разделитель слево от которого переменные,
#                                                                              а справо то что мы с ними планируем делать
# Теперь, чтобы вызвать функцию суммы, достаточно просто вызвать sum.
# Также можно пропустить шаг создания переменной sum и сразу вызвать lambda:
# calc(lambda x, y: x + y, 4, 5) # 9
# print((lambda x: x)(5)) сразу вывод функции

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ФУНКЦИЯ map()

# 💡 Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами.

# def f(x) # <- функция которая прибовляет 10 к числу
#   return x + 10
# map(f, [1, 2, 3, 4, 5])
# map(f, [11, 12, 13, 14, 15]) 

# list_1 = [x for x in range (1,20)]
# list_1 = list(map(lambda x: x + 10, list_1 )) 
# print(list_1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ФУНКЦИЯ filter()

# 💡 Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итератор с теми объектами, для которых функция вернула True.

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data)))
# print(res) # [0, 2, 4, 6, 8]

# Как в данном случае работает функция filter()? Все данные, которые находятся внутри проходят через функцию, которая указана следующим образом:
# lambda x: x % 2 == 0

# То есть делает проверка на те числа, которые при делении на 2 дают в остатке 0.
# Тем самым мы ищем только четные числа. Действительно преобразовав наши итоговые данные в список, с помощью функции list(),
# мы с Вами можем наблюдать такой красивый результат 🙂

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ФУНКЦИЯ zip()

# 💡 Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных

# На выходе получаем набор данных, состоящий из элементов соответствующих исходному набору. Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333] # этот список как самый короткий выступит ограничителем
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ФУНКЦИЯ enumerate()

# 💡 Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных.

# Функция enumerate() позволяет пронумеровать набор данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
