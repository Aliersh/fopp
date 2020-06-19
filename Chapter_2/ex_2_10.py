'''Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven 
and the number of gallons used. Print a nice message with the answer.'''

miles = int(input( "Enter miles driven: " ))

gallons = int(input( "Enter gallons used: " ))

MPG = miles/gallons

print( "MGP: " + str(MPG) )