#ATM Transaction Sequence Simulation
balance = float(input("Enter initial balance: "))

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")