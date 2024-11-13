from src.database_dictionary import *

class Budget:
    def __init__(self):
        self.entries = {}
        self.next_id = 1

    def add_entry(self, entry, main_dict):
        if self.entries:
            self.next_id = max(self.entries.keys()) + 1

        entry_id = max(main_dict['id'])
        self.entries[entry_id] = entry
        for key in main_dict.keys():
            if (key == 'id'):
                main_dict[key].append(entry_id + 1)
            else:
                main_dict[key].append(self.entries[entry_id][key])
        dict_to_database(main_dict)
    


    def edit_entry(self, entry_id, updated_entry, main_dict):
        index = main_dict['id'].index(entry_id)
    
        for key in main_dict.keys():
            main_dict[key][index] = updated_entry[key]     
    
        dict_to_database(main_dict)


    def get_entries(self):
        print("\n--- Budget Entries ---")
        for entry_id, details in self.entries.items():
            print(f"ID: {entry_id}, Details: {details}")



def main(date, tag, amount, description, choice, main_dict, entry_id):
    budget = Budget()
    
    
    if choice == '1':
        entry = {
            'date': date,
            'tag': tag,
            'amount': amount,
            'description': description
        }
        
        budget.add_entry(entry, main_dict)
    
    elif choice == '2':
        if entry_id in main_dict['id']:
            updated_entry = {}

            updated_entry['id'] = entry_id

            updated_entry['date'] = date
        
            updated_entry['tag'] = tag
            
            
            updated_entry['amount'] = amount
            
        
            updated_entry['description'] = description

            """
            while True:
                additional_key = input("Enter additional key to update (or 'done' to finish): ")
                if additional_key.lower() == 'done':
                    break
                additional_value = input(f"Enter new value for '{additional_key}' (or 'null' for no value): ")
                if additional_value.lower() == 'null':
                    additional_value = None
                updated_entry[additional_key] = additional_value
            """
  
            budget.edit_entry(entry_id, updated_entry, main_dict)

        
        else:
            print(f"No entry found with ID: {entry_id}")
    
    elif choice == '3':
        budget.get_entries()
    
    elif choice == '4':
        print("Exiting the program.")
    
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()