'''Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, 
all angles the same):
An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)'''

import turtle

wn=turtle.Screen()
cami=turtle.Turtle()

for i in range(8):
    cami.forward(50)
    cami.left(360/8)

wn.exitonclick()