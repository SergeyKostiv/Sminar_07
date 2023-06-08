# def sq1(x):
#     print(x ** 2)
#
#
# print(sq1(10))
#
# def sq2(x):
#     return x ** 2
#
#
# print(sq2(20))

# def c(x):
#     return x ** 3
#
#
# some_list = [1, 2, 3, 4, 5]
#
# new_list = []
#
# for el in some_list:
#     new_list.append(c(el))
#
# print(new_list)


# def c(x):
#     return x ** 3


# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, some_list))
# print(new_list)

# def even(a):
#     return a % 2 == 0


# some_list = [1, 2, 3, 4, 5]

# new_list = list(filter(lambda a: a % 2 == 0, some_list))
# print(new_list)


# import random
#
# some_list = []
# for _ in range(100):  # 0, 1, 2, 3, 4, 5, 6, 7... 99
#     number = random.randint(1, 10)
#     if number % 2 == 0:
#         some_list.append(number)
#
#
# some_list = [random.randint(1, 10) for _ in range(100)]
#
# some_list = [int(input()) for _ in range(int(input()))]

# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# transformation = lambda z : z
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(ransormed_values)


# Задача №49. Общее обсуждение
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def s(x):
#     if x[0] == x[1]:
#         return 0
#     return x[0] * x[1]

# mult = list(map(s, orbits))
# print(mult)
# maxx = mult.index(max(mult))
# print(orbits[maxx])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(list(filter(lambda y: y[0] * y[1] == max(list(map(lambda x: x[0] * x[1] if x[0] != x[1] else 0, orbits))), orbits))[0])


# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(objects) == len(new_objects) or len(new_objects) == 0:
#         return True
#     return False

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')