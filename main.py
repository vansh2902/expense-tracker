expenses = []

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4. Exit")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:

        try:
            amount = float(input("Enter your amount: "))
        except ValueError:
            print("Enter a valid amount!")
            continue

        category = input("Category: ")
        description = input("Description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Your expense added successfully!")

    elif choice == 2:

        print("YOUR EXPENSES:")

        for expense in expenses:
            print()
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("-------------------")

    elif choice == 3:

        if len(expenses) == 0:
            print("No expenses added yet!")
        else:
            total = sum(expense["amount"] for expense in expenses)
            print("Total expenses:", total)

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, or 4!")