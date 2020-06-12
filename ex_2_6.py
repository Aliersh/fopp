'''It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. 
If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights 
you would return home on a Saturday (day 6). 
Write a general version of the program which asks for the starting day number, and the length of your stay,
and it will tell you the number of day of the week you will return on.'''

leaving_day=int(input('Enter leaving day: '))
lenght_stay=int(input('Enter lenght of your stay: '))

rem_day=lenght_stay%7
ret_day=leaving_day+rem_day
print(ret_day)