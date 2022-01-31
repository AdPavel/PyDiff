#=========================================================  rectangle
# import turtle
#
# def rectangle(width, height):
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.done()
#
# rectangle(int(input()), int(input()))

#====================================================== triangle
# import turtle
#
# def triangle(side):
#     for _ in range(3):
#         turtle.forward(side)
#         turtle.left(120)
#     turtle.done()
#
# triangle(int(input()))

#========================================================3 square

# import turtle
#
# def square(side, angle):
#     for _ in range(2):
#         turtle.left(angle)
#         turtle.forward(side)
#         turtle.left(90)
#         turtle.forward(side)
#         turtle.left(90-angle)
#
# k = 0
# for i in range(8):
#     square(200, 0+k)
#     k +=45
# turtle.done()

#=====Напишите программу, которая рисует правильный шестиугольник
# import turtle
#
# def hexagon():
#     for _ in range(6):
#         turtle.forward(50)
#         turtle.left(60)
#     turtle.forward(50)
#     turtle.right(60)
#
# for _ in range(6):
#     hexagon()
# #     turtle.right(240)
# #
# # turtle.left(120)
# # hexagon()
# # turtle.forward(50)
# turtle.done()

# #=========Напишите программу, которая рисует ромб с углами 60 и 120 градусов.
# import turtle
# def rhomb():
#     for sym in [60,120]*2:
#         turtle.forward(50)
#         turtle.left(sym)
#
# for _ in range(10):
#     rhomb()
#     turtle.left(36)
# turtle.done()

#=================Напишите программу, которая рисует лучи звезды, показанной на рисунке
# import turtle
# def star(side):
#     for _ in range(12):
#         turtle.forward(side)
#         turtle.backward(side)
#         turtle.left(30)
#
# star(50)
# turtle.done()

#========================Напишите программу, которая рисует правильную пятиконечную звезду.
# import turtle
# def star(side):
#     for _ in range(5):
#         turtle.right(144)
#         turtle.forward(side)
#
# star(50)
# turtle.done()

#=========================== узор из квадратов
# import turtle
#
# def square(k):
#     for _ in range(4):
#         turtle.backward(25 + k*5)
#         turtle.right(90)
#
#
# for i in range(20):
#     square(i)
#
# turtle.done()

#================================== лабиринт
import turtle

def half_square(k):
    for i in range(k):
        turtle.forward(10 + i*2)
        turtle.left(90)

turtle.left(90)
half_square(33)
turtle.done()






















