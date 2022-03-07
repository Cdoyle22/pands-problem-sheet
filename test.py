# Program that reads in a students percentage mark and prints out corresponding the grade checking that the percentage is valid
# Author: Ciara Doyle

percentage = float(input("Enter your percentage:"))

if percentage < 0 or percentage > 100: 
    print ("please enter a number between 0 and 100")
elif percentage < 40:
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit1")
elif percentage < 70:
    print ("Merit2")
else: print("Distinction")