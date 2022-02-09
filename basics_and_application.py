# print(sum([int(input()) for _ in range(int(input()))]))

#Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов.
# Выведите количество различных объектов в этом списке.

# import random
# obj = [random.randrange(1, 100) for _ in range(100)]
# obj1 = set()
# obj1 = {id(sym) for sym in obj}
# print(type(obj1))
# print(len(set(obj1)))


# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и
# возвращающую самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5

# def closest_mod_5(x):
#     while x % 5 != 0:
#         x += 1
#     return x
#
# print(closest_mod_5(int(input())))


# task

# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#
#
# print(s(0, 0, 31))
# print(s(11, 10))
# #print(s(b=31, 0))
# print(s(11, 10, 10))
# #print(s(b=31))
# print(s(21))
# print(s(11, b=20))
# print(s(5, 5, 5, 5, 1))
# print(s(11, 10, b=10))


# Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).
## Пример:
# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
# Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
# Различных сочетаний три, поэтому C(3, 2) = 3.
## Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
# Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.
## Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
#
# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
## Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).


# @lru_cache() создает словарь, в котором хранит параметры с которыми была вызвана функция и ответ который она
# вернула. Если где-нибудь в рекурсии снова встретится вызов функции с этими же параметрами- никакого вызова не
# произойдет, ответ вернется из словаря.

# from functools import lru_cache # офигенная штука!!!
#
# @lru_cache()
# def is_C(n,k):
#     if k == 0: return 1
#     elif k > n: return 0
#     else:
#         return is_C(n-1, k) + is_C(n-1, k-1) # рекурсия
#
# ls = list(map(int, input().split()))
# # n, k = map(int, input().split())
# print(is_C(*ls))

#-----
# import itertools
#
# n, k = map(int, input().split())
# var = list(itertools.combinations(range(n), k))
# print(len(var))
# # permutations - все возможные комбинации, combinations - уникальные

# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
# создания пространств имен и добавление в них переменных.

# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#
# Вашей программе на вход подаются следующие запросы:
#
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует
# Рассмотрим набор запросов
#
# add global a
# create foo global
# add foo b
# create bar foo
# add bar a
# Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен, созданной при
# выполнении данного кода
#
# a = 0
# def foo():
#   b = 1
#   def bar():
#     a = 2
# В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. Далее мы
# объявляем функцию foo, что влечет за собой создание локального для нее пространства имен внутри пространства
# global. В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo функцию
# bar, тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.
#
# Добавим запросы get к нашим запросам
#
# get foo a
# get foo c
# get bar a
# get bar b
# Представим как это могло бы выглядеть в коде
#
# a = 0
# def foo():
#   b = 1
#   get(a)
#   get(c)
#   def bar():
#     a = 2
#     get(a)
#     get(b)
# Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
# Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a,
# но в пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично, результатом
# запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.
#
# Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве global
# не была объявлена переменная с.
#
# Более формально, результатом работы get <namespace> <var> является
#
# <namespace>, если в пространстве <namespace> была объявлена переменная <var>
# get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>,
# если переменная не была объявлена
# None, если не существует <parent>, т. е. <namespace>﻿ – это global

# import sys
# sys.stdin = open('input.txt', 'r')


# def create(namespace, parent = None):
#     dict_ns[namespace] = {'parent': parent, 'var_s': set()}
#
# def add(namespace, var):
#     dict_ns[namespace]['var_s'].add(var)
#
# def get(namespace, var):
#     if var in dict_ns[namespace]['var_s']:
#         return namespace
#     else:
#         return get(dict_ns[namespace]['parent'], var)
#
# dict_cmd = {'add': add, 'create': create, 'get': get}
# dict_ns = {'global': {'parent': None, 'var_s': set()}}
#
# for _ in range(int(input())):
#     cmd, namespace, var = input().split()
#     if cmd == 'get':
#         try:
#             print(get(namespace, var))
#         except:
#             print(None)
#     else:
#         dict_cmd[cmd](namespace, var)


# ==============================================     Классы

# class Count:
#     pass
#
# print(Count)
# x = Count()
# print(x)
# x.count = 0
# x.count += 1
# print(x.count)
#
# class Counter:
#     def __init__(self):
#         self.count = 0
#         #self.init_state = -1
#
#     def inc(self):
#         self.count += 1
#
#     def reset(self, num = 0):
#         self.count = num
#
# x = Counter()
# print(x.count)
# x.inc()
# print(x.count)
# Counter.inc(x)
# print(x.count)
# x.reset()
# print(x.count)

# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
# положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
# добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
#
# Класс должен иметь следующий вид:

# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.count = 0
#          # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         # count = self.count + v
#         return self.count + v <= self.capacity
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         if self.can_add(v):
#             self.count += v
#
#         # положить v монет в копилку
#
# box1 = MoneyBox(10)
# n = int(input())
# while box1.can_add(n):
#     box1.add(n)
#     print(box1.count)

# pyrmide
# n = l = 4
# while l:
#     # star = ' ' * l, '*' * (n-l)
#     # rev_star = '*' * (n-l+1), ' ' * l,
#     print(' ' * l, '*' * (n-l), '*' * (n-l+1), ' ' * l, sep='')
#     l -=1

# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел
# из этой последовательности, затем сумму второй пятерки, и т. д.
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
# Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
# последовательных элементов по мере их накопления.
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
# необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
# Обратите внимание, что во время выполнения метода add выводить сумму пятерок может потребоваться несколько раз до
# тех пор, пока в буфере не останется менее пяти элементов.

# Пример работы:
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]

# class Buffer:
#     def __init__(self):
#         self.buffer = []
#         # конструктор без аргументов
#
#     def add(self, *a):
#         self.buffer.extend(a)
#         while len(self.buffer) >= 5:
#             print(sum(self.buffer[:5]))
#             self.buffer[:5] = []
#         # добавить следующую часть последовательности
#
#     def get_current_part(self):
#         return self.buffer
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]

#      obj
#      / \
#     C   A
#    /|   |
#   D |   B
#    \|  /
#      E
#
# L(A) = [A, obj]
# L(C) = [C, obj]
# L(B) = [B] + merge(L(A)[A]) = [B,A,obj]
# L(D) = [D] + merge(L(C)[C]) = [D,C,obj]
# L(E) = [E] + merge(L(B),L(C),L(D)[B,C,D]) =
# = [E] + merge([B,A,obj],[C,obj],[D,C,obj],[B,C,D]) =
# = [E,B] + merge([A,obj],[C,obj],[D,C,obj],[C,D]) =
# = [E,B,A] + merge([obj],[C,obj],[D,C,obj],[C,D]) =
# = [E,B,A, ] + merge() - ERROR (E(B,D,C))
#
# E(B, D, C) - Correct

#=====================================================================
#
# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
#
# Или эквивалентно записи:
#
# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:
#
#
# class B(A):
#     pass
#
#
# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C

# class B(A):
#     pass
#
# class C(B):
#     pass
#
# # A -- предок С
#
#
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
#
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
#
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число q - количество запросов.
#
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
#
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No",
# если не является.

# import sys
# sys.stdin = open('input.txt')
#
## strat - потомок, end - родитель (предок)
# def find_path(graph, start, end, path=[]):
#     path = path + [start]
#
#     if start not in graph:
#         return None
#
#     if start == end:
#         return path
#
#     for node in graph[start]:
#
#         if node not in path:
#
#             newpath = find_path(graph, node, end, path)
#
#             if newpath: return newpath
#
#     return None
#
# # class_ls = [input() for _ in range(int(input()))]
# # class_dict = {val[0]: val[3:].split() for val in class_ls}
# class_dict = {}
# for _ in range(int(input())):
#     key, *val = input().replace(':', ' ').split()
#     if key not in class_dict:
#         class_dict[key] = val
#     else:
#         class_dict[key] += val
#
#
# for k, v in dict(class_dict).items():
#     for ls_val in v:
#         class_dict[ls_val] = class_dict.get(ls_val, list())
#
# for _ in range(int(input())):
#     ls = input().split()
#     if len(ls) > 1:
#         end, start = ls
#     else:
#         end = start = ls[0]
#     print('Yes' if find_path(class_dict, start, end) else 'No')

#==================================================================================
# Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление
# элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания,
# умножения и целочисленного деления.
#
# Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент(top1), затем снимается
# следующий верхний элемент(top2), и затем как результат операции сложения на вершину стека кладется элемент, равный
# top1 + top2.
#
# Аналогичным образом определяются операции вычитания(top1 - top2), умножения(top1 * top2) и целочисленного деления
# (top1 // top2).
# Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.

# Примечание: Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.
# Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента.

# Требуемая структура класса:
#
# class ExtendedStack(list):
#     def sum(self):
#         self.append(self.pop()+self.pop())
#
#
#     def sub(self):
#         self.append(self.pop() - self.pop())
#
#
#     def mul(self):
#         self.append(self.pop() * self.pop())
#
#
#     def div(self):
#         self.append(self.pop() // self.pop())
#
#
# ls = [1, 2, 3, 4, 5, 6]
# test = ExtendedStack(ls)
# print(test.div())

#================================================================
# Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным
# способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.
#
# Рассмотрим класс Loggable:
#
# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))

# У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение,
# добавляя при этом текущее время.
# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении
# элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.
#
# Примечание
# Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс,
# и он будет содержать метод log, описанный выше.

# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self, el):
#         super().append(el)
#         return self.log(el)
#
#
# ls = LoggableList()
# ls.append(input())

#=================================================================
# Вашей программе будет доступна функция foo, которая может бросать исключения.
# Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError,
# ZeroDivisionError и выводит имя пойманного исключения.
# Пример решения, которое вы должны отправить на проверку.
#
# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#      print("ArithmeticError")
# except AssertionError:
#      print("AssertionError")

#==========================================================================
# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
#
# Или эквивалентно записи:
# class Error1(Error2, Error3 ... ErrorK):
#     pass
#
# Антон написал код, который выглядит следующим образом.
#
# try:
#    foo()
# except <имя 1>:
#    print("<имя 1>")
# except <имя 2>:
#    print("<имя 2>")
# ...
#  Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде
#  будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого
# положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
#
# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы.
# Создавать классы исключений также не требуется
#  Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее
# где-то поймали их предка.
#
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
#
#  В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
#  i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
#
# Формат выходных данных
#  Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
# поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

# import sys
# sys.stdin = open('input.txt')
#
# class_dict = {}
# for _ in range(int(input())):
#     key, *val = input().replace(':', ' ').split()
#     if key not in class_dict:
#         class_dict[key] = val
#     else:
#         class_dict[key] += val
#
# for k, v in dict(class_dict).items():
#     for ls_val in v:
#         class_dict[ls_val] = class_dict.get(ls_val, list())
#
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start]:
#         dfs(graph, next, visited)
#     return visited
#
# ls_req = [input() for _ in range(int(input()))]
# ls_out = [ls_req[0]]
# temp = 0
# for i in range(len(ls_req)-1):
#     for sym in ls_out:
#         if sym == ls_req[i+1]: break
#         z = dfs(class_dict, ls_req[i+1])
#         if sym not in z:
#             ls_out.append(ls_req[i+1])
#         else:
#             print(ls_req[i+1])
#             break

#====================================================
# raise
# class Bad_name(Exception):
#     pass
#
# def greet(name):
#     if name[0].isupper():
#         print('Hello ', name)
#     else:
#         raise Bad_name#ValueError(name + ' not correct')
#
# while True:
#     try:
#         greet(input())
#     except Bad_name:
#         print('Wrong')
#     else:
#         break

#===============================================================
# Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
# Также реализуйте новое исключение NonPositiveError.
# # В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить
# неположительное целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить
# положительное целое число, число добавлялось бы как в стандартный list.
#
# В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
#
# Примечание:
# Положительными считаются числа, строго большие нуля.

# class NonPositiveError(Exception):
#     pass
#
# class PositiveList(list):
#     def append(self, el):
#         if el <= 0:
#             raise NonPositiveError
#         else:
#             super().append(el)
#
# ls = PositiveList()
# while True:
#     ls.append(int(input()))
#     print(ls)

#========== import ===========
# from bad_name import greet
#
# print(greet('Pavel'))

#===========================================
# import sys
#
# for path in sys.path:
#     print(path)

#===================================================================================
# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число
# дней, равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

# import test_file, datetime
#
# date_obj = datetime.datetime.strptime(input(), '%Y %m %d')
# days = datetime.timedelta(days=int(input()))
# result = date_obj + days
# print(result.strftime('%Y %-m %-d'))
# # print(result.year, result.month, result.day)

#========================================================================
# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой
# из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
# служит ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.
#
# Файл с информацией
# Файл с паролями
#
# Примечание:
# Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:
#
# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()


# import simplecrypt
#
# # with open('encrypted.bin', 'rb') as enc_file, open('passwords.txt', 'r') as psw:
# #     ciphertext = enc_file.read()
# #     password = psw.readlines()
# #     for pw in password:
# #         try:
# #             plaintext = simplecrypt.decrypt(pw.rstrip(), ciphertext)
# #             print(plaintext.decode('utf8'))
# #         except:
# #             continue
#
# # с мультипроцессом и URL
# from multiprocessing import Process
# import urllib.request
# from functools import lru_cache
#
# ciphertext = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/24466/encrypted.bin').read()
# passwords = urllib.request.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt').readlines()
#
# @lru_cache(maxsize=None) # используем КЭШ для ускорения вычислений в функции
# def decrypt_out(psw, number):
#     try:
#         plaintext = simplecrypt.decrypt(psw, ciphertext)
#         print(plaintext.decode('utf8'))
#
#     except:
#         print(f'{number}. {psw.decode("utf8")}')
#
#
# number = 1
# procs = []
# for psw in passwords:
#     proc = Process(target=decrypt_out, args=(psw.rstrip(), number,)) # создаем процесс для каждого подбора пароля
#     procs.append(proc)
#     proc.start()
#     number += 1
#
# for proc in procs:
#     proc.join()


# #=============== Фибоначи и Факториал с КЭШ===================================
# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonaci(num):
#     if num < 2:
#         return num
#     else:
#        return fibonaci(num-2) + fibonaci(num - 1)
#
#
# @lru_cache(maxsize=None)
# def factorial(num):
#     return num * factorial(num-1) if num > 1 else 1
#
# n = int(input())
# print([fibonaci(i) for i in range(1, n+1)])
# print(factorial(n))

#============ Iterators ============================
# class DoubleIterator():
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0
#
#     def __next__(self):
#         if self.i >= len(self.lst):
#             raise StopIteration
#         self.i += 1
#         return self.lst[self.i - 1]
#
#
# class MyList(list):
#     def __iter__(self):
#         return DoubleIterator(self)
#
# for x in MyList([1,2,3,4,5]):
#     print(x)

#=========== Yeild====================================
# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента
# a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из
# последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x,
# а элемент x является допущенным.
#
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию,
# что и стандартный класс filter, но будет использовать не одну функцию, а несколько.
#
# Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент,
# и сколько не допускают. Обозначим эти количества за pos и neg.
#
# Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает
# True, если элемент допущен, и False иначе.
#
# Рассмотрим процесс допуска подробнее на следующем примере.
# a = [1, 2, 3]
# f2(x) = x % 2 == 0 # возвращает True, если x делится на 2
# f3(x) = x % 3 == 0
# judge_any(pos, neg) = pos >= 1 # возвращает True, если хотя бы одна функция допускает элемент
#
# В этом примере мы хотим отфильтровать последовательность a и оставить только те элементы, которые делятся на два
# или на три.
#
# Функция f2 допускает только элементы, делящиеся на два, а функция f3 допускает только элементы, делящиеся на три.
# Решающая функция допускает элемент в случае, если он был допущен хотя бы одной из функций f2 или f3,
# то есть элементы, которые делятся на два или на три.
#
# Возьмем первый элемент x = 1.
# f2(x) равно False, т. е. функция f2 не допускает элемент x.
# f3(x) также равно False, т. е. функция f3 также не допускает элемент x.
# В этом случае pos = 0, так как ни одна функция не допускает x, и соответственно neg = 2.
# judge_any(0, 2) равно False, значит мы не допускаем элемент x = 1.
#
# Возьмем второй элемент x = 2.
# f2(x) равно True
# f3(x) равно False
# pos = 1, neg = 1
# judge_any(1, 1) равно True, значит мы допускаем элемент x = 2.
#
# Аналогично для третьего элемента x = 3.
#
# Таким образом, получили последовательность допущенных элементов [2, 3].

# class multifilter():
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         return pos >= neg
#
#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         return pos >= 1
#
#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         return neg == 0
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         # iterable - исходная последовательность
#         # funcs - допускающие функции
#         # judge - решающая функция
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#
#     def __iter__(self):
#         # возвращает итератор по результирующей последовательности
#         for i in self.iterable:
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(i):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 yield i
#
# def mul2(x):
#     return x % 2 == 0
#
# def mul3(x):
#     return x % 3 == 0
#
# def mul5(x):
#     return x % 5 == 0


# a = [i for i in range(31)] # [0, 1, 2, ... , 30]

# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
# [0, 30]

#==========
# def multiply_list(list1, list2):
#     for i in range(len(list1)):
#         print(f'{list1[i]} * {list2[i]} = {list1[i] * list2[i]}')
#
#
# multiply_list([1,2,3],[4,5,6])
# # output
# # 1 * 4 = 4
# # 2 * 5 = 10
# # 3 * 6 = 18

#=========================
# Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только
# на единицу и на само себя.
# Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5,
# 31, и еще бесконечно много чисел.
# Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1,
# так как оно имеет ровно один делитель – 1.
#
# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
#
# Пример использования:
#
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# # # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# import itertools
# from datetime import datetime
#
# begin = datetime.now()
# def primes():
#     n = 2
#     while True:
#         # теорема Ферма быстрее чем первый вариант (не правильно считает! ПОЧЕМУ!!!)
#         if n == 2 or n ==3 or ((((2**(n - 1)) - 1) % n == 0) and (((3**(n - 1)) - 1) % n == 0)):
#             yield n
#         n +=1
#
# print((datetime.now() - begin).microseconds)
#
# # первый вариант
# begin = datetime.now()
# def primes1():
#     n =1
#     while True:
#         count = 0
#         n += 1
#         for i in range(1, int(n/2) + 1):
#             if n % i == 0:
#                 count +=1
#         if count < 2:
#             yield n
# print((datetime.now() - begin).microseconds)
# #
# print(list(itertools.takewhile(lambda x : x <= 1000, primes())))
# print(list(itertools.takewhile(lambda x : x <= 1000, primes1())))
# #print(list(itertools.takewhile(lambda x : x <= 10000, primes())) == list(itertools.takewhile(lambda x : x <= 10000,
#                                                                                              # primes1())))
#============================= list comprehension

# ls = [(x,y) for x in range(3) for y in range(3) if y>=x]
# print(ls)
# # аналогично
# ls1 = []
# for x in range(3):
#     for y in range(3):
#         if y >= x:
#             ls1.append((x,y))
#
# print(ls1)

#============== files====================================

# from datetime import datetime

# with open('dataset_24465_4.txt') as input, open('out.txt', 'w') as output_file:
#     output_file.writelines(input.readlines()[::-1])

#=====================
# import os
# import os.path
# from pathlib import Path

# print('os.getcwd(): ',os.getcwd()) # текущая папка
# print('Path: ', Path.cwd())
# print(*os.listdir(), sep='\n') # список дир, файлов
# print(os.path.exists('file.txt')) # существование файла
# print(os.path.exists('file1.txt'))

# print(os.path.isfile('file.txt')) # файл?
# print(os.path.isdir('file1.txt')) # директория?
#
# print(os.path.abspath('file.txt')) # абсалютный путь
#
# os.chdir('.idea')
# print(os.getcwd())

##обход все поддиректорий и отображение файлов

# for cur_dir, dir, file in os.walk('.'):
#     print(cur_dir, dir, file)

# # копирование файлов
# os.chdir('.')
# import shutil
#
# os.mkdir('test') #создание директории
# shutil.copy('out.txt', 'out2.txt') #копия файла
# shutil.copytree('test', 'test/test2') #копия папки

#====================================================
# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть
# хотя бы один файл с расширением ".py".
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом
# порядке.

# import os
# import os.path
#
# os.chdir('./Task 2.4')
# # ls = []
#
# # for cur_dir, dir, file in os.walk('./sample'):
# #     for f in file:
# #         if f[-3:] == '.py':
# #             ls.append(cur_dir[2:])
# #             break
#
# #ls1 = {cur_dir[2:] for cur_dir, dir, file in os.walk('./main') for f in file if f[-3:] == '.py'}
# ls1 = [cur_dir for cur_dir, dir, file in os.walk('sample') if any(f.endswith('.py') for f in file)]
#
# print(*sorted(ls1), sep='\n')
# with open('output.txt', 'w') as out:
#     out.write('\n'.join(sorted(ls1)))

#============== import op
# import operator as op
#
# print(op.add(3, 4))
# print(op.mul(3, 4))
# print(op.contains([1, 2, 3], 4))
#
# x = [1,2,3,4,5,6]
# dict = {'asd': 123, '23': 'qwer', 45: (6, 9, 5)}
#
# f = op.itemgetter(2) # f(x) == [2]
# print(f(x))
# s = op.itemgetter('23')
# print(s(dict))
#
# y = [5, 4, 3, 2, 1]
# f1 = op.attrgetter('sort') # возвращает метод для аргумента переданного в f1
# print(f1(y))
# f1(y)() # вызов ф-ции, y.sort()
# print(y)
#
# z = [5, 4, 3, 2, 1]
# f2 = op.methodcaller('sort') # исполнение метода для атрибута ф-ции f2
# f2(z)
# print(z)

# from functools import partial
#
# x = int('1001', base = 2)
# print(x)
#
# int_2 = partial(int, base = 2)
# print(int_2('1111'))

# import operator as op
# from functools import partial
#
# ls = [
#     ('Anton', 'Nikolaevich', 'Zorro'),
#     ('Dmitry', 'Ivanovich', 'Elsk'),
#     ('Ivan', 'Petrovich', 'Abysov')
# ]
#
# ls_2 = partial(list.sort, key=op.itemgetter(-1))
# print(ls)
# ls_2(ls)
# print(ls)

#===== factorial
# from functools import reduce
#
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n+1))
#
# print(factorial(int(input())))

# #======================================================================
# Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте».
# Но иногда, когда нужно создавать много однотипных лямбда функций, еще удобнее будет создать функцию, которая будет
# их генерировать.
#
# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y,
# которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod
#
# mod_3 = mod_checker(3)
#
# print(mod_3(3)) # True
# print(mod_3(4)) # False
#
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True

# def f(x):
#   def f1(y):
#     return y+x
#   return f1
#
# a=f(5)
# print(a)
# print(a(2))
#
# #================= for tkinter
# import tkinter as tk
#
# windows = tk.Tk()
# windows.grid_columnconfigure(0, weight=1)
# windows.title = 'lambda Test'
# windows.geometry('300x100')
# label = tk.Label(windows, text="Lambda Calculus")
# label.grid(column=0, row=0)
# button = tk.Button(
#     windows,
#     text="Reverse",
#     command=lambda: label.configure(text=label.cget("text")[::-1].lower()),
# )
# button.grid(column=0, row=1)
# windows.mainloop()

#====================== strings
# text = 'My name is {}, and im is {}'
# print(text.format('Pavel', 'potato :)'))

#===============================================
# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#
# Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
# после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.
# Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если
# операций потребуется более 1000, выведите Impossible.
# Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки
# a, или Impossible, если операций потребуется более 1000.
# import sys
# sys.stdin = open('input.txt', 'r')
#
# def min_operation(s: str, a: str, b: str):
#     count = 0
#     # if a == b and a in s or len(b) > len(a): return 'Impossible'
#     # else:
#     #     while True:
#     #         if a not in s:
#     #             return count
#     #         s = s.replace(a, b)
#     #         count += 1
#     if a in b: return 'Impossible'
#     else:
#         while True:
#             if a not in s:
#                 return count
#             elif count == 1000:
#                 return 'Impossible'
#             s = s.replace(a, b)
#             count += 1
#
#
# print(min_operation(input(), input(), input()))

#=================================================================================
# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# # Выведите одно число – количество вхождений строки t в строку s.
#
# Пример:
# s = "abababa"
# t = "aba"
#
# Вхождения строки t в строку s:
# (aba)baba
# ab(aba)ba
# abab(aba)
#
# from timeit import timeit
# import sys
# sys.stdin = open('input.txt', 'r')
#
# def count_str(s:str, t:str):
#     count = 0
#     i = -1
#     while True:
#         i = s.find(t, i+1)
#         if i == -1: return count
#         count += 1
#
# # print(count_str(input(), input()))
# a, b = input(), input()
# print(timeit('count_str(a,b)', number=10, globals=globals()))
#=====================================
# from timeit import timeit
# from math import factorial
# def fact(x):
#     return factorial(x)
#
# print(timeit('fact(99)', number=10, globals=globals()))
# print(timeit(lambda: factorial(999), number=10))

#============= regular expressions===========

# x = 'hello\nworld'
# print(x)
# y = r'hello\nworld' # raw
# print(y)

#====================
# import re

# print(re.match.__doc__)
# pattern = r'abc'
# my_str = 'abc'
# match_obj = re.match(pattern,my_str) # first entry
# print(match_obj)

# pattern = r'abc'
# my_str = 'bvabc'
# match_obj = re.search(pattern,my_str) # search substring
# print(match_obj)

# pattern = r'a[abc]c' # второй символ может быть a или b или c
# my_str = 'asdabczxc 123acc234 zzzaaczz'
# all_incl = re.findall(pattern, my_str) # search substring
# print(all_incl)
#
# fix_string = re.sub(pattern, 'a1', my_str )
# print(fix_string)

#====================
# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так

# import sys, re
# sys.stdin = open('io.txt', 'r')
#
# pattern = r"(.*cat.*cat.*)"
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'cat.*cat', line):
#         print(line)
#     # match = re.search(pattern, line, re.IGNORECASE)
#     # if match:
#     #     print(match.string)
#
#     # process line
# #=====================
# import sys, re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\bcat\b', line):
#         print(line)

#===========Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.========
# import sys, re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'z.{3}z', line):
#         print(line)

#====Выведите строки, содержащие обратный слеш "\﻿".
# import sys, re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\\.*', line):
#         print(line)

#========Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
# import sys, re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\b(.+)\1\b', line):
#         print(line)

#=========В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
# import sys, re
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'human', 'computer', line))

#===В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
# import sys, re
# sys.stdin = open('io.txt', 'r')
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'\ba+\b', 'argh', line, flags = re.IGNORECASE, count=1))

#===В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
# import sys, re
# sys.stdin = open('io.txt', 'r')
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'\b(\w)(\w)+?', r'\2\1', line))

#В каждой строке замените все вхождения нескольких одинаковых букв на одну букву. Буквой считается символ из группы \w.

# import sys, re
# sys.stdin = open('io.txt', 'r')
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'(\w)\1+', r'\1', line))

#========== HHTP==============

# import requests
#
# # res = requests.get('https://docs.python.org/3.9/_static/py.svg')
# # print(res.status_code)
# # print(res.headers['Content-Type'])
# # # print(res.content)
# # # print(res.text)
# # with open('python_logo.png', 'wb') as f:
# #     f.write(res.content)
#
# res = requests.get('https://yandex.ru/search',
#                    params={'text': 'Stepic'})
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.url)

#==============#==============#==============#==============#==============#==============#==============#==============
# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
# возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход
# и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

# import requests, sys, re
#
# sys.stdin = open('io.txt')
# a, b = sys.stdin
# any_link = (r'<a href="(.*?)">')
# pattern = (fr'<a href="{b.rstrip()}">')
# ls = list()
# ls2 = list()
# res = requests.get(a.rstrip())
# if res.status_code == 200:
#     ls = re.findall(any_link, res.text)
#     for link in ls:
#         res1 = requests.get(link)
#         if res1.status_code == 200:
#             ls2.extend(re.findall(any_link, res1.text))
#             # match = re.search(any_link, res1.text)
#             # ls2.extend((match.group(1),))
#
# if b.rstrip() in ls2:
#     print('Yes')
# else:
#     print('No')

#=====================================================================
# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список
# сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность
# символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
# за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.
#
# Сайты следует выводить в алфавитном порядке.
#
# Пример HTML файла:
#
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">
#
# Пример ответа:
#
# mail.ru
# neerc.ifmo.ru
# stepic.org
# www.ya.ru
# ya.ru
#
# import requests, re
#
# ls_all = []
# match_set = set()
# any_link = re.compile(r'<a.*href=[\"\'](http://|ftp://|https://|\.\.)?(.*?)(\:.*|\/.*)?[\'\"].*>')
# res = requests.get(input())
# if res.status_code == 200:
#     ls_all = any_link.findall(res.text)
#     match_set = sorted({i[1] for i in ls_all})
#
# [print(link) for link in match_set]

#=========================================================================================================
# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
# Файл с данными:
# Crimes.csv

# import csv
# from collections import Counter
#
# ls_crimes = []
# with open('Crimes.csv') as f:
#     reader = csv.DictReader(f)
#     ls_crimes = [row['Primary Type'] for row in reader if '2015' in row['Date']]
#     count = Counter(ls_crimes).most_common()
#     name, count = count[0]
#     print(name)
#
#
# # count_crimes = dict()
# # with open('Crimes.csv') as f:
# #     reader = csv.DictReader(f)
# #     for row in reader:
# #         if '2015' in row['Date']:
# #             if count_crimes.get(row['Primary Type'], None):
# #                 count_crimes[row['Primary Type']] += 1
# #             else:
# #                 count_crimes[row['Primary Type']] = 1
# #
# # print(max(count_crimes, key=count_crimes.get))

#===================================================================================================
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть
# поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# # Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#  ﻿Эквивалент на Python:
# class A:
#     pass
# class B(A, C):
#     pass
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно
# от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.
# Sample Input:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Sample Output:
# A : 3
# B : 1
# C : 2
# [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D",
# "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]
import sys
import json

sys.stdin = open('io.txt')
json_read = json.loads(input())

def dfs(graph:dict, start:str, visited=None) -> set:
    '''
    Функция обхода графа и вывод родителей
    :param graph: словарь вида {'key': set()}
    :param start: str
    :param visited:
    :return: мжество всех родителей
    '''
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# graph = {row_dict['name']: set(row_dict['parents']) for row_dict in json_read}
# count_dict = {row_dict['name']: 0 for row_dict in json_read}
graph, count_dict = {}, {}
for row_dict in json_read:
    graph[row_dict['name']] = set(row_dict['parents'])
    count_dict[row_dict['name']] = 0

ls = []
for key, val in graph.items():
    ls.append(dfs(graph, key))

for row_set in ls:
    for key in row_set:
        count_dict[key] += 1

[print(f'{key} : {val}') for key, val in sorted(count_dict.items())]






