try:
    acc_balance = float(input("Enter your account balance: $"))
    withdrawal_amount = float(input("Enter the withdrawal amount: $"))

    if withdrawal_amount <= 0:
        print("\nWithdrawal amount must be greater than zero.")
    elif withdrawal_amount > acc_balance:
        print("\nInsufficient funds!")
    else:
        acc_balance -= withdrawal_amount
        print("\nTransaction successful!")
        print(f"Updated Account Balance: ${acc_balance:.2f}")
except ValueError:
    print("\nInvalid input! Please enter numeric values.")
