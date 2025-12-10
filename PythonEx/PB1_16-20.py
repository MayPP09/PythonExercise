print("\n_______ Exercise 16 _______")
import math
num1 = int(input("Enter a number: "))
num2 = 17
diff = num1-num2
if num1>num2:
    result=2*diff
    print(result)
else:
    result=math.ceil(math.fabs(diff))
    print(result)


print("\n_______ Exercise 17 _______")
n=int(input("Enter a number between 800-2200: "))
diff1=abs(1000-n)
diff2=abs(2000-n)
def near_thousand(n):
    return(diff1 <=100) or (diff2 <=100)
print(near_thousand(n))


print("\n_______ Exercise 18 _______")
def sumOf3(x,y,z):
    sum=x+y+z
    if x==y==z:
        sum=3*sum
    return sum
print(sumOf3(1,2,3))
print(sumOf3(3,3,3))


print("\n_______ Exercise 19 _______")
def new_string(text):
    if text[:2] == "Is":
        return text
    else:
        return "Is"+text
print(new_string("Array"))
print(new_string("IsEmpty"))


print("\n_______ Exercise 20 _______")
def copy(text,num):
    return text*num
print(copy(".test",3))
#option2 - from the web
def string(text,n):
    Result= ""  #initializing an empty string
    for i in range(n):
        Result=Result+text
    return Result
print(string(".abc",2))
print(string(".py",5))
