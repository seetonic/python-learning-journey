email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index+1:]

print(f"your username is {username} and your domain name is {domain}.")