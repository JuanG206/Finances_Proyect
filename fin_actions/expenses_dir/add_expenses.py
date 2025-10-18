#!/usr/bin/env python3
import uuid
from datetime import datetime
from dp_actions.rofi_menu import Rofimenu
from dp_actions.create_dictionary import CreateDictionary
from dp_actions.save_to_json import Save
import os
import json

class Addexpenses:
    def __init__(self, directory="fin_actions/expenses_dir/Bills_register"):
        self.directory = directory
        self.bills = CreateDictionary().create_dictionary()
        self.rofi = Rofimenu()

    def adding_bills(self):
        """
        Agrega gastos usando Rofi como interfaz.
        """
        while True:
            options = ["Add new expense", "Show current", "Save & Exit"]
            action = self.rofi.rofi_menu(options, prompt="Expenses Menu")

            if not action or action == "Save & Exit":
                if self.bills:
                    try:
                        save = Save(self.directory)
                        save.savetojson(self.bills, "bills")
                        self.rofi.rofi_menu(["Expenses saved successfully!"], prompt="Done")
                    except Exception as e:
                        self.rofi.rofi_menu([f"Error saving JSON: {str(e)}"], prompt="Error")
                else:
                    self.rofi.rofi_menu(["No expenses added"], prompt="Info")
                break

            elif action == "Add new expense":
                try:
                    name = self.rofi.rofi_menu([], prompt="Expense name")
                    if not name:
                        continue

                    cost = self.rofi.rofi_menu([], prompt="Expense cost")
                    if not cost:
                        continue

                    date = self.rofi.rofi_menu([], prompt="Date (dd.mm.yyyy) or ENTER for today")
                    if not date:
                        valid_date = datetime.today()
                    else:
                        try:
                            valid_date = datetime.strptime(date.strip(), "%d.%m.%Y")
                        except ValueError:
                            self.rofi.rofi_menu(["Invalid date format (use dd.mm.yyyy)"], prompt="Error")
                            continue

                    expense_id = str(uuid.uuid4())
                    self.bills[expense_id] = {
                        "Name": name.strip(),
                        "Cost": float(cost.strip()),
                        "Issuing_date": valid_date.strftime("%d.%m.%Y")
                    }

                    self.rofi.rofi_menu(
                        [f"Added: {name} - ${cost} ({valid_date.strftime('%d.%m.%Y')})"],
                        prompt="Success"
                    )

                except ValueError as ve:
                    self.rofi.rofi_menu([f"Input Error: {str(ve)}"], prompt="Error")

            elif action == "Show current":
                if not self.bills:
                    self.rofi.rofi_menu(["No expenses recorded yet."], prompt="Info")
                else:
                    lines = [f"{v['Name']} - ${v['Cost']} ({v['Issuing_date']})"
                             for v in self.bills.values()]
                    self.rofi.rofi_menu(lines, prompt="Current Expenses")

    def show_json_files(self):
        """
        Lista los archivos JSON del directorio y permite verlos en Rofi.
        """
        try:
            files = [f for f in os.listdir(self.directory) if f.endswith(".json")]
            if not files:
                self.rofi.rofi_menu(["No JSON files found"], prompt="Info")
                return

            selected_file = self.rofi.rofi_menu(files, prompt="Select File")
            if not selected_file:
                return

            path = os.path.join(self.directory, selected_file)
            with open(path, "r") as f:
                data = json.load(f)

            # Mostrar contenido en Rofi
            lines = []
            for k, v in data.items():
                lines.append(f"{v['Name']} - ${v['Cost']} ({v['Issuing_date']})")
            self.rofi.rofi_menu(lines, prompt=f"Content of: {selected_file}  (Click 'esq' or 'Enter' to exit)")

        except Exception as e:
            self.rofi.rofi_menu([f"Error reading JSON: {str(e)}"], prompt="Error")

