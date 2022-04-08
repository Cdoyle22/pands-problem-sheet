#calculate somebody's Body Mass Index (BMI). 
#Author: Ciara Doyle

weight= float(input('Enter weight (kg):'))
# this asks for input which will be the weight used in kg
height= float(input('Enter height (cm):'))
# this asks for input which will be the height used in cm

BMI= weight / ((height/100) ** 2)
# this calculates the BMI based on the standard calculation of BMI = kg/m2 
#(This also includes changing cm to m2)
# ref: https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator#:~:text=Body%20Mass%20Index%20is%20a,most%20adults%2018%2D65%20years.

BMIx= round(BMI, 2)
# this will limit the numbers after the decimal point to 2

print ('The BMI is (kg/m2)', BMIx)
# This will print out the answer
