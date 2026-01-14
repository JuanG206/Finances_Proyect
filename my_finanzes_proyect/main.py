#!/usr/bin/env python3
"""
Main module for My Finanzes (Expenses only version)
Provides a simple terminal menu to manage Expenses using TXT files.
"""

from datetime import datetime
from controllers.expense_controller import ExpenseController


def add_expense(controller):
    """Add a new expense."""
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")
    expense = controller.add_expense(name, amount, category, date)
    print(f"Expense '{expense.name}' added successfully!")


def list_expenses(controller):
    """List all expenses."""
    expenses = controller.list_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n--- Expenses ---")
    for exp in expenses:
        print(
            f"ID: {exp['id']}, Name: {exp['name']}, Amount: {exp['amount']}\n"
            f"Category: {exp['category']}, Date: {exp['date']}"
        )
        print()


def modify_expense(controller):
    """Modify an existing expense."""
    expense_id = input("Enter Expense ID to modify: ")
    print("Enter new values (leave empty to keep current):")
    name = input("Name: ")
    amount = input("Amount: ")
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")

    updates = {}
    if name:
        updates['name'] = name
    if amount:
        updates['amount'] = float(amount)
    if category:
        updates['category'] = category
    if date:
        updates['date'] = datetime.fromisoformat(date)

    try:
        controller.modify_expense(expense_id, **updates)
        print("Expense modified successfully!")
    except ValueError as e:
        print(e)


def delete_expense(controller):
    """Delete an expense."""
    expense_id = input("Enter Expense ID to delete: ") 
    controller.delete_expense(expense_id)
    print("Expense deleted successfully!")


def main():
    """Main loop to interact with the user."""
    controller = ExpenseController()

    while True:
        print("\n===== MY EXPENSES =====")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Modify Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(controller)
        elif choice == "2":
            list_expenses(controller)
        elif choice == "3":
            modify_expense(controller)
        elif choice == "4":
            list_expenses(controller)
            print()
            delete_expense(controller)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
