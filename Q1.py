bill = float(input("Enter bill amount: "))
if bill > 1000:
    bill *= 0.8
elif bill > 500:
    bill *= 0.9
print("Final amount:", bill)