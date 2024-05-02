class Restaurant:
    """A simple attempt to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value set to 0
        
    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"The restaurant name is {self.restaurant_name.title()} and the cuisine type is {self.cuisine_type.title()}.")
        
    def open_restaurant(self):
        """Announce that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open!")
        
        
    def set_number_served (self, number):
        """Set the number of customers that have been served, ensuring it does not decrease."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print(f"Error: You cannot decrease the number of customers served. The last reading was {self.number_served}.")
            
    def increment_number_served(self, customers_incremented):
        self.number_served += customers_incremented
            
    def served(self):
        """Print the number of customers the restaurant has served."""
        print(f"The amount of customers served is {self.number_served}.")
        
# Create an instance of Restaurant
restaurant = Restaurant('chipotle', 'fast food')

# Using the Restaurant class methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.served() # Initially 0 customers served

# Correctly using the number_of_customers method to update the number served
restaurant.set_number_served(12)
restaurant.served() # Now prints 12 customers served

# Attempting to set a lower number, which should trigger an error message
restaurant.set_number_served(1) # This should not decrease the number and print an error
restaurant.served() # The count remains at 12 due to the safeguard in number_of_customers

restaurant.increment_number_served(40)
restaurant.served()