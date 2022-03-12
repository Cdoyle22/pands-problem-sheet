#Write a program that takes a positive floating-point number as input 
# and outputs an approximation of its square root.
#Author: Ciara Doyle
#create a function called <tt>sqrt</tt> 
# look at the newton method at estimating square roots
#"Please enter a positive number:"
#"The square root of" x "is approx. "



#Newton’s Method: 
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.

#Let N be any number then the square root of N can be given by the formula: 
#root = 0.5 * (X + (N / X)) where X is any guess 
# which can be assumed to be N or 1. 


tolerance = 0.000001
def square_root(N):
    #needed to call the function something different as it can only have letters and _ included
   estimate = 1
   while True:
        estimate = (estimate + N / estimate) / 2
        difference = abs(N - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate

def main():
   while True:
       x = input("Please enter a positive number:")
       x = float(x)
       print("The square root of " + str(x) + " is approx.",square_root(x))
#TypeError: can only concatenate str (not "float") to str - need to add str()
main()



