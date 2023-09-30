#1)Python program to get the Fibonacci series between 0 to 50
# Using while Loop

num=int(input("Please enter the Range:"))
i=0
first_num=0
second_num=1

while (i<num):
    if (i<=1):
        fibonacci=i
    else:
        fibonacci=first_num+second_num
        first_num=second_num
        second_num=fibonacci
    print(fibonacci)
    i=i+1

#  We have initialized 3 variables - i, first_num and second-num
#  While Loop starts from 0 and ends till less than the given range
#  Used If statement within while loop- If i value is less than or equal
#  to 1, then fibonacci=i
#  If i value is greater than 1, it performs else block conditions


# Iterations:For example taken 5 for the purpose of iterations
# first iter:
# while 0<5 = True then it executes if statement in while loop
# if 0<=1= True
# fibonacci=0 then it comes to print fibonacci & print value as 0
# Then i=0+1=1>5

# 2nd iter:
# while 1<5 = True then it executes if statement in while loop
# if 1<=1= True
# fibonacci=1 then it comes to print fibonacci & print value as 1
# Then i=2>5

# 3nd iter:
# while 2<5 = True then it executes if statement in while loop
# if 2<=1= False
# Then it comes to else block
# fibonacci=0+1=1
# first_num=second_num=1
# second_num=fibonacci=1 & prints fibonacci as 1  
# Then i=3>5

# 4th iter:
# while 3<5 = True then it executes if statement in while loop
# if 3<=1= False
# Then it comes to else block
# fib0nacci=1+1=2
# first_num=second_num=1
# second_num=fibonacci=2, & prints fibonacci as 2 
# Then i=4>5

# 5th iter:
# while 4<5 = True then it executes if statement in while loop
# if 4<=1= False
# Then it comes to else block
# fib0nacci=1+2=3
# first_num=second_num=2
# second_num=fibonacci=3, & prints fibonacci as 3 
# Then i is incremented to 5

# As 5 < 5 is false, it exits from while loop


# Using for Loop

num=int(input("Please enter the Range:"))

first_num=0
second_num=1
for i in range(0,num):
    if(num<=1):
        fibonacci=num
    else:
        fibonacci=first_num+second_num
        first_num=second_num
        second_num=fibonacci
    print(fibonacci)
    i=i+1
    
#2)Python program that accepts a word from the user and reverse it. 
# Input-Edyoda Output-adoydE
# Using for Loop

string1=input("Enter the string to get reversed:")
string2=" "
index=-1
for i in string1:
    string2=string2+string1[index]
    index=index-1
print("The Mirror Image of Given String ",string1,"is",string2)

#  We have initialized index as -1
#  For Loop starts working for string1. Example: "Edyoda"
#  string2= string2+string1[-1], then string2 stores "a" for 1st Iter
#  Then index=-1-1=-2,then string2 stores"ad" for 2nd Iter
#  Then index=-2-1=-3,then string3 stores"ado" for 3rd Iter
#  Then index=-3-1=-4,then string3 stores"adoy" for 4th Iter
#  Then index=-4-1=-5,then string3 stores"adoyd" for 5th Iter
#  Then index=-5-1=-6,then string3 stores"adoydE" for 6rd Iter

#3)Write a Python program to count the number of even and odd numbers
#  from a series of numbers.

max=int(input("Please enter the range of numbers:"))
for number in range(1,max+2):
    if(number%2!=0):
        print(number,"is odd")
        
    else:
        print(number,"is even")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)









