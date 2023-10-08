#Importing the math module to access mathematical functions.
import math
#Getting user input for the radius of the circle and converting it to a float
radius= float(input("Enter the radius of the circle :"))
#Calculating the area of the circle using the formula πr^2
area= math.pi * (radius**2) 
#Printing the calculated area along with a formatted string showing radius.
print(f"the area of the circle with radius{radius} is:{area}")