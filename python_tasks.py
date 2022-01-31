#=====================================================================
# import sys
# sys.stdin = open('/home/pavel/PycharmProjects/pythonProject/test.txt', 'r')

import test_file
#==========================Подсписки списка===========================================
# Sample Input 2: a b v
# Sample Output 2:
# [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

# def chunk(ls, n):
#     new_ls = []
#     for i in range(len(ls) - n + 1):    # ,kzzzz rfhfv,f =;()
#         new_ls.append(ls[i:i+n])
#     return new_ls
#
# #new_ls = []   ##--------- my dicision on second day
# ls = input().split(' ')
# empty_ls = [[]]
#
# for i in range(1, len(ls)+1):
#     empty_ls.extend(chunk(ls, i))
#
# print(empty_ls)

#--------- my dicision on second day-----------------------------
# for i in range(1, len(ls)+1):
#     for j in range(i):
#         new_ls.append(ls[j:i])
#
# print(sorted(new_ls, key=len))
#====================matrix 1=============================
#-------------  с записью в матрицу
# n, m = int(input()), int(input())
# matrix = []
# for i in range(n):
#     matrix.append([input() for j in range(m)])
#
# for i in range(n):
#     print(*[matrix[i][j] for j in range(m)])
#----------- сразу вывод
# n, m = int(input()), int(input())
# matrix = []
# for i in range(n):
#     print(*[input() for j in range(m)])
#====================matrix 2=============================
# def in_matrix(n,m):
#     matrix = []
#     for i in range(n):
#         matrix.append([input() for j in range(m)])
#     return matrix
#
# def out_matrix(matrix, n, m, flag):
#     for i in range(n):
#         if flag:
#             print(*[matrix[i][j] for j in range(m)])
#         else:
#             print(*[matrix[j][i] for j in range(m)])
#
# n, m = int(input()), int(input())
# matrix = in_matrix(n, m)
# out_matrix(matrix, n, m, True)
# print()
# out_matrix(matrix, m, n, False)
#====================matrix trace=============================
# n = int(input())
# total = 0
# matrix = [input().split(' ') for _ in range(n)]
# total = [int(matrix[i][i]) for i in range(n)]
# print(sum(total))
#====================More than average=============================
# n = int(input())
# matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
# #average = [sum(list(map(int, matrix[i])))/n for i in range(n)]
# for i in range(n):
#     count = 0
#     average = int(sum(matrix[i])/n)
#     for j in range(n):
#         if matrix[i][j] > average:
#            count += 1
#     print(count)
#====================max in area below main diagonal=============================
# n = int(input())
# matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
# maximum = matrix[0][0]
# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > maximum:
#             maximum = matrix[i][j]
# print(maximum)
#====================max in area =============================
# n = int(input())
# matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
# maximum = matrix[0][0]
# for i in range(n):
#     for j in range(n):
#         if ((i >= j) and (i <= (n-1-j))) and matrix[i][j] > maximum or ((i <= j) and (i >= (n-1-j))) and matrix[i][j] > maximum:
#             maximum = matrix[i][j]
# print(maximum)
#====================summ of quarter (четверть)=============================
# n = int(input())
# matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
# total_up = total_right = total_left = total_down = 0
# for i in range(n):
#     for j in range(n):
#         if (i < j) and (i < (n-1-j)):    # up
#             total_up += matrix[i][j]
#         elif (i < j) and (i > (n-1-j)):  # right
#             total_right += matrix[i][j]
#         elif (i > j) and (i < (n-1-j)):  # left
#             total_left += matrix[i][j]
#         elif (i > j) and (i > (n-1-j)):   # down
#             total_down += matrix[i][j]
#
# print(f'Верхняя четверть: {total_up}', f'Правая четверть: {total_right}', f'Нижняя четверть: {total_down}', f'Левая четверть: {total_left}', sep = '\n' )
#==================== multiplication table =============================
# n, m = int(input()), int(input())
# mult = [[0] * m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         mult[i][j] = i*j
#
# for i in range(n):
#     print(*[str(mult[i][j]).ljust(3) for j in range(m)])
#==================== maximum in table =============================
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
# maximum = [0, 0]
# max_number = matrix[0][0]
# for i in range(len(matrix)):
#     if max(matrix[i]) > max_number:
#         max_number = max(matrix[i])
#         maximum[0], maximum[1] = i, matrix[i].index(max(matrix[i]))
#
# print(*maximum)
#==================== Column swapping (Обмен столбцов) =============================
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
## a_b = list(map(int, input().split(' ')))
## a = a_b[0]
## b = a_b[1]
# a,b = [int(i) for i in input().split()]
# for i in range(n):
#     matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
#
# for i in range(n):
#     print(*[matrix[i][j] for j in range(m)])
#-------------------получить столбец-------------------------------------------------------
# col_a = [row[a] for row in matrix]
# col_b = [row[b] for row in matrix]
# ==================== Symmetric matrix (Симметричная матрица) =============================
# n = int(input())
# matrix = [[int(i) for i in input().split(' ')] for j in range(n)]
# flag = True
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             flag = False
#             break
# print('YES' if flag else 'NO')
#==================== Swap of matrix diagonal (Обмен диагоналей) =============================
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]
#
# for row in matrix:
#     print(*row)
#==================== Mirroring (Зеркальное отображение) =============================
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# matrix.reverse()
# # for i in range(n//2):
# #     matrix[i], matrix[n - (i + 1)] = matrix[n - (i + 1)], matrix[i]
#
# for row in matrix:
#     print(*row)
#==================== Rotate matrix (Поворот матрицы) =============================
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# new_matrix = []
# for i in range(n):
#     col = [row[i] for row in matrix]
#     col.reverse()
#     new_matrix.append(col)
#
# for row in new_matrix:
#     print(*row)
#==================== Knight's Moves (Ходы коня) =============================
# pos = input()
# x, y = ord(pos[0]) - ord('a'), 8 - int(pos[1])
# matrix = [['.'] * 8 for _ in range(8)]
# check = 0
# matrix[y][x] = 'N'
# for i in range(8):
#     for j in range(8):
#         check = (x - j) * (y - i)
#         if check == 2 or check == -2:
#             matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)
#==================== Magic Square (Магический квадрат) =============================
# def is_equal(list, n):
#     flag = True
#     for i in range(1, n):
#         if list[i] != list[i-1]:
#             flag = False
#             break
#     return flag
#
# def sum_row(n, matrix):
#     sum_row_v = []
#     for i in range(n):
#         sum_row_v.append(sum(matrix[i]))
#
#     if is_equal(sum_row_v, n):
#         return sum_row_v[0]   # сумма по строкам
#     else:
#         return False
#
# def sum_col(n, matrix):
#     sum_col_v = []
#     for i in range(n):
#         sum_col_v.append(sum([row[i] for row in matrix]))  # сумма по столбцам
#     if is_equal(sum_col_v, n):
#         return sum_col_v[0]
#     else:
#         return False
#
#
# def sum_diagonal(n, matrix):
#     main_sum_diagonal = secondery_sum_diagonal = 0
#     # сумма по диагоналям
#     for i in range(n):
#         main_sum_diagonal += matrix[i][i]
#         secondery_sum_diagonal += matrix[i][n - i - 1]
#     if main_sum_diagonal == secondery_sum_diagonal:
#         return main_sum_diagonal
#     else:
#         return False
#
# def check_digital(n, matrix):
#     sort_matrix = []
#     template = [i for i in range(1, n**2+1)]
#     for i in range(n):
#         for j in range(n):
#             sort_matrix.append(matrix[i][j])
#
#     sort_matrix.sort()
#     if sort_matrix == template:
#         return True
#     else:
#         return False
#
# n = int(input())
# matrix = [[int(i)for i in input().split()] for _ in range(n)]
# if check_digital(n, matrix):
#     sum_col = sum_col(n, matrix)
#     sum_row = sum_row(n, matrix)
#     sum_diagonal = sum_diagonal(n, matrix)
#     if sum_col == sum_row == sum_diagonal and sum([sum_col, sum_row, sum_diagonal]) != 0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')
#==================== Chess board (Шахматная доска) =============================
# n, m = [int(i) for i in input().split()]
# matrix = [['.'] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(1 - i%2, m, 2):
#         matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)
#==================== Side diagonal (Побочная диагональ) =============================
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     matrix[i][n - i - 1] = 1
#     for j in range(n):
#         if i > n-1-j:
#             matrix[i][j] = 2
#
# for row in matrix:
#     print(*row)
#==================== load (заполнение 1) =============================
# n, m = [int(i) for i in input().split()]
# count = 1
# matrix = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = count
#         count += 1
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(m)])
#==================== load (заполнение 2) =============================

# n, m = [int(i) for i in input().split()]
# matrix = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i+1 + j*n
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(m)])
#-------------------------------------------------------------------
# n, m = [int(i) for i in input().split()]
# count = 1
# matrix = [[0]*m for _ in range(n)]
# for j in range(m):
#     for i in range(n):
#         matrix[i][j] = count
#         count += 1
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(m)])
# ==================== load 3 (заполнение 3) =============================
# n = int(input())
# # matrix = [[0]*n for _ in range(n)]
# # for i in range(n):
# #      matrix[i][i] = 1
# #      matrix[i][n-i-1] = 1
#
# ####matrix = [[1 if j == n-j-1 or i == n-i-1 else 0 for j in range(n)] for i in range(n)]  # крестик
#
# matrix = [[1 if i == j or i == n-j-1 else 0 for j in range(n)] for i in range(n)]
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(n)])
# ==================== load 4 (заполнение 4) =============================
# n = int(input())
# matrix = [[0 if (i>j and i < n-j-1) or (i<j and i > n-1-j) else 1 for j in range(n)] for i in range(n)]
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(n)])
# ==================== load 5 (заполнение 5) =============================
# n, m = [int(i) for i in input().split()]
# row = list(range(1, m+1))
# matrix = [[0]*m for _ in range(n)]
# shift = 0
# for i in range(n):
#     matrix[i] = row[shift:]+row[:shift]
#     shift += 1
#     if shift == m:
#         shift = 0
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(m)])
# ==================== snake (змейка) =============================
# n, m = [int(i) for i in input().split()]
# matrix = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + 1 + j
#     if i % 2 != 0:
#         matrix[i].reverse()
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(m)])
# ==================== Filling with diagonals (Заполнение диагоналями) =============================
# n, m = [int(i) for i in input().split()]
# matrix = [[0]*m for _ in range(n)]
# count = 1
# for num in range(n+m-1):
#     for i in range(n):
#         for j in range(m):
#             if (i + j) == num:
#                 matrix[i][j] = count
#                 count += 1
#
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(m)])
# ==================== Spiral (спираль) =============================
# n, m = [int(i) for i in input().split()]
# # row, col = n, m
# # #list = [i for i in range(1, n*m+1)]
# matrix = [[0] * m for _ in range(n)]
# count = 1
# shift = 0
#----------------- 1---------------------------------------------------------
# while count <= row*col:
# #  ---->
#     for i in range(1):
#         for j in range(m):
#             if j == m - (shift + 1):
#                 break
#             else:
#                 matrix[i + shift][j+shift] = count
#                 count += 1
# # down
#     for i in range(n):
#         for j in range(m):
#             # if matrix[i][j] != 0:
#             #     break
#             if j == m - 1:
#                 if matrix[i][j] != 0:
#                     continue
#                 else:
#                     matrix[i][j] = count
#                     count += 1
# # <----
#     for i in range(n):
#         for j in range(m-2, -1, -1):
#             if matrix[i][j] != 0:
#                 break
#             if i == n - 1: # and j == m - i:
#                 matrix[i][j] = count
#                 count += 1
# # up
#     for i in range(n-2, 0, -1):
#         for j in range(m):
#             # if matrix[i][j] != 0:
#             #     break
#             if j == shift:
#                 if matrix[i][j] != 0:
#                     continue
#                 else:
#                     matrix[i][j] = count
#                     count += 1
#
#     n -= 1
#     m -= 1
#     shift +=1
#
# for i in range(row):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(col)])
#----------------- 2---------------------------------------------------------
# total = n*m
# while count <= total:
#     for j in range(shift, m):
#         matrix[shift][j] = count
#         count += 1
#
#     for i in range(shift+1, n):
#         matrix[i][j] = count  # j остаеься с предыдущего цикла
#         count +=1
#     if count == total+1:    # для одномерного массива
#         break
#     for j in range(m-2, shift-1, -1): # начинаем с правого нижнего угла, т.к. i и j получены ранее и не определены занов
#         matrix[i][j] = count
#         count += 1
#
#     for i in range(n-2,shift, -1):
#         matrix[i][j] = count
#         count += 1
#
#     n -= 1
#     m -= 1
#     shift +=1
#
# for row in matrix:
#     for sym in row:
#         print(str(sym).ljust(3), end = '')
#     print()
# ====================  (прогрессия) =============================
# n = 4
# x = 0
# count = 1
# while count < 26:
#     x += n
#     count += 1
#
# print(x)
# ==================== sum of matrix (сумма матриц) =============================
# import numpy as np
# n, m = [int(i) for i in input().split()]
# # matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
# # empty = input()
# # matrix_b = [[int(i) for i in input().split()] for _ in range(n)]
# matrix_c = [[0] * m for _ in range(n)]
# # for i in range(n):
# #     for j in range(m):
# #         matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
# #
# # for row in matrix_c:
# #     print(*row)
# #--------------------with numpy----------------------------------
# matrix_a = np.array(list(input().split() for _ in range(n)), int)
# empty = input()
# matrix_b = [[int(i) for i in input().split()] for _ in range(n)]
# matrix_c = [[0] * m for _ in range(n)]
#
# matrix_c = matrix_a + matrix_b
#
# for row in matrix_c:
#     print(*row)
# ==================== prod of matrix (произведение матриц) =============================
# n, m = [int(i) for i in input().split()]
# matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
# empty = input()
# m, k = [int(i) for i in input().split()]
# matrix_b = [[int(i) for i in input().split()] for _ in range(m)]
# matrix_c = [[0] * k for _ in range(n)]
# s = 0
# for i in range(n):
#     row = matrix_a[i]
#     for j in range(k):
#         col = [row[j] for row in matrix_b]
#         s = 0
#         for l in range(m):
#             s += row[l] * col[l]
#         matrix_c[i][j] = s
#
# for row in matrix_c:
#     print(*row)
#--------whith numpy
# import numpy as np
# n, m = [int(i) for i in input().split()]
# a = np.array(list(input().split() for _ in range(n)), int)
# empty = input()
# m, k = [int(i) for i in input().split()]
# b = np.array(list(input().split() for _ in range(m)), int)
# #c = np.zeros((n, k), int)
#
# c = np.dot(a,b)
# for row in c:
#     print(*row)
# ==================== pow of matrix (матриц в степень) =============================
def prod_matrix(matrix, matrix_temp, n):
    matrix_c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                matrix_c[i][j] += matrix[i][l] * matrix_temp[l][j]
    return matrix_c

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
matrix_temp = matrix
while m-1 > 0:
    matrix = prod_matrix(matrix, matrix_temp, n)
    m -= 1
for row in matrix:
    print(*row)





























