import test_file
# Десятичные числа хранятся в списке numbers в виде строк. Дополните приведенный код, чтобы он для каждого десятичного
# числа вывел его представление в виде обыкновенной дроби в формате: десятичное число = обыкновенная дробь
# from fraction import Fraction as F
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
#            '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
#            '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
#            '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# print(*[f'{i} = {F(i)}' for i in numbers], sep='\n')

#Десятичные числа разделенные символом пробела хранятся в строковой переменной s. Дополните приведенный код,
# чтобы он вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби.

# from fractions import Fraction as F
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46' \
#     ' 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60' \
#     ' 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# ls = [F(i) for i in s.split()]
# print(max(ls) + min(ls))

#Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.

# from fractions import Fraction as F
# m, n = input(), input()
# print(f'{m} + {n} = {F(m)+F(n)}')
# print(f'{m} - {n} = {F(m)-F(n)}')
# print(f'{m} * {n} = {F(m)*F(n)}')
# print(f'{m} / {n} = {F(m)/F(n)}')

#На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения
#
# from fractions import Fraction as F
#
# n = int(input())
# summa = F(0)
# for i in range(1, n+1):
#     summa += F(1, i**2)
#
# print(summa)

#На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения
# from fractions import Fraction as F
# from math import factorial
#
# print(sum([F(1, factorial(i)) for i in range(1, int(input())+1)]))

#На вход программе подается натуральное число n. Напишите программу, которая находит наибольшую правильную
# несократимую дробь с суммой числителя и знаменателя равной n. 10 - 3/7
# from fractions import Fraction as F
#
# n = int(input())
# ls = [sym for sym in [F(i, n-i) for i in range(1, n) if i < (n-i)] if (sym.numerator + sym.denominator) == n]
# print(max(ls))

#На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все
# несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.

from fractions import Fraction as F
n = int(input())
ls = sorted(set(F(i, j) for j in range(2, n+1) for i in range(1, j)))
# sets = set()
# for row in ls:
#     for sym in row:
#         if 0 < sym < 1:
#             sets.add(sym)

print(*sorted(ls), sep='\n')
# from fractions import Fraction as F
# print(*sorted(set(F(i, j) for j in range(1, int(input()) + 1) for i in range(1, j))), sep='\n')

