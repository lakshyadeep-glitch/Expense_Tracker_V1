# this is a simple expense tracker program that allows users to add expenses, view expenses, and show the total amount spent. The program uses a list to store expenses, where each expense is represented as a dictionary containing the category, amount, and description.
"""
1. Add Expense
2. View Expenses
3. Show Total
4. Exit"""

expenses = []

while True:

    print("Welcome to the Expense Tracker!")
    print("Please select an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    opt = int(input("Enter your choice (1-4): "))

    # add expense function
    def add_expense():

        ent = int(input("Enter the number of expenses you want to add: "))

        for i in range(ent):

            Catg = input("Enter category: ")
            Amt = float(input("Enter amount: "))
            Des = input("Enter description: ")

            expense = {
                "category": Catg,
                "amount": Amt,
                "description": Des
                }

            expenses.append(expense)

        print("Expenses added successfully!")
        save_expenses()
    
    # view expenses function
    def view_expenses():
        if opt == 2:
            print("Expenses:")
            for expense in expenses:
                print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

    # show total function
    def show_total():
        if opt == 3:
            total = sum(expense['amount'] for expense in expenses)
            print(f"Total amount spent: {total}")

    def exit_program():
        if opt == 4:
            print("Are you sure you want to exit? (y/n)")
            confirm = input().lower()
            if confirm == 'y':
                print("Exiting the program. Goodbye!")
                exit()
            else:
                print("Returning to the main menu.")
                return
    
    def save_expenses():

        file = open("expenses.txt","+a")

        for expense in expenses:

            file.write(
                f"{expense['category']},"
                f"{expense['amount']},"
                f"{expense['description']}\n"
                )

        file.close()
        
    if opt == 1:
        add_expense()
    elif opt == 2:
        view_expenses()
    elif opt == 3:
        show_total()
    elif opt == 4:
        exit_program()