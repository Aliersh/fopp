'''A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes 
another 100 steps, turns another random amount, etc. A social science student records the angle of each 
turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, 
-86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. 
After the pirate is done walking, print the current heading. Assume that the turtle originally has a 
heading of 0 and accumulate the changes in heading to print out the final. Your solution should work for 
any sequence of experimental data.'''

import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# I don't understand the heading part
for angle in angles:
    pirate.left(angle)
    pirate.forward(100)
   
print(head)

wn.exitonclick()