print("\n_______ Exercise 11 _______")
print("abs function: ", abs.__doc__)
print("len function: ", len.__doc__)
print("sorted function: ", sorted.__doc__)
print("map function: ", map.__doc__)


print("\n_______ Exercise 12 _______")
import calendar
year=int(input("enter year: "))
month=int(input("enter month: "))
print(calendar.month(year,month))


print("\n_______ Exercise 13 _______")
print(""" 
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")


print("\n_______ Exercise 14 _______")
from datetime import date
date1=date(2012,7,7)
date2=date.today()
delta=date2-date1
print("total number of days: ",delta.days)
print("total time: ", delta)


print("\n_______ Exercise 15 _______")
from math import pi
r=6
V=4/3 *pi* r**3
print("The volume of the sphere is ",V)
print("Round up volume of the sphere is ", int(V))
