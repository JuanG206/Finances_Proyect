#!/usr/bin/env python3
"""Sub class been called in my main class"""
import uuid
from datetime import datetime
from dp_actions.create_dictionary import CreateDictionary
from dp_actions.save_to_json import Save

class Addexpenses:
    """
    class with an object that represent a diccionary with add_bills method
    """
    def __init__(self, directory="fin_actions/expenses_dir/Bills_register"):
        self.directory = directory
        self.bills = CreateDictionary().create_dictionary()


    def adding_bills(self):
        """
        This metod expect an input to then append it into an object(diccionary)
        """
        while True:
            msg = (
                    "Insert your expenses (format:name,value,time:dd.mm.yyyy) "
                    "or just ENTER to finish: "
              )
            expenses = input(msg)

            data_title = "bills"

            if expenses == "":
                if not self.bills:
                    print("expenses no added")
                else:
                    print("\nExpenses added successfully!")
                    for expense_id, data in self.bills.items():
                        print(f"\nExpense ID: {expense_id}")
                        for key, value in data.items():
                            print(f"{key}: {value}")
                    save = Save(self.directory)
                    save.savetojson(self.bills, data_title)
                break
            try:
                data = expenses.split(",")

                if len(data) == 2:
                    key, value = data
                    valid_date = datetime.today()
                elif len(data) == 3:
                    key, value, time = data
                    try:
                        valid_date = datetime.strptime(time.strip(), "%d.%m.%y")
                    except ValueError:
                        msg1 = """Invalid date.
                        Use format dd.mm.yyyy(e.g. 01.01.2025)"""
                        print(msg1)
                        print()
                        continue
                else:
                    msg2 = """input Error:
                        Insert valid format -> Expense_name, cost, [Time]"""
                    print(msg2)
                    print()
                    continue

                expense_id = str(uuid.uuid4())
                self.bills[expense_id] = {
                        "Name": key.strip(),
                        "Cost": float(value.strip()),
                        "Issuing_date": valid_date.strftime("%d.%m.%Y")
                        }

            except ValueError:
                print("Input Error: Insert valid format of expenses -> "
                      "Expense_name, Cost, Time")
                print("")
