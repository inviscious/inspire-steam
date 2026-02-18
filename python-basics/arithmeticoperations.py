# Name : James Karuri
# Date: 17/02/2026
# Program to perform arithmetic operations

f_number = 8 # first numner
s_number = 13 # second number
sum_numbers = f_number + s_number 
diff_numbers = f_number - s_number
product_numbers = f_number * s_number
quotient_numbers = f_number / s_number

print("The sum of the numbers %d" % sum_numbers)
print("The difference of the numbers %d" % diff_numbers)
print("The product of the numbers %d" % product_numbers)
print("The quotient of the numbers %0.1f" % quotient_numbers)

# modulus/remainder operator
print (7%5)

# Even and odd numbers
for x in range(0,20):
    print (x)
    if x%2 == 0:
        print(f"{x} is an even number")
    elif x%2 == 1:
        print(f"{x} is an odd number")
