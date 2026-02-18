# Name : James Karuri
# Date: 17/02/2026
# Program to show lists in python

friends = ["Sirius", "Orion", "Aquarius"]
print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Leo")
print(friends)

new_wives = ["Bob", "Stacy", "Augustine", "Alvin", "Elvis"]

print(len(new_wives))

# New list of students

students = friends + new_wives
print(students)

students.pop()
print(students)

students.insert(5, "Miranda")
print(students)

students.insert(9, "Kimberly")
print(students)

students.extend(["Freddy","Wendy","Emmy","Vivian"])
print(students)

students.remove("Freddy")  
print(students)

new_wives = students.copy()
print(new_wives)
