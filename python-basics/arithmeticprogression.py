# Name : James Karuri
# Date: 11/02/2026
# Program to calculate arithmetic progression

# Calculating the nth term

a = int(input("enter the first number :"))
n = int(input("enter the number of terms :"))
d = int(input("enter the common difference :"))

nth_term = (a) + (n-1) * (d)
sn = (n/2) * (2*a + (n-1)*d) 
print(f"The nth term is : {nth_term}")
print(f"The sum of the first n terms is : {sn}")