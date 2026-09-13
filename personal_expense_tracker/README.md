# Personal Expense Tracker

A simple command-line Python application for managing personal expenses.

## Features

* Add a new expense
* View all recorded expenses
* Calculate total expenses
* Validate expense amounts
* Handle invalid numeric input
* Handle negative expense amounts using a custom exception
* Log successful and failed expense operations to a log file
* Use a modular Python package structure

## Project Structure

```text
personal_expense_tracker/
│
├── main.py
├── README.md
│
└── expense_tracker/
    ├── __init__.py
    ├── models.py
    ├── manager.py
    ├── exceptions.py
    └── utils.py
```

## Modules

### `main.py`

Contains the command-line interface and menu system. It accepts user input and connects the different modules.

### `models.py`

Contains the `Expense` class, which represents an individual expense.

### `manager.py`

Contains the `ExpenseManager` class. It stores expenses, adds expenses, returns expenses, and calculates the total expense.

### `exceptions.py`

Contains the custom `InvalidExpenseError` exception used to handle invalid expense amounts.

### `utils.py`

Contains the logging configuration used by the application.

## Error Handling

The application uses `try`, `except`, and `finally` for error handling.

It handles:

* Invalid numeric input such as `abc`
* Negative expense amounts such as `-500`
* Invalid menu choices

A custom exception called `InvalidExpenseError` is used when the expense amount is less than or equal to zero.

## Logging

The application uses Python's built-in `logging` module.

Logs are stored in:

```text
expense_tracker.log
```

Successful expense additions are recorded as `INFO` logs, while invalid expense amounts are recorded as `ERROR` logs.

## How to Run

Open a terminal in the project directory and run:

```bash
python main.py
```

The application displays a menu:

```text
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit
```

## AI-Assisted Development

This project was developed using an AI coding assistant through an iterative, step-by-step approach. The AI was used to understand requirements, design the project structure, develop individual modules, debug errors, add exception handling, add logging, and test the application.

### Prompts Used During Development

1. **Requirement Understanding**

   "Help me understand the requirements of the Personal Expense Tracker assignment and explain what features and technical requirements I need to implement."

2. **Project Structure**

   "Suggest a modular Python package structure for a Personal Expense Tracker with at least four Python files and explain the purpose of each file."

3. **Expense Model**

   "Help me create an Expense class for the Personal Expense Tracker and explain the purpose of the class attributes and constructor."

4. **Expense Manager**

   "Help me create an ExpenseManager class that can add expenses, return expenses, and calculate the total expense."

5. **Custom Exception**

   "Help me add a custom exception for invalid expense amounts and explain when the exception should be raised."

6. **Exception Handling**

   "Help me add try, except, and finally blocks to handle errors in the Personal Expense Tracker."

7. **Logging**

   "Help me add Python logging to the Personal Expense Tracker and store INFO and ERROR messages in a log file."

8. **CLI**

   "Help me build a command-line menu for the Personal Expense Tracker with options to add, view, total, and exit."

9. **Input Validation**

   "Help me handle invalid amount input such as abc and negative amounts without crashing the application."

10. **Testing and Debugging**

"Help me test the application step-by-step and identify and fix errors based on the terminal output."

## Example

```text
======= Personal Expense Tracker =======
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit

Enter your choice: 1
Enter the amount: 500
Enter the category: food
Enter the description: dinner
Enter the date: 13-09-2026

Expense added successfully.
Expense operation completed.
```

## Technologies Used

* Python
* Python Classes and Objects
* Python Packages and Modules
* Exception Handling
* Custom Exceptions
* Python Logging
* Command-Line Interface
