units = int(input("Enter units used: "))

if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
else:
    rate = 10

bill = units * rate
print("Bill:", bill)