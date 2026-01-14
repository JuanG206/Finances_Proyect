# My Finanzes - Personal Expense Manager

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A simple and efficient console application to manage your personal expenses using plain text files. 

**An open-source practice project to demonstrate Python coding skills**

</div>

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Examples](#examples)
- [Contributing](#contributing)

---

## Features

- Add expenses with name, amount, category, and date
- List all registered expenses
- Modify existing expenses
- Delete expenses by ID
- Persistence in TXT files (no database required)
- Automatically generated unique IDs
- Intuitive and easy-to-use console interface
- Clean and maintainable MVC architecture

---

## Project Structure

```
my_finanzes_proyect/
├── controllers/              # Business logic
│   └── expense_controller.py # Expense controller
├── models/                   # Data models
│   └── expense.py           # Expense model
├── storage/                  # Persistence layer
│   └── file_manager.py      # TXT file manager
├── utils/                    # Utilities
│   └── helpers.py           # Helper functions (UUID)
├── data/                     # Data storage
│   └── expenses/            # Expense TXT files
└── main.py                  # Entry point
```

---

## Requirements

- **Python**: 3.7 or higher
- **Standard modules**: `datetime`, `uuid`, `os`

> **Note**: This project does not require external dependencies.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JuanG206/Finances_Proyect.git
cd Finances_Proyect/my_finanzes_proyect
```

### 2. Verify Python version

```bash
python3 --version
# Must be Python 3.7 or higher
```

### 3. Run the application

```bash
python3 main.py
```

---

## Usage

### Main Menu

When running `python3 main.py`, you will see the following menu:

```
===== MY EXPENSES =====
1. Add Expense
2. List Expenses
3. Modify Expense
4. Delete Expense
5. Exit

Choose an option: 
```

### 1. Add an Expense

```bash
Choose an option: 1
Expense name: Grocery shopping
Amount: 45.50
Category: Food
Date (YYYY-MM-DD): 2026-01-14

Expense 'Grocery shopping' added successfully!
```

> **Note**: If you don't enter a date, the current date will be used automatically.

---

### 2. List Expenses

```bash
Choose an option: 2

--- Expenses ---
ID: 123e4567-e89b-12d3-a456-426614174000
Name: Grocery shopping
Amount: 45.5
Category: Food
Date: 2026-01-14

ID: 987f6543-a21c-34e5-b678-526725185111
Name: Gasoline
Amount: 30.0
Category: Transportation
Date: 2026-01-13
```

---

### 3. Modify an Expense

```bash
Choose an option: 3
Enter Expense ID to modify: 123e4567-e89b-12d3-a456-426614174000

Enter new values (leave empty to keep current):
Name: Market shopping
Amount: 50.00
Category: 
Date (YYYY-MM-DD): 

Expense modified successfully!
```

> **Note**: Empty fields will keep their original values.

---

### 4. Delete an Expense

```bash
Choose an option: 4

--- Expenses ---
[List of expenses...]

Enter Expense ID to delete: 987f6543-a21c-34e5-b678-526725185111

Expense deleted successfully!
```

---

## Architecture

### MVC Pattern (Model-View-Controller)

```
┌─────────────┐
│   main.py   │  ← View (User interface)
│   (View)    │
└──────┬──────┘
       │
       ↓
┌──────────────────────┐
│ expense_controller.py│  ← Controller (Business logic)
│    (Controller)       │
└──────┬───────────────┘
       │
       ├──→ ┌─────────────┐
       │    │ expense.py  │  ← Model (Data structure)
       │    │  (Model)    │
       │    └─────────────┘
       │
       └──→ ┌──────────────────┐
            │ file_manager.py  │  ← Persistence (Storage)
            │    (Storage)      │
            └──────────────────┘
```

### Key Components

#### **Expense** (Model)
Defines the structure of an expense with the following attributes:
- `id`: Unique identifier (UUID)
- `name`: Expense name
- `amount`: Amount
- `category`: Category
- `date`: Date

#### **ExpenseController** (Controller)
Manages operations:
- `add_expense()`: Create new expense
- `list_expenses()`: List all expenses
- `modify_expense()`: Update expense
- `delete_expense()`: Delete expense

#### **FileManager** (Persistence)
Handles storage in TXT files:
- `save()`: Save data
- `load()`: Load a file
- `load_all()`: Load all files
- `delete()`: Delete file

---

## Examples

### TXT File Format

Each expense is stored as a `{ID}.txt` file in `data/expenses/`:

```txt
id=123e4567-e89b-12d3-a456-426614174000
name=Grocery shopping
amount=45.5
category=Food
date=2026-01-14
```

### Programmatic Usage

If you want to use the components in your own code:

```python
from controllers.expense_controller import ExpenseController

# Create controller
controller = ExpenseController()

# Add expense
expense = controller.add_expense(
    name="Coffee",
    amount=3.50,
    category="Food",
    date="2026-01-14"
)

# List expenses
expenses = controller.list_expenses()
for exp in expenses:
    print(f"{exp['name']}: ${exp['amount']}")

# Modify expense
controller.modify_expense(
    expense.id,
    amount=4.00
)

# Delete expense
controller.delete_expense(expense.id)
```

---

## Technical Features

### Unique ID Generation

```python
import uuid

def generate_id():
    """Generate a unique ID using UUID4"""
    return str(uuid.uuid4())
```

### Date Handling

```python
from datetime import datetime

# If no date is provided, use current date
date_obj = datetime.fromisoformat(date) if date else datetime.today()
```

### TXT Persistence

Data is saved in `key=value` format:

```python
def save(self, obj_id: str, data: dict):
    with open(f"{obj_id}.txt", "w") as f:
        for key, value in data.items():
            f.write(f"{key}={value}\n")
```

---

## Development

### Adding New Features

1. **Search by category**:
   ```python
   def search_by_category(self, category: str):
       expenses = self.list_expenses()
       return [e for e in expenses if e['category'] == category]
   ```

2. **Monthly report**:
   ```python
   def monthly_report(self, month: int, year: int):
       expenses = self.list_expenses()
       total = sum(float(e['amount']) for e in expenses 
                   if e['date'].startswith(f"{year}-{month:02d}"))
       return total
   ```

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork** the project
2. Create a **branch** for your feature (`git checkout -b feature/new-feature`)
3. **Commit** your changes (`git commit -m 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. Open a **Pull Request**

---

## Important Notes

### Current Limitations

- No robust input data validation
- TXT format is not ideal for large data volumes
- No automatic backup functionality
- No reports or advanced analytics

### Future Improvements

- [ ] Input data validation
- [ ] Advanced search and filtering
- [ ] Monthly/annual reports
- [ ] CSV/JSON export
- [ ] Graphical User Interface (GUI)
- [ ] Migration to SQLite
- [ ] Expense charts and graphs

---

## About This Project

This is an open-source practice project created to demonstrate Python programming skills, focusing on:
- Clean code architecture (MVC pattern)
- File-based data persistence
- Object-oriented programming
- Console application development
- Project structure and organization

Feel free to use this project as a reference or learning material!

---

## Author

**Juan G206**
- GitHub: [@JuanG206](https://github.com/JuanG206)
- Repository: [Finances_Proyect](https://github.com/JuanG206/Finances_Proyect)

---

<div align="center">

**Made with Python**

[Back to top](#my-finanzes---personal-expense-manager)

</div>