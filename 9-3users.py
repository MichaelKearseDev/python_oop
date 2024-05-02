class User:
    
    def __init__(self, first_name, last_name, email, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.location = location
        
    def describe_user(self):
        print(f"User Profile: \nFirst Name: {self.first_name.title()}\nLast Name: {self.last_name.title()}\nEmail: {self.email}\nUsername: {self.username.title()}\nLocation: {self.location.title()}\n")
        
        
    def greet_user(self):
        print(f"Welcome back, {self.first_name.title()} {self.last_name.title()}")
        
user1 = User("michael", "kearse", "itsmjb247@gmail.com", "itsmjb", "chicago")
user2 = User("john", "doe", "johndoe123@yahoo.com", "johndoe123", "texas")


user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()