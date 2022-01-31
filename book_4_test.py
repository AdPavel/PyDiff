#===== yield    ХЗ пока

# def squre(n):
#     for i in n:
#         yield i**2
#
# ls = squre(5)
# print()

#=================

# def func():
#     x = 'old'
#     print(x)
#     def funint():
#         nonlocal x
#         x = 'new'
#         print(x)
#     return funint()
#
# func()

# рекурсии

# def sum(ls):
# #    total = 0
#     if len(ls) == 1:
#         return ls[0]
#     else:
#         return ls[0] + sum(ls[1:])
#
# def count_el(ls):
#     if len(ls) == 1:
#         return 1
#     else:
#         return 1 + count_el(ls[1:])
#
# def max_element(ls):
#     if len(ls) == 2:
#         return ls[0] if ls[0] > ls[1] else ls[1]
#     sub_max = max_element(ls[1:])
#     return ls[0] if ls[0] > sub_max else sub_max
#
#
# ls = [1,2,3,5,6]
# print(sum(ls))
# print(count_el(ls))
# print(max_element(ls))

# быстрая сортировка

def quick_sort(ls):
    if len(ls) < 2:
        return ls
    else:
        middle = ls[0]
        less = [i for i in ls[1:] if i <= middle]
        greater = [i for i in ls[1:] if i > middle]
        return quick_sort(less) + [middle] + quick_sort(greater)

print(quick_sort([12, 2, 3, 5, 87, 5, 4, 1]))
