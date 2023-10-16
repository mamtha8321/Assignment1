#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
t = tuple(map(lambda a : a + 25, (10,)))
print(t)

# Write a Python program to triple all numbers of a given list of integers. Use Python map.
num=list(map(lambda x: 3*x, [1, 2, 3, 4, 5, 6, 7]))
print(num)


# Find the Squares from the given list using map() with lambda function.
l=list(map(lambda n:n**2, [4,5,2,9]))
print(l)