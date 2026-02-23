

# Tuples of fruits

fruits = ("Mango", "Banana", "Pineapple", "Apple")

print(len(fruits))
print(fruits[0])
print(fruits[3])
print(fruits[-1])

#  error-> fruits.append("Kiwi")

fruits_list = list(fruits)
fruits_list.append("Kiwi")
print(fruits_list)