name = input("Enter username: ")
role = input("Enter role: ")

if name in ['john', 'amy', 'sita'] and role in ['admin', 'manager']:
    print("Login success")
else:
    print("Login failed")