#import test_file
#Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом (в зависимости
# от переданных аргументов) она должна вести себя так:
#matrix() — возвращает матрицу 1× 1, в которой единственное число равно нулю;
# matrix(n) — возвращает матрицу n×n, заполненную нулями;
# matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
# matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый элемент равен числу value
#import numpy as np
# def matrix(row = 1, col = None, value = 0):
#     mat = [[value for j in range((row if not col else col))] for i in range(row)]
#     return mat

# Напишите функцию count_args(), которая принимает произвольное количество аргументов и возвращает количество переданных
# в нее аргументов.

# def count_args(*args):
#     return len(args)

#Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.

# def sq_sum(*args):
#     return sum([num**2 for num in args])

#Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое
# переданных в нее числовых (int или float) аргументов.

# def mean(*args):
#     ls = [num for num in args if type(num) in (float, int)]
#     return sum(ls)/(len(ls) if len(ls) != 0 else 1)

#Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и
# возвращает приветствие в соответствии с образцом.

# def greet(name, *args):
#     # if len(args) < 1:
#     #     return 'Hello, ' + name + '!'
#     # else:
#     return 'Hello, ' + ' and '.join((name, *args)) + '!'
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

#========Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список
# продуктов (любая непустая строка) по образцу: <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы).
# Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.
# import string
# def print_products(*args):
#     count = 0
#     for elem in args:
#         if type(elem) is str and elem not in (string.punctuation + ' '):
#             count += 1
#             print(f'{count}) {elem}')
#     if count == 0:
#         print('Нет продуктов')

#==Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает
# именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов
# следуют в алфавитном порядке (по возрастанию).

# def info_kwargs(**kwargs):
#    # sort_kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))
#    # for key, val in sort_kwargs.items():
#    #     print(f'{key}: {val}')
#
#    for key, val in sorted(kwargs.items()):
#        print(f'{key}: {val}')
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

#Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max()
# выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое значение элементов.

# import statistics  # для вызова mean - средне арифмитического
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# # def middle_arifm(elem):
# #     return sum(elem)/len(elem)
# #
# # print(min(numbers, key=middle_arifm), max(numbers, key=middle_arifm), sep='\n')
# print(*(func(numbers, key=statistics.mean) for func in (min, max)), sep='\n') # перебор и подстановка ф-ий min и max в кортеже

#==Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала
# координат. Программа должна вывести отсортированный список.

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# points.sort(key=lambda x: (x[0]**2 + x[1]**2)**0.5)
#
# print(points)

#===Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует и выводит список numbers в
# соответствии с суммой минимального и максимального элемента кортежа.

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
#            (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# numbers.sort(key=lambda x: min(x) + max(x))
#
# print(numbers)

#===Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
# Напишите программу сортировки списка спортсменов по указанному полю:
# 1: по имени;
# 2: по возрасту;
# 3: по росту;
# 4: по весу.

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# sort_by = int(input()) - 1
# athletes.sort(key=lambda x: x[sort_by])
#
# [print(*data) for data in athletes]

#==Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.
# Список возможных функций:
# квадрат: функция принимает число и возвращает его квадрат;
# куб: функция принимает число и возвращает его куб;
# корень: функция принимает число и возвращает корень квадратный из этого числа;
# модуль: функция принимает число и возвращает его модуль;
# синус: функция принимает число (в радианах) и возвращает синус этого числа.

# from math import sin
# n, command = int(input()), input()
#
# # def func(num, command):
# #     func_dict = {'квадрат': num**2, 'куб': num**3, 'корень': num**0.5, 'модуль': abs(num),
# #                  'синус': sin(num)}
# #     return func_dict[command]
# #
# # print(func(n, command))
#
# func_dict = {'квадрат': lambda x: x**2, 'куб': lambda x: x**3, 'корень': lambda x: x**0.5,
#          'модуль': abs, 'синус': lambda x: sin(x)}
#
# print(func_dict[command](n))

#====На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
#Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если два числа имеют
# одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.

# ls = [list(map(int, el)) for el in input().split()]
# ls.sort(key=lambda x: sum(x))
# for val in ls:
#     print(*val, sep='', end=' ')

#=Интересная сортировка-2. На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел одинаковая
# сумма цифр, их следует вывести в порядке неубывания.

# ls = [int(el) for el in input().split()]
# ls.sort()
# ls.sort(key=lambda x: sum([int(sym) for sym in str(x)]))
# for val in ls:
#     print(val, sep='', end=' ')

#==Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков,
# а затем выводит их, каждый на отдельной строке.

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# # def rnd(arg):
# #     return round(arg, 2)
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# print(*map(lambda x: round(x, 2), numbers), sep='\n')

#===Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные
# числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке.

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def is_dev2(arg):
#     return len(str(arg)) == 3 and arg % 5 == 2
#
#
# def cube(arg):
#     return arg**3
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# print(*map(cube, filter(is_dev2, numbers)), sep='\n')

#====Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers. Решите задачу двумя способами:
# с помощью функции reduce(), и с помощью функций map() и sum().

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
#            72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
#            7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# print(reduce(lambda x, y: x+y**2, numbers, 0))
# print(sum(map(lambda x: x**2, numbers)))

#====Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 7 без остатка.


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def is_two_digit(item):
#     return len(str(abs(item))) == 2 and item % 7 == 0
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
#            152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
#            187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
#            79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# print(sum(map(lambda x: x**2, filter(is_two_digit, numbers))))

#==Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список, в котором каждое
# значение будет результатом применения переданной функции к переданному списку.

# def func_apply(func, items):
#     # result = []
#     # for item in items:
#     #     val = func(item)
#     #     result.append(val)
#     # return result
#     return [func(item) for item in items]

#===== test - замыкание

# def generator_square_polynom(a, b, c):
#     return lambda x: a*x**2 + b*x + c
#
# print(generator_square_polynom(2,3,1)(0))
#
#======================================
# from functools import reduce
#
# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = filter(lambda x: x % 2 == 1, obj)
# result = reduce(lambda x, y: x + y, obj, 0)
#
# print(result)

#===Требовалось написать программу, которая:
# преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
# фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
# находит произведение чисел из списка numbers.

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

#==Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном
# порядке список primary городов с населением более 10,000,000 человек, в формате:
# Cities: Beijing, Buenos Aires, ...

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# filtered_data = filter(lambda x: x[1] > 10**7 and x[2] in 'primary', data)
# sort_data = sorted(filtered_data, key=lambda x: x[0])
# map_data = map(lambda x: x[0], sort_data)
#
# print('Cities:', reduce(lambda x, y: f'{x}, {y}', map_data))

#==Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает
# значение True, если он делится без остатка на 19 или на 13 и False в противном случае.

# func = lambda arg: True if arg % 19 == 0 or arg % 13 == 0 else False

#==Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
# значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен)
# и False в противном случае.

# #func = lambda w: True if (w[0].lower() + w[-1].lower()) == 'aa' else False
# func = lambda w: w[0].lower().endswith('a') and w[0].lower().startswith('a')
#
# print(func('XcdA'))

#===Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент
# и возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным) и False в противном случае.

# is_non_negative_num = lambda arg: arg.replace('.','',1).isdigit()
#
#
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

#===Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
# значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.

# is_num = lambda arg: arg.replace('.','',1).replace('-','',1).isdigit() and '-' not in arg[1:]
#
# print(is_num('11-1'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

#==Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все нечетные
# элементы, большие 47, а все четные элементы нацело делит на два (целочисленное деление – //). Полученные числа следует
# вывести на одной строке, разделив символом пробела и сохранив исходный порядок.

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
#            53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
#            37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# filtred_numbers = filter(lambda x: not (x % 2 != 0 and x > 47), numbers)
# print(*list(map(lambda x: x//2 if x % 2 == 0 else x, filtred_numbers)))

#==Список data содержит информацию о численности населения некоторых штатов США. Напишите программу сортировки по
# убыванию списка data на основании последнего символа в названии штата. Затем распечатайте элементы этого списка,
# каждый на новой строке в формате:
#
# <название штата>: <численность населения>
#
# Vermont: 626299
# Massachusetts: 7029917
#
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'),
#         (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'),
#         (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# sorted_data = sorted(data, key=lambda state: state[1][-1], reverse=True)
# [print(f'{state}: {popl}') for popl, state in sorted_data]

#==Список data содержит слова на русском языке. Напишите программу его сортировки по возрастанию длины слов, а затем в
# лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела.
#
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
#         'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
#         'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# # data.sort()
# # print(*sorted(data, key=lambda x: len(x)))
#
# print(*sorted(data, key=lambda x: (len(x), x)))

#==Список mixed_list содержит целочисленные и строковые значения. Напишите программу, которая с помощью встроенной
# функции max() находит и выводит наибольшее числовое значение в указанном списке.
#
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
#               2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
#               'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
#               'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
#               859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
#               'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
#               'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022,
#               'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# print(max(mixed_list, key=lambda x: x if type(x) is int else 0))

#===Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию
# значений элементов, при этом числа должны следовать до строк.  Элементы отсортированного списка выведите на одной
# строке, разделив символом пробела.
#
# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
#               70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
#               13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
#               'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
#               'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
#               'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))

#==В цветовой схеме RGB цвета задаются с помощью трех компонентов:
#
# R — интенсивность красной составляющей цвета;
# G — интенсивность зеленой составляющей цвета;
# B — интенсивность синей составляющей цвета.
# Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). Считается, что такие цвета хорошо гармонируют друг с другом.
#
# Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета.
#
# print(*list(map(lambda x: 255-int(x), input().split())))

#==Многочленом степени nn называется выражение вида
#==На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число x
# на второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.
# from functools import reduce
# import operator
# def evaluate(coefficients, x):
#     # n = len(coefficients)
#     # coefficients = map(int, coefficients)
#     # ls = list(map(pow, [x]*n, range(n-1, -1, -1)))
#     # ls2 = list(map(operator.mul, coefficients, ls))
#     # return reduce(lambda num1, num2: num1 + num2, ls2)
#     return reduce(lambda c1, c2: c1*x + c2, map(int, coefficients))
#
# print(evaluate(input().split(), int(input())))

#===
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# result = 0
# for x, y in zip(list1, list2):
#     result += x*y
# print(result)

#=Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
#и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.
# #
#
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#
#     return any(map(lambda x: x in command, ignore))

# Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране в формате:
#
# <capital> is the capital of <country>, population equal <population> people.
#
#
# Moscow is the capital of Russia, population equal 145934462 people.
# New York is the capital of USA, population equal 331002651 people.
# ...

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# [print(f'{cap} is the capital of {coun_s}, population equal {popul} people.') for coun_s, cap, popul in zip(countries, capitals, population)]

#На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) и аппликат
# (z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными координатами
# внутри либо на поверхности шара с центром в начале координат и радиусом R =2.
import test_file
# abscissas = [float(num) for num in input().split()]
# ordinates = [float(num) for num in input().split()]
# applicates = [float(num) for num in input().split()]
#
# # ls = [x**2+y**2+z**2 for x, y, z in zip(abscissas, ordinates, applicates)]
# # print(all(map(lambda x: x <= 4.0, ls)))
#
# print(all(x**2+y**2+z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))

#==IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP.
# В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел
# (октетов) со значением от 0 до 255 (включительно), разделённых точками, например, 192.168.1.2.
# # Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в
# IP-адресе – числа со значением от 0 до 255.

# print(all(list(map(lambda x: x.isdigit() and int(x) <= 255, input().split('.')))))
# print(all(x.isdigit() and int(x) <= 255 for x in input().split('.')))

#==На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции
# all() для обнаружения всех целых чисел в диапазоне [a;b], которые делятся на каждую содержащуюся в них
# цифру  без остатка.
# import test_file
# a, b = int(input()), int(input())
# # def prepare_list(x):
# #     list_x = list(str(x)) #all(map(int, list(str(x))))
# #     flag = False
# #     for i in range(len(list_x)):
# #         if list_x[i] != '0' and x % int(list_x[i]) == 0:
# #             flag = True
# #         else:
# #             flag = False
# #             break
# #     return x if flag else 0
# #
# # print(*list(filter(lambda x: x !=0 , map(prepare_list, range(a, b + 1)))))
#
# def isTrue(num):
#     return all(map(lambda x: int(x) and num % int(x) == 0, str(num))) # При х = "0" int("0") вернет 0 (False) и дальше проверка условия num % int(x) == 0 не будет проводиться.
#
# print(*filter(isTrue, range(a, b + 1)))

#==Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру,
# заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

# import test_file
#
# def isTrue(pwrd):
#     if len(pwrd) < 7:
#         return False
#     else:
#         upper = any(map(lambda x: x.isupper(), pwrd))
#         lower = any(map(lambda x: x.islower(), pwrd))
#         digit = any(map(lambda x: x.isdigit(), pwrd))
#     return all(upper, lower, digit)
#
# print('YES' if isTrue(input()) else 'NO')

#==Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться,
# что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе. Напишите программу с
# использованием встроенных функций all(), any() для помощи Тимуру в проверке.

# class_list = [[input().split() for __ in range(int(input()))] for _ in range(int(input()))]
# ls = [any(map(lambda x: x[1] == '5', class_)) for class_ in class_list]
# print('YES' if all(ls) else 'NO')

#===== ИТОГОВАЯ ПО ФУНКЦИЯМ============================================================================================

#==1==
#Напишите функцию generate_letter(), которая будет собирать электронное письмо в соответствии с шаблоном:

# To: <mail>
# Приветствую, <name>!
# Вам назначен экзамен, который пройдет <date>, в <time>.
# По адресу: <place>.
# Экзамен будет проводить <teacher> в кабинете <number>.
# Желаем удачи на экзамене!

# Функция должна получать на вход пять обязательных аргументов mail, name, date, time, place и два необязательных
# teacher, number и возвращать текст готового письма. При отсутствии аргумента teacher учителем будет Тимур Гуев, а
# если нет аргумента number, то кабинет будет 17.
#
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number='17'):
#     return f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!'''
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

#===2===
#Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.
#
# Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных
# строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.
# В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем
# delimiter='|'.
# def make_side(data, side):
#     side_ls = [side * (len(str(el)) + 2) for el in data]
#     return f' {side.join(side_ls)}'
#
# def pretty_print(data, side='-', delimiter='|'):
#     delimiter = f' {delimiter} '
#     print(make_side(data, side))
#     print(f'{delimiter}{delimiter.join(map(str, data))}{delimiter}'.lstrip())
#     print(make_side(data, side))
#
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

#=====4=======
#Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через
# разделитель (sep). Если разделитель не задан, им служит пробел.

# def concat(*args, sep=' '):
#     return sep.join(map(str,args))
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

#=======5========

#Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

# # def product_of_odds(data):   # data - список целых чисел
# #     result = 1
# #     for i in data:
# #         if i % 2 == 1:
# #             result *= i
# #     return result
# from functools import reduce
# from operator import mul
#
# def product_of_odds(data):
#     return reduce(mul, filter(lambda i: i % 2, data), 1)
# ls = []
# print(product_of_odds(ls))

#=======6=========
#Дан список слов words. Допишите код после оператора распаковки (*), который оборачивает в двойные кавычки все элементы
# списка words, а затем печатает результат на одной строке через пробел.

# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: f'"{x}"', words))

#====7=======

#Дан список целых чисел numbers. Допишите код после оператора распаковки (*), для удаления из списка всех чисел-палиндромов
# и печати результата на одной строке через пробел.

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

#=======8======

#Дан список numbers, состоящий из кортежей. Допишите пропущенную часть программы, чтобы список sorted_numbers был
# упорядочен по убыванию среднего арифметического элементов кортежей списка numbers.

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
#            (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
#
# print(sorted_numbers)

#======9========

#Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной функции,
# возвращая ее значение.


# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# def call(func, *args):
#     return func(*args)
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))

#====10=======================

#Напишите функцию compose(), которая принимает на вход две других одноаргументных функции f и g и возвращает новую
# функцию. Эта новая функция также должна принимать один аргумент x и применять к нему исходные функции в нужном
# порядке: для функций f и g порядок применения должен выглядеть, как f(g(x)).

# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def compose(f, g):
#     return lambda x: f(g(x))
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

#========11==================

#Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *, /)
# и возвращает функцию двух аргументов для соответствующей операции.
# import operator
# def arithmetic_operation(operation):
#     operation_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
#     return operation_dict[operation]
#
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

#=============12====================

#Дана строка из разделенных пробелами слов в разных регистрах. Напишите программу, которая отсортирует слова независимо
# от регистра, а затем выведет их. Отсортированные слова должны выводиться на печать в исходном регистре, в каком
# переданы программе на вход.

# import test_file
# print(*sorted(input().split(), key=lambda x: x.upper()))

#============13======================

#Гематрией слова называется сумма числовых значений входящих в него букв.
# Для вычисления гематрии слова в этой задаче:
#
# переведём слово в верхний регистр;
# числовое значение буквы вычислим как " код(буквы) минус код(буквы A) ".
# На вход программе подается натуральное число n, а затем n строк английских слов в разных регистрах.
#
# Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке) в порядке возрастания их
# гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.
# from functools import reduce
# from operator import add
# import test_file
# def summ_letter(word):
#     ls1 = reduce(add, map(lambda x: ord(x.upper()) - ord('A'), word))
#     return ls1
#
# ls = [input() for _ in range(int(input()))]
# ls.sort()
# print(*sorted(ls, key=lambda x: summ_letter(x)), sep='\n')

# def summ_letter(word):
#     return sum(map(lambda x: ord(x.upper()) - ord('A'), word)), word
#
# ls = [input() for _ in range(int(input()))]
# print(*sorted(ls, key=summ_letter), sep='\n')

#========14=================
#IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.

# В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел
# (октетов) со значением от 0 до 255, разделённых точками, например, 192.168.1.2
#
# Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии с десятичным представлением.

ip_ls = [list(map(int, input().split('.'))) for _ in range(int(input()))]
# def dec(num):
#     return num[0]*256**3 + num[1]*256**2 + num[2]*256**1 + num[3]*256**0
[print('.'.join(map(str,num))) for num in sorted(ip_ls, key=lambda x: x[0]*256**3 + x[1]*256**2 + x[2]*256**1 + x[3]*256**0)]

# print(*sorted(ip_ls, key=dec), sep='\n')]

