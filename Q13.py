balance = float(input("Enter balance: "))
amount = float(input("Enter amount to withdraw: "))

if amount <= balance and amount % 100 == 0:
    print("Withdrawal allowed")
else:
    print("Withdrawal denied")