print("\n_______ Exercise 36 _______")
def add_numbers(x,y):
    if type(x)==int and type(y)==int:
        return x+y
    else:
        return "Inputs must be integers!"
print(add_numbers(10, 20))     # Valid: Both inputs are integers, and it returns the sum.
print(add_numbers(10, 20.23))  # Invalid: One of the inputs is a float, so it returns an error message.
print(add_numbers('5', 6))     # Invalid: One of the inputs is a string, so it returns an error message.
print(add_numbers('5', '6'))   # Invalid: Both inputs are strings, so it returns an error message.

#Option2
def add_num(a,b):
    if not(isinstance(a,int) and isinstance(b,int)):    #if either a or b is not an integer, return an error message.
        return "Inputs are not integer :("
    return a+b
print(add_num(10, 20))     
print(add_num(10, 20.23))  
print(add_num('5', 6)) 
print(add_num('5', '6'))


print("\n_______ Exercise 37 _______")
def personal_details():
    name= "Simon"
    age=19
    address="Bangalore, Karnataka, India"
    print("Name : {0} \nAge : {2} \nAddress : {1}".format(name, address, age))
personal_details()


print("\n_______ Exercise 38 _______")
x=4
y=3
result=(x+y)*(x+y)
print("({} + {}) ^ 2 = {})".format(x,y,result))


print("\n_______ Exercise 39 _______")
amt=10000
interest=3.5
years=7
future_value=amt*(1+(0.01*interest))**years
print(round(future_value,2))
"""
    The formula for future value with compound interest is FV = P(1 + r/n)^nt.
FV = the future value;
P = the principal;
r = the annual interest rate expressed as a decimal;
n = the number of times interest is paid each year;
t = time in years
"""


print("\n_______ Exercise 40 _______")
#Pythagoras theorem, c = sqrt(a^2 + b^2)
import math
p1=[4,0]
p2=[6,6]
distance=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(distance)
