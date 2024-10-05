# printing the Name of our project in  turtle
from tkinter import *
import turtle as t
import os
# import subprocess
# import sys

def preloader():
    t.title('Student Desk')
    t.speed(10)
    t.pensize(15)
    t.color("red")

    t.penup()
    t.setpos(-180, 120)
    t.pendown()

    t.forward(30)
    t.backward(30)

    t.circle(-50, -185)

    t.circle(50, -225)

    t.backward(20)
# s finish
    t.pensize(5)
    t.color("red")
    t.left(45)
    t.forward(120)
    t.color("black")

    t.right(95)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.backward(30)
    t.right(90)
    t.backward(20)
    t.right(90)
    t.backward(40)
    t.right(90)
    t.backward(20)
    t.right(90)
    t.forward(20)

    t.right(90)
    t.backward(20)
    t.forward(20)

# d start
    t.right(90)
    t.backward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.backward(20)
    t.right(90)
    t.forward(100)
    t.backward(100)

# D end

    t.right(90)
    t.forward(10)
    t.right(90)
    t.backward(30)
    t.right(90)
    t.backward(20)
    t.forward(20)
    t.right(90)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(12)

    t.right(90)
    t.backward(30)

# e end

    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.backward(10)

# n end
    t.right(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.backward(20)


# image setting


# wn.setup(width=300,height=300) used to set the window size

# t.screensize(canvwidth=100, canvheight=500,)
    t.color("white")
    t.goto(170, 50)
    t.addshape(f'{os.getcwd()}/images/sd.gif')

    t.shape(f'{os.getcwd()}/images/sd.gif')

    # sys.exit()
    # t.getscreen()._root.mainloop()

preloader()





