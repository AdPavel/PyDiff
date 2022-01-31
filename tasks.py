import test_file
#======================== Конкурсный отбор ======================
# n = int(input())
# ls = [tuple([txt for txt in input().split()]) for _ in range(n)]
# [print(*row) for row in ls]
# print()
# # [print(*row) for row in ls if 4 <= int(row[1]) <= 5]
# for name, grade in ls:
#     if grade in '45':
#         print(name, grade)
#========================= фибоначи ==========================
# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f2+f1
#===================== Tribonachi =====================
# n = int(input())
# ls = [1,1,1]
# count = 0
# if n < 3:
#     print('1 ' * n)
# else:
#     for i in range(n - 3):
#         count = sum(ls[i:])
#         ls.append(count)
#         # print(f1)
#         # f1, f2, f3 = f3+f2+f1, f2+f1, f3 + f2  #1 1 1 3 5 9 17 31 57 105
#     print(*ls)
#--------------------------------
# f1 = f2 = f3 = 1
# for _ in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f1 + f2 + f3
#-------------+++++++++++++++=================== МНОЖЕСТВА ====================+++++++++++++++++++++++++++++------------
# n, m, k, x, y, z = [int(input()) for _ in range(6)]
# print((n+m+k)-(x+y)+z)
#======================= reverse ====================
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# print(*sorted(fruits, reverse=True), sep='\n')
#===================== count =========================
# print(len(set(input())))
#===================== equal? ========
# ls = input()
# print('YES' if len(ls) == len(set(ls)) else 'NO')
#=====================Все 10 цифр========================
# print(('NO', 'YES')[len(set(input()+input())) == 10])
#=======================Три слова==========================
# ls = input().split()
# print(('NO', 'YES')[set(ls[0])==set(ls[1])==set(ls[2])])
#=============================Уникальные символы 1==========
# n = int(input())
# ls = [set(input().lower()) for _ in range(n)]
# print(*[len(el) for el in ls], sep='\n')
#==============================Уникальные символы 2===========
# ls = ''
# for _ in range(int(input())):
#     ls += input().lower()
# print(len(set(ls)))
#============================Количество слов в тексте========
# ls = input().lower()
# ls = ls.translate(ls.maketrans('','','.,;:-?!')) # delete symbol in third argument
# sets = set()
# for el in list(ls.split()):
#     sets.add(el)
# print(len(sets))
#---------------------------------
# ls = [word.strip('.,;:-?!') for word in input().lower().split()]
# print(len(set(ls)))
#=============================Встречалось ли число раньше?===================
# ls = input().split()
# sets = set()
# for el in ls:
#     if el.lstrip('0') not in sets:
#         print('NO')
#         sets.add(el)
#     else:
#         print('YES')
#===============================Количество совпадающих=============================
# myset1 = set(input().split())
# myset2 = set(input().split())
# print(len(myset1.intersection(myset2)))
#=============================Общие числа===========================================

# myset1 = set([int(i) for i in input().split()])
# myset2 = set([int(i) for i in input().split()])
# print(*sorted(myset1.intersection(myset2)))
#=========================Числа первой строки===================================
# myset1 = set(int(i) for i in input().split())
# myset2 = set(int(i) for i in input().split())
# print(*sorted(myset1 - myset2))
#========================Общие цифры2========================================
# myset = set(range(10))
# for _ in range(int(input())):
#     myset &= set(int(i) for i in input())
# print(*sorted(myset))
#============================Все цифры=====================================
# print(('NO', 'YES')[set(input()).issuperset(set(input()))])
#==============================Урок информатики==============================
# myset1 = set([int(i) for i in input().split()])
# myset2 = set([int(i) for i in input().split()])
# myset3 = set([int(i) for i in input().split()])
#
# print(*sorted((myset1 & myset2) - myset3, reverse=True))
#=======================Урок математики=====================================
# myset1 = set([int(i) for i in input().split()])
# myset2 = set([int(i) for i in input().split()])
# myset3 = set([int(i) for i in input().split()])
#
# print(*sorted((myset1^myset2) | (myset2^myset3)))
#=======================Урок физики======================================
# myset1 = set([int(i) for i in input().split()])
# myset2 = set([int(i) for i in input().split()])
# myset3 = set([int(i) for i in input().split()])
#
# print(*sorted(myset3 - (myset1 | myset2), reverse=True))
#============================Урок биологии=================================
# myset1 = set([int(i) for i in input().split()])
# myset2 = set([int(i) for i in input().split()])
# myset3 = set([int(i) for i in input().split()])
# temp_set = set(range(11))
#
# print(*sorted(temp_set - (myset1 | myset2 | myset3)))
#======================== первая буква из списка ===============================
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {word[0].lower() for word in words}
# print(*sorted(myset))
#========================= уникальные слова ==================================
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
#               pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over
#               which, if you can still stand my style (I am writing under observation), the sun of my infancy had set:
#                surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom
#                 or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry
#                  warmth, golden midges.'''
# myset = {word.lower().strip(',.:;!?()') for word in sentence.split()}
# print(*sorted(myset))
#======================== уникальные слова длино менее 4 символов ==================
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {word.lower().strip(',.:;!?()') for word in sentence.split() if len(word.strip(',.:;!?()')) < 4}
# print(*sorted(myset))
#======================== файлы с расширением .png ===================================
# files = ['python.png', 'qwerty.PNG', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# #myset = {file.lower() for file in files if '.png' in file.lower()}
# myset = {file.lower() for file in files if file.lower().endswith('.png')}
# print(*sorted(myset))
#=========================== Книги на прочтение https://stepik.org/lesson/479457/step/15?unit=470432 =()
# n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
# s1 = n + m - x - t
# s2 = m + k - y - t
# s3 = k + n - z - t
# n1 = n - s1 - s3 - t
# m1 = m - s1 - s2 - t
# k1 = k - s2 - s3 - t
# print(n1+m1+k1)
# print(s1+s2+s3)
# print(a-(n1+m1+k1)-(s1+s2+s3)-t)
# 1 =============================Домашнее задание===================================1
# n, m, k, p = (int(input()) for _ in range(4))
# print(n-((m-p)+(k-p)+p))
# 2 ====================================Восход==================================2
# ls = [i for i in input().split()]
# print(len(ls) - len(set(ls)) )
#=====================================Города=====================================3
# n = int(input())
# cities = {input() for _ in range(n)}
# new_citi = input()
# print(('OK', 'REPEAT')[new_citi in cities])
#====================================Книги на прочтение=========================4
# n, m = int(input()), int(input())
# task = {input() for _ in range(n)}
# library = {input() for _ in range(m)}
# for book in library:
#     print(('NO', 'YES')[book in task])
#====================================Странное увлечение=========================5
# paper1 = set([int(i) for i in input().split()])
# paper2 = set([int(i) for i in input().split()])
# paper3 = paper1 & paper2
# print(*sorted(paper3, reverse=True) if len(paper3) != 0 else ('BAD DAY')) # распаковка * действует и на sorted и на BAD DAY
#====================================Онлайн-школа BEEGEEK 1 =========================6
# str1 = {i for i in input().split()}
# str2 = {i for i in input().split()}
# print(('NO', 'YES')[str1 == str2])
#====================================Онлайн-школа BEEGEEK 2 =========================7
# n, m = int(input()), int(input())
# set1 = {input() for _ in range(n)}
# set2 = {input() for _ in range(m)}
# print(len(set1 - set2))
#====================================Онлайн-школа BEEGEEK 3 =========================8
# n, m = int(input()), int(input())
# set1 = {input() for _ in range(n)}
# set2 = {input() for _ in range(m)}
# print(len(set1 ^ set2) if len(set1 ^ set2) != 0 else 'NO')
#====================================Онлайн-школа BEEGEEK 4 =========================9
# print(*sorted(set(input().split())|set(input().split()), reverse=False))
#====================================Онлайн-школа BEEGEEK 5 =========================10
# n, m = int(input()), int(input())
# ls = [input() for _ in range(n+m)]
# set1 = set(ls)
# count = 0
# for el in set1:
#     if ls.count(el) == 1:
#         count += 1
# print(('NO', count)[count != 0])
#====================================Онлайн-школа BEEGEEK 6 =========================11
# n = int(input())
# ls_set = [{input() for __ in range(int(input()))} for _ in range(n)]
# # new_set = set(ls_set[0])
# # for el in ls_set:
# #     new_set &= el
# # print(*sorted(new_set), sep='\n')
# print(*sorted(set.intersection(*ls_set)), sep='\n')











