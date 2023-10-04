import re

def check_password_strength(password):
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'\d', password))
    sp_characters = bool(re.search(r'[!@#$%^&*()_+-{};:"]', password))

    score = 0

    if length:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if numbers:
        score += 1
    if sp_characters:
        score += 1

    return score

def main():
    user_password = input("check your password strength: ")

    user_score = check_password_strength(user_password)

    if user_score < 3:
        print("Your Password is weak.")
    elif user_score < 5:
        print("Your password is medium.")
    else:
        print("Your password is strong.")


if __name__ == "__main__":
    main()