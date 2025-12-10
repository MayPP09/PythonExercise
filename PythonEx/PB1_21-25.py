print("\n_______ Exercise 21 _______")
num=int(input("Enter an integer: "))
if num%2==0:
    print("The number is an even number.")
else:
    print("The number is an odd number.")


print("\n_______ Exercise 22 _______")
def list_count(ls):
    count=0
    for i in ls:
        if i==4:
            count+=1
    return count
print(list_count([1,4,6,7,4]))
print(list_count([1,4,6,4,7,4]))


print("\n_______ Exercise 23 _______")
def substring_copy(text,n):
    if len(text) <=2:
        return text*n
    else:
        return text[:2]*n
print(substring_copy("abcdef",2))
print(substring_copy("p",3))
#option2 - https://www.w3resource.com/python-exercises/python-basic-exercise-23.php


print("\n_______ Exercise 24 _______")
def vowel(n):
    all_vowels="aeiou"
    for char in all_vowels:
        if n == char:
            return True
    return False
print(vowel("c"))
print(vowel("e"))


print("\n_______ Exercise 25 _______")
def is_group_member(num):
    group=[1,5,8,3]
    for i in group:
        if num == i:
            return True
    return False
print(is_group_member(3))
print(is_group_member(-1))
