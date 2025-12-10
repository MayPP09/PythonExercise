print("\n_______ Exercise 31 _______")
import math
import random
num1 = random.randint(0,99)
num2 = random.randint(30,120)
def gcd(x,y):
    return math.gcd(x,y)
print(f"Greatest Common Divisor of {num1} and {num2} is: ", gcd(num1, num2))


print("\n_______ Exercise 32 _______")
def lcm(x,y):
    return math.lcm(x,y)
print("The least common multipler is : ", lcm(336,360))

#Option2
def LCM(x,y):
    if x>y: #compare x and y to determine the larger number and store it in z
        z=x
    else:
        z=y
    
    while True:
        if (z%x==0) and (z%y==0):   #check if z is divisible by both x and y with no remainder
            lcm=z
            break
        z+=1    #if the conditions are not met, increment z and continue checking
    return lcm
print(LCM(4,6))
print(LCM(15,17))


print("\n_______ Exercise 33 _______")
def sum3(x,y,z):
    if x==y or x==z or y==z:
        sum=0
    else:
        sum=x+y+z
    return sum
print("Sum of 3 intergers is: ", sum3(2,1,2))
print("Sum of 3 intergers is: ", sum3(3,2,2))
print("Sum of 3 intergers is: ", sum3(2,2,2))
print("Sum of 3 intergers is: ", sum3(1,2,3))

print("\n_______ Exercise 34 _______")
def sum2(x,y):
    sum=x+y
    if 15<sum<20:
        return 20
    else:
        return sum
print("Sum of 2 is: ", sum2(10,6))
print("Sum of 2 is: ", sum2(10,2))
print("Sum of 2 is: ", sum2(10,12))


print("\n_______ Exercise 35 _______")
def test_number5(x,y):
    sum=x+y
    diff=abs(x-y)
    if x==y or sum==5 or diff==5:
        return True
    else:
        return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))
