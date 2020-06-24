'''Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
a. Write a loop that prints each of the numbers on a new line.
b. Write a loop that prints each number and its square on a new line.'''

nlist = [12,10,32,3,66,17,42,99,20]

for number in nlist:
    print(number)

for number in nlist:
    sqrt = (number)**(1/2)
    print(number, sqrt)