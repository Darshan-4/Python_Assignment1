age = int(input("Enter age: "))

if age >= 21:
    print("Can vote and drive")
elif age >= 18:
    print("Can vote")
else:
    print("Not eligible")