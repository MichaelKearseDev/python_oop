class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()} and the cuisine type is {self.cuisine_type.title()}")
        
        
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")
        
restaurant = Restaurant('chipotle', 'fast food')

print(f"Restaurant Name: {restaurant.restaurant_name.title()}")
print(f"Cuisine Type: {restaurant.cuisine_type.title()}\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()
