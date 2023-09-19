class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def user_info(self):
        print(f"Your username is {self.username} and email is {self.email}")

    def valid_email(email, users):
        for user in users:
            if user.email == email:
                return False
        return True

    def register_user(users):
        print("User Registration")
        while True:
            username = input("Enter username: ")
            email = input("Enter email address: ")
            if not User.valid_email(email, users):
                print("This email has already been used. Try another one.")
                continue
            password = input("Enter password: ")

            new_user = User(username, email, password)
            users.append(new_user)
            print("User registered successfully!")
            break

users = []
while True:
    User.register_user(users)
    another = input("Do you want to register another user? (yes/no): ")
    if another.lower() != "yes":
        break

print("\nRegistered Users:")
for idx, user in enumerate(users, start=1):
    print(f"User: {idx}")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Password: {user.password}")
