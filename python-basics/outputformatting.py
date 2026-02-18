# Name : James Karuri
# Date: 17/02/2026
# Program to format the output in different styles

name = "James Karuri"

weight = "68" # weight in kgs

fav_team = "Manchester United"

height = "174.0" # height in cm

# 1. Format using printf(f"{}")

print(f"My name is {name} and I weigh {weight} kgs")

# 2. Using f string
text = f"My name is {name} and I support {fav_team}"
print (text)

# 3. Using kali brackets {} and format method ( .format())

print("My name is {0} and I am {1} cm tall".format(name, height))   

# 4. Using output specifiers ( %s for string, %d for integers and %f for floats)

import math
print("The approximate value of pi is %f" % math.pi)
print("I support %s" % fav_team)