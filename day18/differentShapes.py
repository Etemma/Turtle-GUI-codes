import random
import  turtle as T
dom = T.Turtle()
x = []
for i in range(11):
    x.append(i)
print(x)
colors = [ 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat','SlateGray','SeaGreen','Yellow', 'Orange','CornflowerBlue', 'Purple']
for u in x:
    for _ in range(u):
        if u > 2:
            dom.forward(100)
            dom.right(360/u)
            dom.color(random.choice(colors))

u = T.Screen()
u.exitonclick()