# colors = [ 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat','SlateGray','SeaGreen','Yellow', 'Orange','CornflowerBlue', 'Purple']
import turtle as o
import random

hil = o.Turtle()
o.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return  rand_color
directions = [0, 90, 180, 270]
hil.speed('fastest')
for i in range(500):
    hil.forward(30)
    hil.setheading(random.choice(directions))
    hil.color(random_color())
    hil.pensize(10)

s = o.Screen()
s.exitonclick()