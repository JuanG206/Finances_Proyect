#!/usr/bin/env python3
"""
Super class expenses
"""
from fin_actions.expenses_dir import Addexpenses 

class ShowExpenses:
    """
    Class that use the location from the file, and calls an
    object to get the Json file
    """
    def __init__(self, add_expenes_instance):
        self.json_path = add_expenes_instance
    def showing_bills(self):
        """
        Function that extract the instance pointing to a directory path
        and manipulate it to find my json file
        """
        json_path = self.json_path.directory

