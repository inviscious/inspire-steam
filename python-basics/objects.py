# Name : James Karuri
# Date: 19/02/2026
# Program to show objects in python

class Human:
    # First we deifne the attributes of a human
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True

    # We then create a constructor for the class/object
    # The constructor will be used to create copies of the object
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Ohayoo. I am {self.human_name}. Here is a story.")
        print("Causes of death are many. Accidents, sickness, old age.")
        print("But in that long morbid list stands one that is feared the most.")
        print("Death by fire.")

    # Create the humans
Frieren = Human ("Frieren", 20)
Cid = Human ("Cid", 18)
     
    # Let the humans created do things
Frieren.tell_story()
Cid.tell_story()

# Modify one if the objects, without modifying other objects
Frieren.city = "Tokyo"
Cid.city = "Nairobi"

print("Frieren's location", Frieren.city)
print("Cid's location", Cid.city) # This will give an error because Cid does not have the city attribute