
import logging
from expense_tracker.exceptions import InvalidExpenseError
from expense_tracker.manager import ExpenseManager
from expense_tracker.utils import setup_logging

setup_logging()

manager = ExpenseManager()

while True:
    print('======= Personal Expense Tracker =======')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Total Expenses')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        try:
            amount = float(input('Enter the amount: '))
            category = input('Enter the category: ')
            description = input('Enter the description: ')
            date = input('Enter the date: ')

            manager.add_expense(amount, category, description, date)

            print('Expense added successfully.')

        except ValueError:
            print('Please enter a valid number for amount.')

        except InvalidExpenseError as error:
            print('Error:', error)

        finally:
            print('Expense operation completed.')

    elif choice == '2':
        expenses = manager.get_expenses()

        if not expenses:
            print('No expenses found.')
        else:
            for expense in expenses:
                print(f'Amount: {expense.amount}')
                print(f'Category: {expense.category}')
                print(f'Description: {expense.description}')
                print(f'Date: {expense.date}')
                print('--------------------')

    elif choice == '3':
        print('Total Expenses:', manager.get_total_expense())

    elif choice == '4':
        print('Good Bye')
        break

    else:
        print('Invalid choice. Please select 1 to 4.')

