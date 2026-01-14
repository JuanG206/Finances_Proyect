#!/usr/bin/env python3
"""
Module: expense_controller
Handles all business logic related to Expenses stored as TXT.
"""

from datetime import datetime
from models.expense import Expense
from storage.file_manager import FileManager
from utils.helpers import generate_id


class ExpenseController:
    """
    Controller for Expense operations: add, modify, delete, list
    """

    def __init__(self):
        """Initialize the ExpenseController with FileManager"""
        self.file_manager = FileManager('data/expenses')

    def add_expense(self, name: str, amount: float, category: str,
                    date: str = None):
        """
        Create and save a new Expense as TXT.
        If no date is provided, assign today's date.

        Args:
            name (str): Expense name.
            amount (float): Expense amount.
            category (str): Expense category.
            date (str): Optional date in 'YYYY-MM-DD' format.

        Returns:
            Expense: Created Expense instance.
        """
        expense_id = generate_id()
        date_obj = datetime.fromisoformat(date) if date else datetime.today()
        expense = Expense(expense_id, name, amount, category, date_obj)
        data = {
            k: str(v) if not isinstance(v, str) else v
            for k, v in expense.to_dict().items()
        }
        self.file_manager.save(expense_id, data)
        return expense

    def list_expenses(self):
        """List all expenses (reads TXT files)."""
        return self.file_manager.load_all()

    def modify_expense(self, expense_id: str, **kwargs):
        """
        Modify an existing expense (updates TXT file).

        Args:
            expense_id (str): ID of the expense to modify.
            **kwargs: attributes to update
        """
        expense_data = self.file_manager.load(expense_id)
        if not expense_data:
            raise ValueError(f"Expense with ID '{expense_id}' not found")

        # Convert amount and date properly
        expense_data['amount'] = float(expense_data['amount'])
        expense_data['date'] = datetime.fromisoformat(expense_data['date'])
        expense = Expense(**expense_data)
        expense.edit(**kwargs)

        data = {
            k: str(v) if not isinstance(v, str) else v
            for k, v in expense.to_dict().items()
        }
        self.file_manager.save(expense_id, data)

    def delete_expense(self, expense_id: str):
        """Delete an expense TXT file by ID."""
        self.file_manager.delete(expense_id)
