#import random
#======================================='Орел','Решка'==================================================================
# print(*[('Орел','Решка')[random.randrange(2)] for _ in range(int(input()))], sep='\n')

#========================================игрального кубика c 6 гранями==================================================
#Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 6 гранями.
# Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на
# грани кубика (каждое на отдельной строке).
# print(*[random.randint(1,7) for _ in range(int(input()))], sep='\n') # randint - [1,7] вкл

#===================================генерирует случайный пароль=========================================================
#Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину
# пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).

# my_range = list(range(65, 91)) + list(range(97, 123))
# print(*[chr(random.choice(my_range)) for _ in range(int(input()))],sep='')

#=======================================Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).
#Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
# Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.

# print(*sorted(random.sample(list(range(1, 50)), 7)), sep=' ')

#===========================================IP адрес состоит из четырех чисел из диапазона от 00 до 255255
# (включительно) разделенных точкой. Напишите функцию generate_ip(), которая с помощью модуля random  генерирует
# и возвращает случайный корректный IP адрес.
# def generate_ip():
#     ip_ls = random.sample(list(range(255)), 4)
#     return '{}.{}.{}.{}'.format(*ip_ls)
#
# print(generate_ip())

#========================================Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter,
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).
# import string
#
#
# def generate_index():
#     letter = random.sample(string.ascii_uppercase, 4)
#     num = str(random.randint(0, 99)) + '_' + str(random.randint(0, 99))
#     index = [*letter[0:2],num,*letter[2:]]
#     return '{}{}{}{}{}'.format(*index)
#
#
# print(generate_index())

#Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).
# import numpy as np
# matrix = np.array([[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]])
#
# random.shuffle(matrix)
# # for i in matrix:
# #     random.shuffle(i)
#
# print(matrix)

#====Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов
# и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:
# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.

# def ticket():
#     s = random.sample(list(range(1, 10)), 7)
#     ls = ''.join(str(sym) for sym in s)
#     return ls
#
# print(*[ticket() for _ in range(100)], sep='\n')

#Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.
# Например, слова пила и липа или пост и стоп – анаграммы.
# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

# ls = list(input())
# random.shuffle(ls)
# print(''.join(ls))

#Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75
# (включительно), при этом центральная клетка является пустой (она заполняется числом 00).

# import numpy as np
# import random
#
# ls = np.array(random.sample(list(range(1, 76)), 25))
# ls[12] = 0
# ls.shape = (5, 5)
# for row in ls:
#     for el in row:
#         print(str(el).ljust(3), end='')
#     print()

#=================================================Тайный друг 🌶️
#Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе
# с ним решать задачи по программированию.
# import test_file
# import random
# 
# ls = [input() for _ in range(int(input()))]
# ls_rnd = list(ls)
# 
# random.shuffle(ls)
# temp = []
# 
# for i in range(0, len(ls)):
#     print(f'{ls[i]}-{ls[i-1]}')
# print()

#==================================================Генератор паролей 1
#Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных
# и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
# import random as rn
# import string
# n, m = int(input()), int(input())
#
# def generate_password(length):
#     str_up_temp = string.ascii_uppercase.replace('I','').replace('O','') #+ string.digits
#     str_low_temp = string.ascii_lowercase.replace('l','').replace('o','')
#     digital_temp = string.digits.replace('1','').replace('0','')
#
#     password2 = [rn.choice(el) for el in (str_up_temp, str_low_temp, digital_temp)] + [rn.sample(string.digits+string.ascii_letters) for _ in range(3, length)]
#     # for _ in range(length):
#     #     password2 += rn.choice(str_up_temp) + rn.choice(str_low_temp) + rn.choice(digital_temp)
#
#     rn.shuffle(password2)
#     return ''.join(password2)
#
# def generate_passwords(count, length):
#     ls = []
#     for _ in range(count):
#         ls.append(generate_password(length))
#     return ls
#print(*generate_passwords(n, m), sep='\n')

#=======Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью
# системы неравенств:

# import random as rn
#
# n = 10**6
# s0 = 16
# k = 0
# for _ in range(n):
#     x = rn.uniform(-2, 2)
#     y = rn.uniform(-2, 2)
#
#     if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
#         k += 1
# print((k/n)*s0)

#Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа π
import random as rn
from math import pi

n = 10**6
s0 = 4#pi
k = 0
for _ in range(n):
    x = rn.uniform(-1, 1)
    y = rn.uniform(-1, 1)

    if x**2 + y**2 <= 1: #если использовать s0=pi и x**2 + y**2 != 1, ответ точнее
        k += 1
print((k/n)*s0)













