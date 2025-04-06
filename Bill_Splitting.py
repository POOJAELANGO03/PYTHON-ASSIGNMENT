try:
    total_bill = float(input("Enter the total bill amount: $"))
    num_friends = int(input("Enter the number of friends splitting the bill: "))

    if total_bill <= 0 or num_friends <= 0:
        print("\nTotal bill and number of friends must be greater than zero.")
    else:
        print("\nCalculating...")
        if total_bill > 200:
            discount = total_bill * 0.10
            total_bill -= discount
            print(f"🎉 A 10% discount has been applied! You saved: ${discount:.2f}")

        per_person = total_bill / num_friends
        print(f"\nEach friend should pay: ${per_person:.2f}")
except ValueError:
    print("\nInvalid input! Please enter numeric values.")
