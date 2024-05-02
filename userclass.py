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