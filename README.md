# 💰 Finanzas.py

**Finanzas.py** is a console-based application built in **Python 3** designed to practice **Object-Oriented Programming (OOP)**, file management with **JSON**, and modular programming.  
The project’s goal is to help track and manage personal expenses through an interactive command-line menu.

---

## 📁 Project Structure

├── dp_actions
│   ├── clean_terminal.py
│   ├── create_dictionary.py
│   ├── create_directory.py
│   ├── delete_dictionary.py
│   ├── __init__.py
│   ├── modify_dictionary.py
│   ├── save_to_json.py
│   └── show_json.py
├── fin_actions
│   ├── expenses_dir
│   │   ├── add_expenses.py
│   │   ├── Bills_register
│   │   │   └── bills_Date:13-10-25,hour:19:02.json
│   │   ├── delete_expenses.py
│   │   ├── __init__.py
│   │   ├── modify_expenses.py
│   │   └── show_expenses.py
│   └── __init__.py
├── __init__.py
├── main.py
└── tasks.txt

## Main Features

###  'Main'
Acts as the entry point of the program, showing a simple text-based menu.
It allows users to:
- Add new expenses

### 'Addexpenses`
Handles the creation and registration of new expenses.  
Each expense includes:
- **Name** of the expense  
- **Amount** spent  
- **Date** (automatically set to today if not provided)  

Each record is saved as a **JSON file**, identified by a unique `UUID`.


### `Cleanterminal`
Clears the terminal screen automatically depending on the operating system
(Windows, Linux, or macOS).

---

Requirements:

-  Python 3.10+ i
-  python3 main.py

EXAMPLE USAGE:
Menu of actions
Option 1: Add expenses

Insert which action you want to do: 1

Insert your expenses in (format:name,value,date)
or just ENTER to finish:
Food, 20, 15.10.2025
Transport, 10

-> Check if the Directory with the files is correctly saved in a json file
