import turtle as tt
import random

dan = tt.Turtle()
tt.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return  rand_color

dan.speed('fastest')
def draw_spirograph(gap_size):
        for _ in range(int(360/gap_size)):
            dan.circle(100)
            dan.color(random_color())
            dan.setheading(dan.heading()+ gap_size)

draw_spirograph(5)

u = tt .Screen()
u.exitonclick()