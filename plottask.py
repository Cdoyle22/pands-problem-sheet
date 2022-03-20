# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 
# and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Ciara Doyle

import numpy as np
import matplotlib.pyplot as plt

#f(X)=X
fxpoints = np.array(range(0,5))
fypoints = fxpoints

#g(X)=2X
gxpoints = np.array(range(0,5))
gypoints = gxpoints*2

#h(X)=3X
hxpoints = np.array(range(0,5))
hypoints = hxpoints*3


plt.plot(fxpoints, fypoints, label = 'f(x)') #label is used to call the axes something
plt.plot(gxpoints, gypoints, label = 'g(x)', color = 'red') #color is for 
#changing colour of the line
plt.plot(hxpoints, hypoints, label = 'h(x)', color = 'purple')

plt.legend() #to add a legend to the table
plt.show() # to show the table

#plt.savefig('plottask.png') to save this as a PNG file instead



