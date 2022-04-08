# A program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# The program will end if the current value is one.
# Author: Ciara Doyle


def collatz(number):

    if number % 2 ==0: # if the number is even
        print(number//2)
        return number //2 # then divide it by 2

    elif number % 2 ==1: # but if it is odd 
        result = 3* number +1  #multiply it by 3 and add 1  
        print(result)
        return result
 #ref: https://automatetheboringstuff.com/chapter3/
 
n = input("Please enter a positive integer:") # this is input for the positive integer number
while n !=1: #when n is not equal to one the while loop will continue. this is the break for when it equals 1
    n = collatz(int(n))


