"""Can't import 9-1restaurant.py cause of the numbers, so I added the class here to import it for my 9-10 assignment. Cheers!"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()} and the cuisine type is {self.cuisine_type.title()}")
        
        
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")