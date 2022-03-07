# Create a program that asks a user to input a string and outputs every second letter in reverse order.
#Author:Ciara Doyle

word = str(input("Enter a word:"))
listofletters = list(word)[::-2]

print (listofletters)
