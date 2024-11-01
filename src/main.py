from tkinter import *
from src.pages import *

sample_dict = {
    'id': [1,2,3],
    'date': [241101,241102,241103],
    'tag': ['snaks','electricity bill','snacks'],
    'amount': [250,1000,50],
    'description': ['chips', 'bill', 'noodles']
}

is_setup_done = True



#Checks if setup is done
if (is_setup_done == False):
    pass

#If yes, opens the dashboard page
else:
    dashboard_page()