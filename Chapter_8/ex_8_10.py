'''Get the user to enter some text and print out True if it’s a palindrome, False otherwise. (Hint: Start 
by reversing the input string, and then use the == operator to compare two values to see if they are the 
same)'''

word = input('Enter a word: ')
cpos = -1 #Initialize char index
rword = ''

for char in word:
    char = word[cpos]
    rword += char
    cpos -=1

if word == rword:
    print(True)
else:
    print(False)