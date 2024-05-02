class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()} and the cuisine type is {self.cuisine_type.title()}")
        
        
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")
        

restaurant = Restaurant('chipotle', 'fast food')
restaurant2 = Restaurant('red lobster', 'sea food')
restaurant3 = Restaurant('marias', 'mexican food')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()