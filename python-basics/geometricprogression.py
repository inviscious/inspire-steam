# Name : James Karuri
# Date: 11/02/2026
# Program to calculate geometric progression

# Calculating the nth term

a = int(input("enter the first number :"))
n = int(input("enter the number of terms :"))
r = int(input("enter the common ratio :"))

nth_term = (a) * (r**(n-1))
sn = (a * (r**n - 1)) / (r - 1)
print(f"The nth term is : {nth_term}")
print(f"The sum of n terms is : {sn}")
