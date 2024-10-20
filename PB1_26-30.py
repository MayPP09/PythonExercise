print("\n_______ Exercise 26 _______")
def histogram(items):
    for i in items:
        print("@"*i, end="")
        print(" ")
histogram([2,3,6,5])


print("\n_______ Exercise 27 _______")
def to_string(list):
    result=""
    for i in list:
        result=result+str(i)
    return result
print(to_string([1,5,12,2]))


print("\n_______ Exercise 28 _______")
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for i in numbers:
    if i == 237:
        print(i)
        break
    elif i%2==0:
        print(i)


print("\n_______ Exercise 29 _______")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print("Original set elements")
print(color_list_1)
print(color_list_2)

print("\n Difference of color_list_1 and color_list_2")
print(color_list_1.difference(color_list_2))

print("\nDifference of color_list_2 and color_list_1")
print(color_list_2.difference(color_list_1))


print("\n_______ Exercise 30 _______")
b=int(input("Enter the base: "))
h=int(input("Enter the height: "))
A=(1/2)*b*h
print("Area of the triangle is ", A)
