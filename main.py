
# Expense Tracker
# Features: Add expenses, view expenses, show total, and save expenses.

expenses = []


def add_expense():
    try:
        ent = int(input("Enter the number of expenses you want to add: "))

        if ent <= 0:
            print("Error: Enter a number greater than zero.")
            return

    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    for i in range(ent):
        print(f"\nExpense {i + 1}")

        Catg = input("Enter category: ").strip()

        while True:
            try:
                Amt = float(input("Enter amount: "))

                if Amt < 0:
                    print("Error: Expense amount cannot be negative.")
                    continue

                break

            except ValueError:
                print("Error: Please enter a valid number.")

        Des = input("Enter description: ").strip()

        expense = {
            "category": Catg,
            "amount": Amt,
            "description": Des
        }

        expenses.append(expense)

    print("\nExpenses added successfully!")
    save_expenses()


def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print(f"Category: {expense['category']}")
        print(f"Amount: {expense['amount']:.2f}")
        print(f"Description: {expense['description']}")

    print("==============================")


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal amount spent: {total:.2f}")


def save_expenses():
    # Save the complete list instead of appending duplicate records.
    import csv

    with open("expenses.txt", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["category", "amount", "description"]
        )
        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved successfully!")


def load_expenses():
    import csv

    try:
        with open("expenses.txt", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                amount = float(row["amount"])

                # Ignore invalid negative records in the saved file.
                if amount < 0:
                    continue

                expenses.append({
                    "category": row["category"],
                    "amount": amount,
                    "description": row["description"]
                })

    except FileNotFoundError:
        pass
    except (ValueError, KeyError) as error:
        print(f"Warning: Some saved data could not be loaded: {error}")


def exit_program():
    confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()

    if confirm == "y":
        save_expenses()
        print("Exiting the program. Goodbye!")
        return True

    print("Returning to the main menu.")
    return False


# Load saved expenses when the program starts.
load_expenses()

while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")
    print("=====================================")

    try:
        opt = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Error: Please enter a number from 1 to 4.")
        continue

    if opt == 1:
        add_expense()

    elif opt == 2:
        view_expenses()

    elif opt == 3:
        show_total()

    elif opt == 4:
        if exit_program():
            break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
