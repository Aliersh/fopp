'''Write a program to draw a face of a clock'''

import turtle

wn=turtle.Screen()
cami=turtle.Turtle()
cami.shape('turtle')

for i in range(12):
    cami.penup()
    cami.forward(80)
    cami.pendown()
    cami.forward(10)
    cami.penup()
    cami.forward(10)
    cami.stamp()
    cami.backward(100)
    cami.right(360/12)
    
wn.exitonclick()