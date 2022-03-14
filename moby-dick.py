#Write a program that reads in a text file and outputs the number of e's 
# it contains. Think about what is being asked here, 
# document any assumptions you are making.
#The program should take the filename from an argument on the command line.
# I have not shown you how to do this, you need to look it up.
#Author: Ciara Doyle


# The program should take the filename from an argument on the command line:

import os
x = 'C:/Users/paulb/PS 1/my-work/week 07'
os.chdir(x)
#changing directory to where file is saved
filename = (input("Enter file: "))
print (filename)
#request for filename from command line


#Write a program that reads in a text file
with open (filename, 'r') as f:

    #read the content of the file
    data = f.read()
    #using count to get the number of e's
    print (data.count("e"))
#and outputs the number of e's it contains



