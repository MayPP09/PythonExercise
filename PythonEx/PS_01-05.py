print("_______Exercise 001_______")
print("Calculating the length of string")
string= "w3resource.com"
print("solution 1 :",len(string))

def string_length(str1):
    count=0
    for char in str1:
        count += 1
    return count
print("solution 2 :", string_length(string))



print("\n\n_______Exercise 002_______")
print("Counting character frequency")
def char_frequency(str2):
    dict={}
    for i in str2:
        keys=dict.keys()    #retrive the keys (unique characters) in the dict
        if i in keys:
            dict[i] += 1


print("\n_______ Exercise 03 _______")
def newString(string):
    result=""
    if len(string)>=2:
         result=string[0:2]+string[-2:]
    return result
print("The new string is - ", newString("w3resource"))
print("The new string is - ", newString("w3"))
print("The new string is - ", newString("w"))


print("\n_______ Exercise 04 _______")
def change(str):
    char=str[0]
    str=str.replace(char,"$")
    str=char+str[1:]
    return str
print("The changed string - ", change("restart"))


print("\n_______ Exercise 05 _______")
def swap(a,b):
    str1=b[:2]+a[2]
    str2=a[:2]+b[2]
    return str1+" "+str2
print("The swapped string - ", swap('abc','xyz'))
