#Decorator-based Access Control 
'''Scenario: 
Restrict access to certain functions. 
Task: 
● Create a decorator to check user role 
● Use condition inside decorator 
● Apply decorator to multiple functions 
● Store roles in a dictionary'''
roles = {
    "Rohith": "admin",
    "Amulya": "user"
}
def check_role(func):
    def wrapper(name):
        role = roles.get(name)
        if role == "admin":
            func(name)
        else:
            print("Access Denied for", name)
    return wrapper
@check_role
def delete_data(name):
    print(name, "can delete data")
@check_role
def view_data(name):
    print(name, "can view data")
delete_data("Rohith")
view_data("Amulya")