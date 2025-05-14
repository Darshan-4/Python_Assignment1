
password = input("Enter password: ")

if len(password) >= 8 and '@' in password:
    print("Strong password")
else:
    print("Weak password")
