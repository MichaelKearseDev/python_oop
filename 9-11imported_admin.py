from privilegesclass import User, Privileges, Admin 

admin1 = Admin('michael', 'kearse', 'itsmjb247@gmail.com', 'itsmjb', 'chicago')

admin1.privileges.show_privileges(admin1.username)