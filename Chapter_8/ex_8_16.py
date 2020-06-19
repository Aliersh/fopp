'''Create one conditional so that if “Friendly” is in w, then “Friendly is here!” should be assigned to the 
variable wrd. If it’s not, check if “Friend” is in w. If so, the string “Friend is here!” should be assigned 
to the variable wrd, otherwise “No variation of friend is in here.” should be assigned to the variable wrd. 
(Also consider: does the order of your conditional statements matter for this problem? Why?)'''

w = "Friendship is a wonderful human experience!"

words = w.split(' ')

for word in words:
    if 'Friendly' in word:
        wrd = 'Friendly is here!'
        break
    elif 'Friend' in word:
        wrd = 'Friend is here!'
        break
    else:
        wrd = 'No variation of friend is in here'

