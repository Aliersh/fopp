'''Challenge: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on the clock when the alarm goes off.'''

currently_hour=int(input('Enter currently hour: '))
alarm_hours=int(input('Enter how many hours for alarm: '))

hours_sum=alarm_hours%24
alarm_time=currently_hour+hours_sum
print(alarm_time)