print("\n_______ Exercise 01 _______")
def sum_list(elements):
    sum=0
    for element in elements:
        sum+=element
    return sum
print(sum_list([1,2,-8]))
print(sum_list([10,12,20,22]))


print("\n_______ Exercise 02 _______")
def multiply(items):
    multi=1
    for x in items:
        multi*=x
    return multi
print(multiply([1,2,-8]))
print(multiply([3,1,2,3]))


print("\n_______ Exercise 03 _______")
def largestNum(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(largestNum([1,2,-8,0]))
print(largestNum([8,-5,22,-3]))


print("\n_______ Exercise 04 _______")
def smallestNum(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min
print(smallestNum([1,2,-8,0]))
print(smallestNum([8,-3,22,12]))


print("\n_______ Exercise 05 _______")
def match_words(items):
    match=0
    for word in items:
        if (len(word) >= 2) and (word[0]==word[-1]):
            match+=1
    return match
print(match_words(['abc','xyz','aba','1221']))
