x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    greatest = x
elif y >= x and y >= z:
    greatest = y
else:
    greatest = z

print("Greatest is:", greatest)