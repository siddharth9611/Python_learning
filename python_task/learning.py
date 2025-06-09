# Write a Python script that takes two numbers as input from the user, adds them, and prints the result
a = int(input("enter the first number"))
b = int(input("enter the second number"))
sum = a+b
print("sum =", sum)

# Given the radius of a circle, calculate and print its area using the formula
r = 7
area =  3.14159*r*r
print("area of circle is:", area)

# Write a program that takes an integer input and checks if it is even or odd.
a = int(input("enter the numebr"))
if a == 0:
    print("enter the correct numebr")
elif a%2 == 0:
    print("even")
else:
    print("odd")

# Write a script that checks whether a given year is a leap year or not.
y = 2024
if y%4 == 0:
    print("leap year")
else:
    print("not")

# Print the first 10 natural numbers using a for loop
for i in range (1, 11):
    print(i, end=" ")

# Print the multiplication table of a number entered by the user
a = int(input("enter the numebr"))
for i in range (1, 11):
    print(f'{a} X {i} = {a*i}')

# Write a function calculate_square(n) that returns the square of a number.
def calculate_square(n):
    return n*n

print(calculate_square(6))

# Write a script to print the current working directory using the os module.
