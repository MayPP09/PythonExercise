print("_______Exercise 01_______")
print("""
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
""")

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print("\n\n_______Exercise 02_______")
import sys
print("Python version: \n{}".format(sys.version))
print(f"Version info: \n{sys.version_info}")

print("\n\n_______Exercise 03_______")
import datetime
now=datetime.datetime.now()	#getting the current date and time
print("Current date and time in %c: \n{}".format(now.strftime("%c")))
print("Current time in individual: {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))

print("\n\n_______Exercise 04_______")
from math import pi 
radius=float(input("Please enter the measurement of the radius of the circle: "))
area=pi * radius**2
print(f"area of the circle {str(radius)} is: " + str(area))

print("\n\n_______Exercise 05_______")
firstName=input("Please enter your first name: ")
lastName=input("Please enter your last name: ")
fullName=print("Hello, " + lastName + " " + firstName)
