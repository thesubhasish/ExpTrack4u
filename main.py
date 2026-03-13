# ExpTRack4u - A simple command-line expense tracker application
expenses_list = [] 
print("Welcome to the Expense Tracker")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    # Error handling for correct option
    try:
        choice = int(input("Please enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number from the menu.")
        continue

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter the date (e.g., YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Travel, Utilities, Books): ")
        description = input("Enter a brief description: ")
        
        # Error handling for input ammount value
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses_list.append(expense)
        print("\nSuccess: Expense added successfully.")

    # 2. VIEW ALL EXPENSES 
    elif choice == 2:
        if len(expenses_list) == 0:
            print("\nNo expenses recorded yet. Please add an expense first.")
        else:
            print("\n===== All Expenses ======")
            
            for count, expense_item in enumerate(expenses_list, start=1):
                
                print(f"Expense #{count} -> Date: {expense_item['date']}, Category: {expense_item['category']}, Description: {expense_item['description']}, Amount: {expense_item['amount']:.2f}")

    # 3. VIEW TOTAL SPENDING 
    elif choice == 3:
        
        total = sum(expense_item['amount'] for expense_item in expenses_list)
        print(f"\nTOTAL EXPENSES = {total:.2f}")

    # 4. EXIT 
    elif choice == 4:
        print("\nThank you for using the Expense Tracker. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please select an option between 1 and 4.")