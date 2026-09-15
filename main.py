accounts = {}

while True:
    print("\n1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Account Name: ")
        accounts[name] = 0
        print("Account Created")

    elif choice == "2":
        name = input("Name: ")
        amount = float(input("Deposit Amount: "))
        accounts[name] += amount
        print("Deposited Successfully")

    elif choice == "3":
        name = input("Name: ")
        amount = float(input("Withdraw Amount: "))
        if accounts[name] >= amount:
            accounts[name] -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        name = input("Name: ")
        print("Balance:", accounts[name])

    elif choice == "5":
        break
