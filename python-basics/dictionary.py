# Name : James Karuri
# Date: 17/02/2026
# Program to show dictionaries in python

cars = {"Model": "Audi", 
        "Make": "Q8", 
        "Color": "Burgundy", 
        "Year": 2025}
print(cars)

print(cars["Model"])
print(cars["Make"])
print(cars["Color"])
print(cars["Year"])

students = {"Gloria" : 19, 
            "Rose" : 18, 
            "Jeff" : 21}

for key in students:
    print(key)

for val in students.values():
    print(val)