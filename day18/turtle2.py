import  turtle as t

tom = t.Turtle()

for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = t.Screen()
screen.exitonclick()