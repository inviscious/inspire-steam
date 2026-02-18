# Name : James Karuri
# Date: 17/02/2026
# Program to draw a diamond shape using asterisks

n = 5 # number of rows
# upper half of the diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
# lower half of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


# Program to draw a triangle shape using asterisks
n = 5 # number of rows
print("__________________________________________________________________")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Program to calculate the quadratic formula
import math
a = 1
b = -3
c = 2
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The roots are real and equal: {root}")
