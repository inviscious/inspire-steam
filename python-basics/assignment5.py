# Name : James Karuri
# Date: 16/02/2026
# Program to calculate income tax

salary = int(input("enter your salary :"))
if salary < 50000:
    tax = 0.025 * salary
    net_salary = salary - tax
if salary >= 50000 and salary < 100000: 
    tax = 0.045 * salary
    net_salary = salary - tax
else: 
    tax = 0.075 * salary
    net_salary = salary - tax
print(f"Gloss salary : {salary}")
print(f"Net salary : {net_salary}")
print(f"Tax : {tax}")