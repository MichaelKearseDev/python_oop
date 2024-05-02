"""Can't import 9-8privileges.py cause of the numbers, so I added the class here to import it for my 9-11 assignment. Cheers!"""

class User:
    
    def __init__(self, first_name, last_name, email, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username 
        self.location = location
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"User Profile: \nFirst Name: {self.first_name.title()}\nLast Name: {self.last_name.title()}\nEmail: {self.email}\nUsername: {self.username.title()}\nLocation: {self.location.title()}\n")
        
        
    def greet_user(self):
        print(f"Welcome back, {self.first_name.title()} {self.last_name.title()}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):
    
    def __init__(self, first_name, last_name, email, username, location):
        super().__init__(first_name, last_name, email, username, location)
        """Set the attribute to store the list os strings aka the privileges."""
        self.privileges = Privileges()
        
class Privileges:
    
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"] 
        
    def show_privileges(self, username):
        print(f"Privileges for {username.title()}")
        for privileges in self.privileges:
            print(f"- {privileges}")