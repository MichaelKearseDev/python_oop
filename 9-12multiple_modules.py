from privilegesclass import Admin, Privileges, User 

user1 = Admin('michael', 'kearse','itsmjb247@gmail.com', 'itsmjb', 'newport beach california')

user1.privileges.show_privileges(user1.username)

