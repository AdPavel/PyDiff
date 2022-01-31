import test_file
#Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.
# a, b = complex(input()), complex(input())
# ([print(f'{(a)} {op} {(b)} =',eval(f'{(a)} {op} {(b)}')) for op in '+-*'])

#Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число
# с наибольшим модулем и сам модуль числа на отдельных строках.

# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j,
#            1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
#
# # abs_num = [abs(i) for i in numbers]
# # idx = abs_num.index(max(abs_num))
# # print(numbers[idx], max(abs_num), sep='\n')
#
# max_el = max(numbers, key=abs)
# print(max_el, abs(max_el), sep='\n')

#Дано натуральное число n и два комплексных числа z1,z2.Напишите программу, которая вычисляет и выводит значение выражения
n, z1, z2 = int(input()), complex(input()), complex(input())

print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n+1))