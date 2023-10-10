#1. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


#2.Write a Python program to reverse a string.
# Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s
mystr = "1234abcd"
print("Given String: ", mystr)
print("Reversed String: ", reverse(mystr))

#Alternately
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd')) 

#3)Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

def countUpperAndLowerCase(sentence):
    upper = 0
    lower = 0
    for i in sentence:
        if i >= 'A' and i <= 'Z':
            upper += 1
        elif i >= 'a' and i <= 'z':
            lower += 1
    print("Upper case: " + str(upper))
    print("Lower case: " + str(lower))

countUpperAndLowerCase("The quick Brow Fox")

#without def

string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)







