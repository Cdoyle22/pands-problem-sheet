# Create a program that asks a user to input a string and outputs every second letter in reverse order.
#Author:Ciara Doyle

word = str(input("Please enter a sentence:"))
# this asks for a string input which will be called word

listofletters = list(word)[::-2]
# this uses string slicing to fetch all characters in a string which have an index difference equal to the value supplied at the right starting from the value at the left.
#Ref: https://codippa.com/how-to-print-characters-at-even-position-in-string-in-python/
# including - in front of the number ensures it is in reverse

print (*listofletters)
#This prints every second letter in order from reverse and the asterisk operator is used to unpack an iterable into the argument list of a given function.
