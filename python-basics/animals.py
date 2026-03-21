# Name : James Karuri
# Date: 23/02/2026
# Program to show inheritence in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food
    
    def grow(self,weight):
        weight = 1.1* weight
        print(f"The animal weight  {weight} in kgs")
    
    def eat(self,food):
        print(f"The animal eats {food}")


class Dog(Animal):
    def __init__(self,species,weight,food,color,barks,breathe):
        super().__init__(species,weight,food)
        self.barks = barks
        self.breathe = breathe
    
    def bark(self,barks):
        print(f"The dog says woof woof")
    
    def breathe(self,breathe):
        print(f"The dog breathes")


class Horse(Animal):
    def __init__(self,species,weight,food,neigh,gallops):
        super().__init__(species,weight,food)
        self.neigh = neigh
        self.gallops = gallops
    
    def neigh(self,neigh):
        print(f"The horse {neigh}")
    
    def gallops(self,gallops):
        print(f"The horse {gallops}")