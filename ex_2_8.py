'''Write a program that will compute the area of a circle. Prompt the user to enter the radius and save it 
to avariable called radius. Print a nice message back to the user with the answer.'''

pi=3.14
radius=int(input('Enter radius value: '))

area=(1/2)*(2*pi*radius)*radius
print('The area of a circle wiyh radius',radius,'is',area)