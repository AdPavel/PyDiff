#=На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его содержимое.

# file_= open(input())
# print(file_.read())
# file_.close()

#На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его предпоследнюю строку.

# file_ = open(input())
# print(file_.readlines()[-2])
# file_.close()

#Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную строку из этого файла.

# import random
#
# file = open('lines.txt')
# # read_file = file.readlines()
# # print(read_file[random.randrange(len(read_file))])
# print(random.choice(file.readlines()))
# file.close()

#Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу, выводящую на экран сумму этих чисел.

# file = open('numbers.txt')
# # content = list(map(int, file.readlines()))
# # print(sum(content))
# print(sum(map(int, file)))
# file.close()

#Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и
# конца строки. Напишите программу, выводящую на экран сумму этих чисел.

# file = open('nums.txt')
# # content = file.readlines()
# # print(sum(map(int, filter(str.isdigit, map(str.strip, content)))))
# cont = file.read().split()
# print(sum(map(int, cont)))

#Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью
# символа табуляции (\t) разделена на три колонки:

# 1. наименование товара;
# 2. количество товара (целое число);
# 3. цена (в рублях) товара за 11 шт (целое число).
#
# Напишите программу, выводящую на экран общую стоимость заказа.
#from functools import reduce
# file = open('prices.txt')
# content = file.readlines()
# summ = 0
# for name, count, cost in list(map(str.split, content)):
#     summ += int(count)*int(cost)
# print(summ)
# file.close()

#Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в
# обратном порядке.

# with open('text.txt') as file:
#     print(file.read()[::-1])

#Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки
# данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

# with open('data.txt') as file:
#     print(*file.readlines()[::-1], sep='')

#ам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки
# наибольшей длины из файла, не меняя их порядок.

# with open('lines.txt') as file:
#     ls = list(map(str.rstrip, file.readlines()))
#     max_el = max(ls, key=len)
#     # print(*[el for el in ls if len(el) == len(max_el)], sep='\n')
#     print(*filter(lambda x: len(x) == len(max_el), ls), sep='\n')

#Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел,
# разделенных одним или несколькими пробелами.
# Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки
# выводится сумма чисел в этой строке).

# with open('numbers.txt') as file:
#     # ls = list(map(str.split, file.readlines()))
#     # print(*[sum(list(map(int, ls_))) for ls_ in ls], sep='\n')
#     print(*[sum(list(map(int, line.split()))) for line in file], sep='\n')

#Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно. Числом
# назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).
# Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

# with open('nums.txt') as file:
#     line = file.read()
#     new_line = ''
#     for el in line:
#         if el.isdigit():
#             new_line += el
#         else:
#             new_line += ' '
#     print(sum(map(int, new_line.split())))

#Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
# латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

# with open('file.txt') as file:
#     count_lines = 0
#     count_word = 0
#     count_letter = 0
#     for line in file:
#         count_lines += 1
#         count_word += len(line.split())
#         count_letter += len(list(filter(str.isalpha, ''.join(line.rstrip().split()))))
#     print(f'''Input file contains:
# {count_letter} letters
# {count_word} words
# {count_lines} lines''')

#Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
# Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их,
# каждую на отдельной строке.

# import random
# with open('first_names.txt') as name, open('last_names.txt') as lastname:
#     name_ls, lastname_ls = name.readlines(), lastname.readlines()
#     [print(f'{random.choice(name_ls).rstrip()} {random.choice(lastname_ls).rstrip()}') for _ in range(3)]

#Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.
# Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше
# чем 500 000 человек, не меняя их порядок.

# with open('population.txt') as file:
#     ls = list(map(str.split, file.readlines()))
#     [print(country) for country, popul in filter(lambda x: x[0][0] == "G" and int(x[-1]) > 5 * 10**5, ls)]

#Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из
# этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую
# строку как значения этих ключей.

# def read_csv():
#     with open('data.csv') as file:
#         dict_key = file.readline().strip().split(',')
#         # ls = []
#         # for line in file:
#         #     val = line.strip().split(',')
#         #     ls.append(dict(zip(dict_key, val)))
#         ls = [dict(zip(dict_key, line.strip().split(','))) for line in file]
#         return ls

# print(read_csv())

#========================================== ЗАПИСЬ В ФАЙЛ===================================================

#Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt

# with open('output.txt', 'w') as output:
#     print(input(), file=output)

#Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне от 111 до 777
# (включительно), каждое с новой строки.

# from random import randint
# with open('random.txt', 'w') as output:
#     print(*[randint(111, 777) for _ in range(25)], sep='\n', file=output)

#Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого
# файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
# Нумерация строк должна начинаться с 1.

# with open('input.txt') as input_file, open('output.txt', 'w') as output_file:
#     # ls_ = list()
#     # ls = list(map(lambda x: f'{x[0]}) {x[1]}', enumerate(input_file.readlines(), 1)))
#     for number, val in enumerate(input_file.readlines(), 1):
#         print(f'{number}) {val.rstrip()}', file=output_file)

#Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и
# оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.
#Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в
# файл new_scores.txt.

# with open('class_scores.txt') as input_file, open('new_scores.txt', 'w') as output_file:
#     # ls = list(map(str.split, map(str.strip, input_file.readlines())))
#     # [print(f'{line[0]} {int(line[1])+5}', file=output_file) for line in ls]
#
#     for line in input_file:
#         lastname, score = line.split()
#         print(f'{lastname} {min(100, int(score)+5)}', file=output_file)

#Однажды Жака Фреско спросили:

# "Если ты такой умный, почему не богатый?"
#
# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
#
# "Были разноцветные козлы. Сколько?"
#
# "Сколько чего?"
#
# "Сколько из них составляет более 7% от общего количества козлов?"
#
# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.
#
# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

# with open('goats.txt') as input_file, open('answer.txt', 'w') as output:
#     # dict_goats = {'GOATS':0}
#     # line = input_file.readline()
#     # line = input_file.readline()
#     # while line.strip() != 'GOATS':
#     #     dict_goats[line.strip()] = 0
#     #     line = input_file.readline()
#     # line = input_file.readline()
#     # for line in input_file:
#     #     dict_goats['GOATS'] += 1
#     #     dict_goats[line.strip()] += 1
#     # ls = list(filter(lambda  key: int(dict_goats[key]/dict_goats['GOATS'] *100) > 7, dict_goats))
#     # print(*ls[1:], sep='\n', file=output)
#
#     whole = input_file.read().split('\n')
#     color = whole[1:whole.index('GOATS')]
#     goats = whole[whole.index('GOATS') + 1:]
#     print(*sorted(filter(lambda x: int(goats.count(x)/len(goats) * 100) > 7, color)), sep='\n',file=output)

#На вход программе подается натуральное число n и n строк с названиями файлов. Напишите программу, которая создает
# файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

# import sys
# sys.stdin = open('io.txt', 'r')
# #ls_file_name = [input() for _ in range(int(input()))]
# for _ in range(int(input())):
#     file_name = input()
#     with open(file_name) as input_file, open('output.txt', 'a') as output:
#         output.write(input_file.read())


#Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. Каждая
# строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, время
# выхода, где время указано в 24-часовом формате.

#Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка
# следования), которые были в сети не менее часа.
# def in_minute(arg):
#     ls = list(map(int, arg.split(':')))
#     return ls[0]*60+ls[1]
#
#
# with open('logfile.txt') as input_file, open('output.txt', 'w') as output:
#     # ls = input_file.read().split('\n')
#     for line in input_file:
#         name, enter_time, out_time = line.rstrip().split(',')
#         if in_minute(out_time) - in_minute(enter_time) >= 60:
#             print(name, file=output)

#=============================ЭКЗАМЕН=================================================================================

# На вход программе подается строка текста с именем текстового файла. Напишите программу для вывода на экран
# количества строк данного файла.

# with open(input()) as input_file:
#     print(len(input_file.readlines()))

# Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц. На каждой строке файла указано,
# сколько клиент заплатил за товар, в долларах (целое число):
# $47
# $100
# $60
# $12
# $8
# ...
# Напишите программу для подсчета суммарной месячной выручки фирмы.
# summ = 0
# with open('ledger.txt') as file:
#     for line in file:
#         summ += int(line[1:])
#
# print(f'${summ}')

# Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров. Строки
# файла имеют вид: фамилия оценка_1 оценка_2 оценка_3.
# Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным,
# если количество баллов по нему не меньше 65.
# count = 0
# with open('grades.txt') as file:
#     for line in file:
#         name, t1, t2, t3 = line.strip().split()
#         if int(t1) >= 65 and int(t2) >= 65 and int(t3) >= 65:
#             count += 1
# print(count)

# Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и
# выводит самые длинные слова этого файла, не меняя порядка их следования.

# with open('words.txt') as file:
#     ls = file.readline().split()
#     max_word = max(ls, key=len)
#     print(*filter(lambda x: len(max_word) == len(x), ls), sep='\n')

# На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран
# последние 10 строк данного файла.

# with open(input()) as input_file:
#     # ls = list(map(str.strip, input_file.readlines()[-10:]))
#     # print(*ls, sep='\n')
#     print(*input_file.readlines()[-10:], sep='')

# На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран
# содержимое этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется,
# что все слова в этом файле записаны в нижнем регистре.

# with open('forbidden_words.txt') as forbidden, open(input()) as input_file: #поставить вместо 'data.txt' # input()
#     ls_forb = forbidden.readline().strip().split()
#     line = input_file.read()
#     line_lower_star = line
#     for word in ls_forb:
#         line_lower_star = line_lower_star.lower().replace(word, len(word) * '*')
#
# line_out = []
# for i in range(len(line)):
#     if line[i].lower() == line_lower_star[i]:
#         line_out.append(line[i])
#     else:
#         line_out.append(line_lower_star[i])
# print(''.join(line_out))

# Транслитерация — передача знаков одной письменности знаками другой письменности, при которой каждый знак (или
# последовательность знаков) одной системы письма передаётся соответствующим знаком (или последовательностью знаков) другой системы письма.

# Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла,
# то есть замены кириллических символов на латинские в соответствии с предложенной таблицей. Все остальные символы
# надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt.

# d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n',
#       'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y',
#       'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j',
#       'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }
#
# with open('cyrillic.txt') as input_file, open('transliteration.txt', 'w') as output:
#     ls = input_file.read()
#     line = ''
#     for sym in ls:
#         if sym in d:
#             line += d[sym]
#         else:
#             line += sym
#     print(line, file=output)

# При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и
# возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.

# На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите
# программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать,
# что любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит
# комментарий, если первый символ предыдущей строки - #.

# with open(input()) as file:
#     ls = file.read().strip().split('\n')
# new_ls = []
# for i in range(len(ls)):
#     if ls[i][0:4] == 'def ' and ls[i-1].find('#') < 0:
#         new_ls.append(ls[i][4:ls[i].find('(')])
#
# if len(new_ls) > 0:
#     print(*new_ls, sep='\n')
# else:
#     print('Best Programming Team')
