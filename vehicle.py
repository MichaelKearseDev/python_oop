class Vehicle:
    
    def __init__(self, color_of_car, age_of_car, seats_in_car):
        self.color = color_of_car
        self.age = age_of_car
        self.seats = seats_in_car
        
    def __str__(self):
        return f"My car is a {self.color.title()} car, it is {self.age} years old and it has {self.seats} seats in it."
        
    def get_color(self):
        return f"The color of the car is {self.color.title()}"
    
    def get_age(self):
        return f"The car is {self.age} years old."
    
    def get_seats(self):
        return f"There are {self.seats} seats in the car."
    
my_mustang = Vehicle("black", "5", 2)
print(my_mustang)

print(my_mustang.get_age())
print(my_mustang.get_color())
