Auth_users =["user1","user2","user3","user4"]
def  authorize(func):
        def wrapper():
            username = input("Enter your Username: ")
            if username in Auth_users:
                return func()
            else:
                print(f"{username} is not authorized")
        return wrapper

@authorize
def login():
    print("Logging in")

login()