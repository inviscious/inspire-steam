# Name : James Karuri
# Date: 16/02/2026
# Program to calculate the factorial of a number

number = int(input("enter the number x:")) # this will capture the number
factorial = 1 # initilize the factorial
for x in range(1,number+1):
    factorial *= x # this will calculate the factorial of the number
print(f"{number}! = {factorial}")