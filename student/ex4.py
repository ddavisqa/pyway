# establishes the value of cars variable
cars = 100

# gives a value to the "space in a car" variable
space_in_a_car = 4.0

# gives a value to the number of drivers variable
drivers = 30

# gives a value to the number of passengers variable
passengers = 90

# calculates the number of cars not driven by subtracting drivers from cars
cars_not_driven = cars - drivers

# sets cars_driven variable equal to the number of drivers(drivers variable)
cars_driven = drivers

# determines how much space is available in each car for additional passengers
carpool_capacity = cars_driven * space_in_a_car


average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")