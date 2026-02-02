class user:
    def role(self):
        print("Normal user")

class Admin(user):
    def role(self):
        print("Admin user")

a = Admin()
a.role()