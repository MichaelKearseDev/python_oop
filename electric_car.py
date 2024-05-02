from car import Car

"""Just testing that the Car class was imported."""
# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(98)
# my_new_car.read_odometer()


class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}--kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
            
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        
        if self.battery_size <= 65:
            self.battery_size = 65
        print(f"Your car's battery has now been upgraded to: {self.battery_size}")
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks. Assume the Car class had a fill_gas_tank method. This would override the method 
        for the ElectricCar class."""
        print("This car doesn't have a gas tank!")
        
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

"""Testing the upgrade_battery() function"""
# my_tesla = ElectricCar('tesla', 'model 3', 2022)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()