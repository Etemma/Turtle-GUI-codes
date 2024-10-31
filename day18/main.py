from turtle import Turtle, Screen

joe = Turtle()
joe.shape('turtle')
joe.color('firebrick2')
##DRAWING A SQUARE

for _ in range(4):
    joe.forward(100)
    joe.right(90)
screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())