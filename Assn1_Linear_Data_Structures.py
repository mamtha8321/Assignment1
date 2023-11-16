# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_allpairs(arr,sum):
    low = 0
    high =len(arr)-1
    while (low<high):
        if (arr[low]+arr[high]==sum):
            print("pair : (",arr[low],",",arr[high],")")
        if (arr[low]+arr[high]>sum):
            high -= 1
        else:
            low += 1

find_allpairs([1,2,3,4,5,6,7,8],10)


#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reversearr(arr,start):
    end = len(arr)-1
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end-=1
    print(arr)
reversearr([1,2,3,4,5,6],0,) 

#Q3. Write a program to check if two strings are a rotation of each other?

def checkrotation(A,B):
    temp = ' '
    if len(A) != len(B):
        return False
    temp =  A + B
    if B in temp:
        return True
    else:
        return False
A = 'asdf'
B = 'fdsa'

if checkrotation(A, B):
    print(f"{A} and {B} are rotations of each other.")
else:
    print(f"{A} and {B} are not rotations of each other.")


# Q4. Write a program to print the first non-repeated character from a string?
from collections import Counter
def mapping(string):
    d1 = Counter(string)

    d1 = {(key):(0 if d1[key]==1 else None) for key, value in d1.items()}
    return d1   
def first_non_repeated_char(s):
    d = mapping(s)
    nonrep = None
    for i in s:
        if d[i] is not None:
            nonrep = i
            break
            
    if nonrep is not None:
        return  nonrep
    else:
        return str("_")
print(first_non_repeated_char("mamatha"))

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
#The objective of the puzzle is to move the entire stack to another rod, obeying the following simple
# rules: Only one disk can be moved at a time

def TowerofHanoi(n,rod1,rod2,rod3):
    if n==1:
        print("move disk 1 from rod",rod1,"to rod",rod2)
        return
    TowerofHanoi(n-1,rod1,rod3,rod2)
    print("movedisk",n,"from rod",rod1,"to rod",rod2)
    TowerofHanoi(n-1,rod3,rod2,rod1)

n=4
TowerofHanoi(n,'A','B','C')

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression
#infix :- An infix is an affix inserted inside a word stem (an existing word or the core of a family of words). It contrasts with adfix, a rare term for an affix attached to the outside of a stem such as a prefix or suffix.
#Prefix:- An expression is called the prefix expression if the operator appears in the expression before the operands. ... Simply of the form (operand1 operand2 operator). Example : AB+CD-* (Infix : (A+B * (C-D) ) Given a Prefix expression, convert it into a Postfix expression.
# Postfix :- If we move the operators after the operands then it is known as a postfix expression.postfix expression can be defined as an expression in which all the operators are present after the operands.

def conversion(s):
    stack = []
    operators ={'+','/','-','*','^'}
    s =s[::-1]
    for i in s:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            
            temp = a+b+i

            stack.append(temp)
        else:
            stack.append(i)
    print(*stack)
conversion("*-A/SD-/QWE")

# Q7. Write a program to convert prefix expression to infix expression.

def conversion(s):
    stack = []
    operators ={'+','/','-','*','^'}
    s =s[::-1]
    for i in s:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            
            temp = "("+ a + i + b +")"

            stack.append(temp)
        else:
            stack.append(i)
    print(*stack)
conversion("*-A/BC-/AKL")

# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_closed(code_snippet):
    stack = []

    # Dictionary to store the mappings of opening and closing brackets
    bracket_mappings = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the code snippet
    for char in code_snippet:
        # If the character is a closing bracket
        if char in bracket_mappings:
            # Pop the top element from the stack if it's not empty; otherwise, assign a dummy value
            top_element = stack.pop() if stack else '#'

            # Check if the popped element matches the corresponding opening bracket
            if bracket_mappings[char] != top_element:
                return False
        else:
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)

    # The brackets are balanced if the stack is empty at the end
    return not stack

# Example :
code_snippet = "{[()]}"
if are_brackets_closed(code_snippet):
    print("All brackets are closed properly.")
else:
    print("Brackets are not closed properly.")

# Q9. Write a program to reverse a stack.

def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)

def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)

def createStack():
    stack = []
    return stack         

def isEmpty( stack ):
    return len(stack) == 0
 

def push( stack, item ):
    stack.append( item )
 

def pop( stack ):
 

    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()

def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)

# Q10. Write a program to find the smallest number using a stack.
class MinStack:
    def __init__(self):
        # Main stack to store elements
        self.stack = []
        # Auxiliary stack to store the minimum element at each level
        self.min_stack = []

    def push(self, value):
        # Push the element onto the main stack
        self.stack.append(value)

        # Update the minimum stack
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        # Pop the element from the main stack
        popped_element = self.stack.pop()

        # If the popped element is the minimum, update the minimum stack
        if popped_element == self.min_stack[-1]:
            self.min_stack.pop()

        return popped_element

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print("Smallest number:", stack.get_min())  # Output: Smallest number: 1

stack.pop()
print("Smallest number:", stack.get_min())  # Output: Smallest number: 2
