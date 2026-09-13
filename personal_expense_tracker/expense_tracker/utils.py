import logging 

def setup_logging():
    logging.basicConfig(
        filename = 'expense_tracker.log',
        level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )