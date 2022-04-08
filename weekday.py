# Write a program that outputs whether or not today is a weekday.
# Author: Ciara Doyle

import datetime # this module allows us to work with dates
#ref: https://www.w3schools.com/python/python_datetime.asp

WeekDay = datetime.datetime.today().weekday()
#The datetime. today() method returns the current date, and the weekday() method returns the day of the week as an integer where Monday is indexed as 0 and Sunday is 6.
#ref: https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=The%20datetime.,0%20and%20Sunday%20is%206.

if WeekDay < 5:
    print ("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")
