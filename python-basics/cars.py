# Name : James Karuri
# Date: 23/02/2026
# Program to show classes in python

class Car():
    #  attributes of the car
    def __init__(self,model,make,color,year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year

    # print car details
    def print_details(self,model,make,color,year):
        print(f"{model} {make} of color {color} was manufactred in the year {year}")


#instantiate a class object

my_car = Car("Mercedes", "Maybach", "Grey", "2014")
my_car = Car("Lamborgini", "Urus", "Burgundy", "2018")

my_car.print_details("Mercedes", "Maybach", "Grey", "2014")