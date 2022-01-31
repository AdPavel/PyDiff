import value as value

import test_file


# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), .
#
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# #======== чей номер оканчивается на 8
# # name_list = []
# # for el in users:
# #     if el['phone'].endswith('8'):
# #         name_list.append(el['name'])
# # print(*sorted(name_list), end=' ')
#
# # name_list = [el['name'] for el in users if el['phone'].endswith('8')]
# # print(*sorted(name_list))
# #========== у которых нет информации об электронной почте
# name_list = [el['name'] for el in users if 'email' not in el or el['email'] == '']
# print(*sorted(name_list))
# ===================================== Строковое представление====================================
# my_dict = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
#
# for el in input():
#     print(my_dict[el], end=' ')
# ===================================== Информация об учебных курсах====================================
# info = {'CS101': [3004,	'Хайнс', '8:00'], 'CS102': [4501, 'Альварадо', '9:00'], 'CS103': [6755, 'Рич', '10:00'],
#         'NT110': [1244, 'Берк', '11:00'], 'CM241': [1411, 'Ли', '13:00']}
# curs = input()
# print(f'{curs}: {info[curs][0]}, {info[curs][1]}, {info[curs][2]}')
# ===================================== Набор сообщений=================================================
# keybord = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#     "A":'2', "B":'22', "C":'222',
#     "D":'3', "E":'33', "F":'333',
#     "G":'4', "H":'44', "I":'444',
#     "J":'5', "K":'55', "L":'555',
#     "M":'6', "N":'66', "O":'666',
#     "P":'7', "Q":'77', "R":'777', "S": '7777',
#     "T":'8', "U":'88', "V":'888',
#     "W":'9', "X":'99', "Y":'999', "Z": '9999',
#     " ":'0'
# }
# message = input().upper().replace('"','')
# print(*[keybord[el] for el in message], sep='')
# ===================================== Код Морзе=================================================
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# dict_morse = dict(zip(letters, morse))
# message = input().upper()
# new_mes = [dict_morse[sym] for sym in message if sym in letters]
# print(*new_mes)
# ===================================== сумма значений словаря=================================================
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# #-------для python 3.6
# keys = dict1.copy()
# keys.update(dict2)
# #-------
# #keys = dict1|dict2 # для python 3.9
# result = {x:dict1.get(x,0)+dict2.get(x,0) for x in keys}
# print(result)
# ===================================== количество символов=================================================
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {sym: text.count(sym)  for sym in text}
# print(result)
# ===================================== наиболее часто встречающееся слово=================================================
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange' \
#     ' barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot' \
#     ' currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate' \
#     ' barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot' \
#     ' currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant' \
#     ' orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# result = {s.count(word): word for word in set(s.split())}
# print(result[max(sorted(result))])
# ===================================== владельцы собак==========================================================
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result = {}
# # result = {el[1:]: [] for el in pets}
# # for string in pets:
# #      result[string[1:]].append(string[0])
# #----------------
# for el in pets:
#         result.setdefault(el[1:], []).append(el[0])
# print(result, sep='\n')
# ===================================== Самое редкое слово ==========================================================
# ls = [word.rstrip('.,!?:;-').lower() for word in input().split()]
# my_dict = {word: ls.count(word) for word in ls}
# ls1 = sorted([key for key, value in my_dict.items() if value == min(my_dict.values())])
# print(ls1[0])
# ===================================== Исправление дубликатов ==========================================================
# message = input().split()
# my_dict = {}
# for sym in message:
#         my_dict[sym] = my_dict.get(sym, -1) + 1
#         print(sym+'_'+str(my_dict[sym]) if my_dict[sym] != 0 else sym, end=' ')
# ===================================== Словарь программиста =========================================================
# message = [input() for _ in range(int(input()))]
# my_dict = {mes[:mes.find(':')].lower(): mes[mes.find(':')+2:] for mes in message}
# qwest = [input().lower() for _ in range(int(input()))]
# [print(my_dict.get(el.lower(), 'Не найдено')) for el in qwest]
# ===================================== Анаграммы 1 =========================================================
# dict1, dict2 = dict(word = sorted(input())), dict(word = sorted(input()))
# print(('NO', 'YES')[dict1 == dict2])
# ===================================== Анаграммы 2 =========================================================
# def get_dict(mes):
#     dict = {}
#     for sym in mes.lower():
#         if sym.isalpha():
#             dict[sym] = dict.get(sym, 0) + 1
#     return dict
#
# print(('NO', 'YES')[get_dict(input()) == get_dict(input())])
# ===================================== Словарь синонимов =========================================================
# my_dict = {}
# for _ in range(int(input())):
#     key, value = input().split()
#     my_dict[key] = value
# invert_my_dict = dict(zip(my_dict.values(), my_dict.keys()))
#
# word = input()
# # if word in my_dict:
# #     print(my_dict[word])
# # else:
# #     print(invert_my_dict[word])
# print(my_dict.get(word, invert_my_dict.get(word)))

# ------------
# #
# my_dict = {inpt_string[0]: inpt_string[1] for inpt_string in [input().split() for _ in range(int(input()))]}
# word = input()
# for key, value in my_dict.items():
#     if word == key:
#         print(value)
#     elif word == value:
#         print(key)
# ===================================== Страны и города =========================================================
# # собрал словарь вида (города): страна
# my_dict = {', '.join(my_string[1:]): my_string[0] for my_string in [input().split() for _ in range(int(input()))]}
# # список городов по которым надо найти страну
# ls = [input() for _ in range(int(input()))]
# # перебор городов и поиск их в ключах
# for citi in ls:
#     for key_citi in my_dict.keys():
#         if citi in key_citi:
#             print(my_dict[key_citi])
# ---------------- для каждого города страна (имхо не очень продуктивно, наверное, словарь становиться намного больше----
# my_dict = {}
# for _ in range(int(input())):
#     contry, *cities = input().split()
#     my_dict.update(dict.fromkeys(cities, contry)) # для каждого города страна
#
# for _ in range(int(input())):
#     print(my_dict[input()])
# ===================================== Телефонная книга ===============================================================
# tel_book = {}
# for _ in range(int(input())):
#     value, key = input().split()
#     tel_book.setdefault(key.lower(), []).append(value)
#
# for _ in range(int(input())):
#     print(*tel_book.get(input().lower(), ['абонент не найден']))
# ===================================== Секретное слово ===============================================================
# word = input()
# freq_dict = {inp_string[0]: int(inp_string[1]) for inp_string in [input().split(':') for _ in range(int(input()))]}
# freq_word = {sym: word.count(sym) for sym in word}
# my_dict = dict(zip(freq_word.keys(), freq_dict.keys()))
# for sym in word:
#     print(my_dict[sym], end='')
# ========================================
# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: numbers[i]**2 for i in range(len(numbers))}
# print(result)
# ========================================
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# #result = {el: colors[el] for el in colors if colors[el] is not None}
# result = {key:val for key,val in colors.items() if val is not None}
# print(result)
# ====================================================================================
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(key): str(val) for key, val in [ls.split(':') for ls in s.split()]}
# print(result)
# ====Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка
# # numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1=========================
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {i: [s for s in range(1, i+1) if i%s == 0] for i in numbers}
# print()
# ====Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря
# letters , за исключением тех, ключи которых есть в списке remove_keys===============================================
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
#            13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {key: val for key, val in letters.items() if key not in remove_keys}
# print(result)

# ====В переменной students хранится словарь, содержащий информацию о росте (в см) и весе (в кг) студентов.
# Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря
# students , где указан рост больше 167 см, а вес меньше 75 кг.===================================================

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
#             'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
#             'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: val for key, val in students.items() if val[0] > 167 and val[1] < 75}
# print(result)

# ======Список tuples содержит кортежи, состоящие из трех чисел.
# Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый элемент
# каждого кортежа, а значением – кортеж из оставшихся двух элементов.===========================================

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
#           (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {data[0]: data[1:] for data in tuples}
# print(result)

# Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.
# Дополните приведенный код, используя генератор, так чтобы получить список result, содержащий вложенные словари в
# соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].

# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
#                  'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{a: {b: c}} for a,b,c in list(zip(student_ids, student_names, student_grades))]
# print(result)

# =================================== exam ============================================================

# Дополните приведенный код, чтобы в списках значений элементов словаря my_dict  не было чисел, больших 2020. При этом
# порядок оставшихся элементов меняться не должен.

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
#            'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
#            'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
# my_dict = {key: [i for i in val if i <= 20] for key, val in my_dict.items()}
# print()

# Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену. Дополните
# приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате
# username@domain.

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# # email_for_sort = []
# # for key, val in emails.items():
# #     for name in val:
# #         email_for_sort.append(f'{name}@{key}')
# # print(*sorted(email_for_sort), sep='\n')

# ==============================================Минутка генетики ==============================================
# Напишите программу, переводящую цепь ДНК в цепь РНК.

# my_dict = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# print(*[my_dict[key] for key in input()], sep='')

# ============================================== Порядковый номер ==============================================
# Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв,
# слова разделены одним пробелом или несколькими.
# Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме,
# с учетом регистра. Для первого вхождения слова программа выведет 1, для второго вхождения того же слова — 2 и т. д.

# ls = input().split()
# my_dict = {}
# for word in ls:
#     my_dict[word] = my_dict.get(word, 0) + 1
#     print(my_dict[word], end=' ')

# ============================================== Scrabble game ==============================================
# В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв.
# Чем реже буква встречается, тем больше она ценится:

# table = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# count = 0
# for sym in input():
#     for key, val in table.items():
#         if sym in val:
#             count += key
#             break
# print(count)

# ============================================== Строка запроса ==============================================
# Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного
# знака и идет до конца адреса. Например:
# https://beegeek.ru?name=timur     # строка запроса: name=timur
# Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
# https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку
# запроса, сформированную из этих параметров.

# def build_query_string(param):
#     # stroka = []
#     # for key, val in param.items():
#     #     stroka.append(key+'='+str(val))
#     # return '&'.join(stroka)
#     return '&'.join(sorted([key + '=' + str(val) for key, val in param.items()]))
#
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

# ============================================== Слияние словарей ==============================================
# Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать
# словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей
# переданного списка.

# def merge(values):  # values - это список словарей
#     m_dict = {}
#     for dict_from_list in values:
#         for key, val in dict_from_list.items():
#             m_dict.setdefault(key, set()).add(val)
#     return m_dict
#
#
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(result)

# ============================================== Опасный вирус ==============================================
#В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль
# прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.
#Для каждого файла известно, с какими действиями можно к нему обращаться:
# запись W (write, доступ на запись в файл);
# чтение R (read, доступ на чтение из файла);
# запуск X (execute, запуск на исполнение файла).
# Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна будет
# возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.

# access_table = {'execute': 'X', 'write': 'W', 'read': 'R'}
# access_dict = {inp_string[0]: inp_string[1:] for inp_string in [input().split() for _ in range(int(input()))]}
#
# for _ in range(int(input())):
#     rigth, file = input().split()
#     print('OK' if access_table[rigth] in access_dict[file] else 'Access denied')

# ============================================== Покупки в интернет-магазине ===========================================
#Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.
#Формат входных данных
#На вход программе подается число n — количество строк в базе данных о продажах интернет-магазина.
# Далее следует n строк с записями вида покупатель товар количество, где покупатель — имя покупателя
# (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц
# товара (натуральное число).

#Формат выходных данных
#Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого
# покупателя — двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке,
# после названия каждого товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.

# ls = [input().split() for _ in range(int(input()))]
# my_dict = {}#{name: {item: count} for name, item, count in [rec for rec in ls]}
# dict_item = {}
# for rec in ls:
#     name, item, count = rec
#
#     #dict_item[item] = dict_item.get(item, 0) + int(count)
#     dict_item.setdefault(item, int(count)) + int(count)
#     if my_dict!={} and my_dict.get(name) and my_dict[name].get(item):
#         dict_item[item] = my_dict[name][item] + int(count)
#         my_dict.setdefault(name, dict_item.copy()).update(dict_item)
#     else:
#         my_dict.setdefault(name, dict_item.copy()).update(dict_item)
#     #
#     dict_item.clear()
#
# for key, val in sorted(my_dict.items()):
#     print(key + ':')
#     for key1,val1 in sorted(val.items()):
#         print(key1, val1)
#------------------------------------------------------------------
ls = [input().split() for _ in range(int(input()))]
my_dict = {}

for rec in ls:
    name, item, count = rec
    my_dict.setdefault(name, {})
    my_dict[name][item] = my_dict[name].get(item, 0) + int(count)

for key, val in sorted(my_dict.items()):
    print(key + ':')
    for key1,val1 in sorted(val.items()):
        print(key1, val1)










