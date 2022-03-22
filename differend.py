# count = 0
# n = int(input())
# for i in range(1, int(n/2)+1):
#     if n % i == 0:
#         count += 1
#
# print(count)

#===== теорема Эратосфена

# ls = list(range(2, int(input())+1))
# for p in list(ls):
#     for i in range(p**2, len(list(ls))+1):
#         if i % p == 0:
#             list(ls).pop(i)
# print(ls)

# li = list(range(2, int(input())))
# ls = []
# while len(li) != 0:
#     n = li.pop(0)
#     ls.append(n)
#     for x in list(li):
#         if x % n == 0:
#             li.remove(x)
# print(len(ls))
# print(ls)

#=======================================

# j = 9
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# res = []
#
# l11, l12 = divmod(len(l), j)
# l1 = len(l) // j
# l2 = len(l) % j
# r1 = [l1 + 1] * l2
# r1.extend([l1] * (j - l2))
# # r = [l1 + 1] * l2 + [l1] * (j - l2)  # длины итоговых списков
#
# temp = l.copy()
# for i in r:
#     res.append(temp[:i])
#     del temp[:i]
#
# print(res)

#====================
# Python программа для проверки, является ли двоичное дерево BST или нет
# INT_MAX = 4294967296
# INT_MIN = -4294967296
#
# # Узел двоичного дерева
# class Node:
#     # Конструктор для создания нового узла
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# Возвращает true, если данное дерево является двоичным деревом поиска
# (эффективная версия)

# def isBST(node):
#     lt = leftTree(node)
#     rt = rigtTree(node)
#     return lt and rt
#     # return (isBSTUtil(node, INT_MIN, INT_MAX))

# Retusn true, если данное дерево является BST и его значения
# > = мин и <= макс
# def isBSTUtil(node, mini, maxi):
#     # Пустое дерево BST
#     if node is None:
#         return True
#     # False, если этот узел нарушает ограничение min / max
#     # if node.data < mini or node.data > maxi:
#     if node.data < mini or node.data > maxi:
#         return False
    # В противном случае проверяем поддеревья рекурсивно
    # ужесточение минимального или максимального ограничения
    # return (isBSTUtil(node.left, mini, node.data - 1) and
    #         isBSTUtil(node.right, node.data + 1, maxi))

# Программа драйвера для проверки вышеуказанной функции
#
# def isBinaryTree(node, min_val, max_val):
#     if node is None:
#         return True
#     if not (min_val < node.data <= max_val):
#         return False
#     else:
#         ltree = isBinaryTree(node.left, min_val, node.data)
#         rtree = isBinaryTree(node.right, node.data, max_val)
#         return ltree and rtree
#
# root = Node(4)
# root.left = Node(2)
# root.right = Node(5)
# root.right.right = Node(6)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.left.left.left = Node(7)
#
# # if (isBSTUtil(root, INT_MIN, INT_MAX)):
# #     print("Is BST")
# # else:
# #     print("Not a BST")
#
# print(isBinaryTree(root, -1000000, 1000000))

# task from leetcode
#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])

s = Solution()
print(s.lengthOfLastWord("luffy is still joyboy"))