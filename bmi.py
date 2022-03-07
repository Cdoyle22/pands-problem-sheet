#calculate somebody's Body Mass Index (BMI). 
#Author: Ciara Doyle

weight= float(input('Enter weight (kg):'))
height= float(input('Enter height (cm):'))

BMI= weight / ((height/100) ** 2)
print(BMI)

