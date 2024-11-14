# Importing everything from the 'database_dictionary' module located in the 'src' directory
from src.database_dictionary import *

class Budget:
    # Initializing the Budget class with an empty entries dictionary and next_id counter
    def __init__(self):
        self.entries = {}
        self.next_id = 1

    def add_entry(self, entry, main_dict):
        ''' ADDING a new entry to the budget and updating the main dictionary

        entry - It is a dictionary that stores the details of the entry entered
        main_dict - It is the main dictionary where all the entries along with their details are stored
        '''
        if self.entries:
            self.next_id = max(self.entries.keys()) + 1 # next_id = 1 + maximum key ID in the 'entries' dictionary

        entry_id = max(main_dict['id'])
        self.entries[entry_id] = entry

        for key in main_dict.keys():

            if (key == 'id'):
                main_dict[key].append(entry_id + 1)

            else:
                main_dict[key].append(self.entries[entry_id][key])

        dict_to_database(main_dict)   #saving the updated 'main_dict' to the database
    


    def edit_entry(self, entry_id, updated_entry, main_dict):

        ''' EDITING an existing entry and updating the main dictionary

        entry_id - ID of the entry to be edited
        updated_entry - It is a dictionary that contains the updated details
        main_dict - main dictionary

        '''
            
        if entry_id in self.entries:
            index = main_dict['id'].index(entry_id)
            for key in main_dict.keys():
                main_dict[key][index] = updated_entry[key]     
            dict_to_database(main_dict)

            print(f"Entry with ID: {entry_id} has been edited.")

        else:
            print(f"No entry found with ID: {entry_id}")

    def delete_entry(self, entry_id, main_dict):

        '''
        DELETING an existing entry from the main dictionary
        entry_id - ID of the entry to be edited
        main_dict - main dictionary

        '''
        if entry_id in main_dict:
            index = main_dict['id'].index(entry_id)
            for key in main_dict.keys():
                main_dict[key].pop(index)
            dict_to_database(main_dict)

            print(f"Entry with ID: {entry_id} has been deleted.")
        
        else:
            print(f"No entry found with ID: {entry_id}")

    def get_entries(self): 
        '''
        GET or DISPLAY all the entries available in the main dictionary
        '''
        print("\n--- Budget Entries ---")
        for entry_id, details in self.entries.items():
            print(f"ID: {entry_id}, Details: {details}")


# defining a function named main
def main(date, tag, amount, description, choice, main_dict, entry_id):
    budget = Budget()
    
    
    if choice == '1': # add entry choice
        entry = {
            'date': date,
            'tag': tag,
            'amount': amount,
            'description': description
        }
        
        budget.add_entry(entry, main_dict)
    
    elif choice == '2': # edit entry choice
        if entry_id in main_dict['id']:
            updated_entry = {}

            updated_entry['id'] = entry_id

            updated_entry['date'] = date
        
            updated_entry['tag'] = tag
            
            updated_entry['amount'] = amount
            
            updated_entry['description'] = description
  
            budget.edit_entry(entry_id, updated_entry, main_dict)

        else:
            print(f"No entry found with ID: {entry_id}")
    
    elif choice == '3': # get entries choice
        budget.get_entries()

    elif choice == '4': # delete entry choice
        if entry_id in main_dict['id']:
            budget.delete_entry(entry_id, main_dict)

        else:
            print(f"No entry found with ID: {entry_id}.")
    
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()