'''Get the user to enter some text and print it out in reverse order.'''

text = input('Please enter some text: ')

ind = -1
rtext = ''
for letter in text:
    letter = text[ind]
    ind-=1
    rtext += letter

print(rtext)