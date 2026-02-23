# Name : James Karuri
# Date: 19/02/2026
# Program to show functions in python

def cook_egg():
    oil = "20ml"
    pan = "hot"
    moto = "on"
    eggs = 2

    print(f"The pan is {pan}, and the fire is {moto}, add {oil} of oil, and add {eggs} eggs to the pan")

print("Here is the statement 1")

print("Here is the statement 2")

cook_egg()

print("Here is the statement 3")

# Ride fare creating function

def calculate_fare(route,distance,is_rush_hour):
    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5
    print(f"The fare to {route} is {fare}")

    return fare

calculate_fare("Juja-Allsops", 7, True)


# Passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")
    
all_interests = ["Star gazing", "Reading novels", "Moon bathing", "Poetry", "Meditation"]

write_all_interests(all_interests)