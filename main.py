#!/usr/bin/env python3
"""
script that include a selection Menu
"""
from fin_actions.expenses_dir.add_expenses import Addexpenses
from dp_actions.clean_terminal import Cleanterminal
class Main:
    """
    Class that include functions, for select, add, and show
    """
    def __init__(self):
        self.add_expenses = Addexpenses()
        self.clean_terminal = Cleanterminal()
    def selection(self):
        """
        function that recieve input to make an action
        """
        while True:
            print("Menu of actions")
            print("Option 1: add expenses")
            print("Option 2: show expenses")
            print("Option 3: clean terminal")
            print("Option 4: exit")
            select = input("\nInsert which action you want to do: ")
            print()

            if select == "1":
                print("Action 1 had been selected")
                self.add_expenses.adding_bills()
                print()
            elif select == "2":
                print("Action 2 had been selected")
                self.add_expenses.showing_bills()
                print()
            elif select == "3":
                print("Action 3 had been selected")
                self.clean_terminal.cleaning_terminal()
                print()
            elif select == "4":
                print("Action 3 had been selected")
                print("Finishing program! --> byee!")
                break
            else:
                print("Nothing had been selected")
                print("finishing program! --> bye!!")
                break


if __name__ == "__main__":
    app = Main()
    app.selection()
