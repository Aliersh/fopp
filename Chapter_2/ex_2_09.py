''' Challenge: Write a program that will compute the area of a rectangle. Prompt the user to enter the 
width and height of the rectangle and store the values in variables called width and height. 
Print a nice message with the answer.'''

width=int(input('Enter width: '))
height=int(input('Enter height: '))

area=width*height
print('The area of a rectangle with width',width,'and height',height,'will be',area)