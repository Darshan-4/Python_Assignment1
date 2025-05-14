number = int(input("Enter number: "))

if number % 2 == 0:
    if number % 5 == 0:
        print("Even and divisible by 5")
    else:
        print("Even and not divisible by 5")
else:
    if number % 5 == 0:
        print("Odd and divisible by 5")
    else:
        print("Odd and not divisible by 5")