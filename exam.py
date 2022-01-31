# import test_file
#======================= 1 ===============================
# ls = input().split()
# n = int(input())
# matrx = []
# for i in range(n):
#     matrx.append(ls[i::n])
#
# print(matrx)
#======================= max elem in area matrix ===============================
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# max_secondary = matrix[0][0]
# for i in range(n):
#     for j in range(n):
#         if ((i >= n - 1 - j) and i <= j) or ((i >= n - 1 - j) and i >= j):
#             if max_secondary < matrix[i][j]:
#                 max_secondary = matrix[i][j]
#
# print(max_secondary)
#======================= transponir matrix ===============================
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# transp_matrix = []
# for i in range(n):
#     col = [row[i] for row in matrix]
#     transp_matrix.append(col)
#
# for row in transp_matrix:
#     print(*row)
#======================= snow matrix ===============================
# n = int(input())
# matrix = [['*' if j == n-j-1 or i == n-i-1 or i == j or i == n-j-1 else '.' for j in range(n)] for i in range(n)]  # крестик
#
# for row in matrix:
#     print(*row)
#======================= simetrik matrix ===============================
# put your python code here
# n = int(input())
# matrix = [[int(i) for i in input().split(' ')] for j in range(n)]
# flag = True
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[~j][~i]:
#             flag = False
#             break
# print('YES' if flag else 'NO')
#==============================Латинский квадрат========================
# n = int(input())
# matrix = [[int(i) for i in input().split()] for j in range(n)]
# ls = list(range(1, n+1))
# result = 'YES'
# for i in range(n):
#     col = [row[i] for row in matrix]
#     row = matrix[i]
#     if not (sorted(col) == sorted(row) == ls):
#         result = 'NO'
#         break
# print(result)
#==============================Ходы ферзя========================
# pos = input()
# x, y = ord(pos[0]) - ord('a'), 8 - int(pos[1])
# matrix = [['.'] * 8 for _ in range(8)]
# check = 0
# for i in range(8):
#     for j in range(8):
#         if x == j or y == i or abs(y - i) == abs(x - j):
#             #y - i == x - j or y - i == ~x - ~j: #check_diag or check_hor:
#             matrix[i][j] = '*'
# matrix[y][x] = 'Q'
# for row in matrix:
#     print(*row)
#========================= заполнение матрицы по диагонали =======================
# n = int(input())
# matrix = [[0]*n for _ in range(n)]
# count = 1
# for i in range(n):
#     for j in range(n):
#         matrix[i][j] = abs(i - j)
#
# for i in range(n):
#     print(*[str(matrix[i][j]).ljust(3) for j in range(n)])

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
prod = 1
for sym in numbers:
    prod *= sym
print(prod)






