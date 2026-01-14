#!/usr/bin/env python3
from datetime import datetime
"""
Module: expense
Defines the Expense class and its methods.
"""

class Expense:
    """
    Represents an expense item.

    Attributes:
        id (str): Unique id for the expense
        name (str): Name or description of the expense
        amount (float): Amount of money spent
        category (str): Category of the expense
        date (datetime): Date of the expense
    """

    def __init__(
        self,
        id: str,
        name: str,
        amount: float,
        category: str,
        date: datetime
    ):
        """
        Initialize a new Expense instance.
        """
        self.id = id
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def edit(
        self,
        name=None,
        amount=None,
        category=None,
        date=None
    ):
        """
        Edit the attributes of the expense.
        """
        if name is not None:
            self.name = name

        if amount is not None:
            self.amount = amount

        if category is not None:
            self.category = category

        if date is not None:
            self.date = date

    def delete(self):
        """
        Placeholder for deletion logic.
        """
        # Actual deletion will be handled by storage/controller

    def to_dict(self):
        """
        Convert the Expense instance to a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.isoformat()
        }

