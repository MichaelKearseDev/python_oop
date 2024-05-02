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
        """Set the attribute to store the list of strings aka the privileges."""
        self.privileges = Privileges()
        
class Privileges:
    
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"] 
        
    def show_privileges(self, username):
        print(f"Privileges for {username.title()}")
        for privileges in self.privileges:
            print(f"- {privileges}")
        
user1 = User("michael", "kearse", "itsmjb247@gmail.com", "itsmjb", "chicago")
user2 = User("john", "doe", "johndoe123@yahoo.com", "johndoe123", "texas")
user3 = User("alex", "james", "alexjames247@gmail.com", "alexjames", "california")

user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()

user4 = Admin("jack", 'jones', 'jackj8@aol.com', 'jackj88', 'nebraska')
user4.privileges.show_privileges(user4.username)

"""This sets the login attempts for user3 from 0 to 50. Then increments it +1 so it will output 51 attempts"""
user3.login_attempts = 50
user3.increment_login_attempts()
print(user3.login_attempts)

"""This will reset the login attempts back to 0."""
user3.reset_login_attempts()
print(user3.login_attempts)
