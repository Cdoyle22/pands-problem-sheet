# Write a program that outputs whether or not today is a weekday.
# Author: Ciara Doyle

import datetime

WeekDay = datetime.datetime.today().weekday()

if WeekDay < 5:
    print ("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")
