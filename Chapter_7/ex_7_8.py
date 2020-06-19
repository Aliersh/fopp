'''Write a program that asks the user for the number of sides, the length of the side, the color, and the 
fill color of a regular polygon. The program should draw the polygon and then fill it in.'''

import turtle

wn = turtle.Screen()
cami = turtle.Turtle()

#Inputs for the user
nsides = int(input('Enter number of sides of the polygon: '))
lenght = int(input('Enter lenght of the side: '))
pcolor = input('Enter pen color: ')
fcolor = input('Enter filling color: ')

sides = range(nsides)
cami.color(pcolor)
cami.fillcolor(fcolor)
cami.begin_fill()

for side in sides:
    cami.forward(lenght)
    cami.left(360/nsides)

cami.end_fill()

wn.exitonclick()