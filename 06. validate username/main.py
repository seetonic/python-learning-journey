# validate username
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("your username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("your username can't be contain spaces.")
elif not username.isalpha():
    print("your username can't be cotain digits.")
else:
    print(f"welcome {username}")