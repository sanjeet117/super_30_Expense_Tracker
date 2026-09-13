import logging
from expense_tracker.exceptions import InvalidExpenseError
from expense_tracker.models import Expense 

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self,amount,category,description,date):
        if amount <= 0:
            logging.error('Invalid expense amount: %s',amount)
            raise InvalidExpenseError('Amount must be greater than 0')
        expense = Expense(amount,category,description,date)
        self.expenses.append(expense)
        logging.info('Expense added successfully: %s',amount)

    def get_expenses(self):
        return self.expenses 

    def get_total_expense(self):
        total = 0
        for expense in self.expenses:
            total = total + expense.amount
        return total 
    

    