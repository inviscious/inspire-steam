# Name : James Karuri
# Date: 16/02/2026
# Program to do show for loops in python

import math

for x in range(1,10):
        print(x)

for x in range(0,360,30):
        print(math.cos(x))
        print(math.sin(x))
        print(math.tan(x))

for i in range(10,0,-1):
        print(i)

for y in range(-180,180,30):
        print(math.cos(y))
        print(math.sin(y))
        print(math.tan(y))


print("__________________________________________________________________")
print("| cos x | sin x | tan x |")
print("------------------------------------------------------------------") 
for x in range(-180,180,30):
        print("|", math.cos(x), "|", math.sin(x), "|", math.tan(x), "|")
print("___________________________________________________________________")
