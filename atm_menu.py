balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

if pin != correct_pin:
    print("Incorrect PIN")
else:
    amount = float(input("Enter amount to withdraw: "))

    # Check whether the requested amount is available in the account.
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful. New balance: {balance:.2f}")
    else:
        print("Insufficient funds")
