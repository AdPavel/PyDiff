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

def sum(ls):
    total = 0
    for i in ls:
        total += i
    print(total)
    return None

sum([1,2,3])




