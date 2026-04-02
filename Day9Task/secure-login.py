#Secure Login System (Decorators) 
#A web application wants to ensure that users are authenticated before accessing sensitive functions. Create a decorator that checks whether the user is logged in before allowing access to a function. 
def login_required(func):
    def wrapper(user_logged_in):
        if user_logged_in:
            func(user_logged_in)
        else:
            print("Access denied. Please log in first.")
    return wrapper

@login_required
def view_account(user_logged_in):
    print("Welcome! You can access your account details.")

status = input("Are you logged in? (yes/no): ").lower()

if status == "yes":
    view_account(True)
else:
    view_account(False)