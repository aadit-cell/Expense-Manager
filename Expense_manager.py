expenses = []

while True:
    print("------------------------------")
    print("Expense Manager")
    print("------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expense_category = input("Enter expense category: ")

        expense = {
            "name": expense_name,
            "amount": expense_amount,
            "category": expense_category
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        print("View Expenses selected")

        for expense in expenses:
            print(f"Name: {expense['name']}, Amount: ₹{expense['amount']}, Category: {expense['category']}")

    elif choice == "3":
        total_spending = sum(expense["amount"] for expense in expenses)
        print(f"Total Spending: ₹{total_spending}")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 4.")




