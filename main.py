#!/usr/bin/env python3
"""
Main script for finance manager.
Uses Rofi for menus and integrates Addexpenses and Cleanterminal classes.
"""

# Importa tus clases desde sus archivos correspondientes
from fin_actions.expenses_dir.add_expenses import Addexpenses
from dp_actions.clean_terminal import Cleanterminal
from dp_actions.rofi_menu import Rofimenu


class Main:
    """
    Main class that manages the application menu and actions.
    """

    def __init__(self):
        # Crear instancias de las clases necesarias
        self.add_expenses = Addexpenses()
        self.rofi = Rofimenu()

    def selection(self):
        """
        Show main menu using Rofi and handle user actions.
        """
        while True:
            # Opciones del menú principal
            options = [
                "Add expenses",
                "Show expenses",
                "Exit"
            ]

            # Llamar a Rofi para seleccionar opción
            select = self.rofi.rofi_menu(options, prompt="Main Menu")

            if not select or select == "Exit":
                break
            elif select == "Add expenses":
                self.add_expenses.adding_bills()
            elif select == "Show expenses":
                self.add_expenses.show_json_files()


if __name__ == "__main__":
    app = Main()
    app.selection()

