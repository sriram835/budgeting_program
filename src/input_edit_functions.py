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
        print(f"Entry added with ID: {entry_id}")
        print(f"Details: {self.entries[entry_id]}")
        for key in main_dict.keys():
            if (key == 'id'):
                main_dict[key].append(entry_id + 1)
            else:
                main_dict[key].append(self.entries[entry_id][key])
        dict_to_database(main_dict)
        print("Done")


    def edit_entry(self, entry_id, updated_entry):
        if entry_id in self.entries:
            self.entries[entry_id].update(updated_entry)
            print(f"Entry with ID: {entry_id} has been updated.")
            print(f"Updated Details: {self.entries[entry_id]}")
        else:
            print(f"No entry found with ID: {entry_id}")

    def get_entries(self):
        print("\n--- Budget Entries ---")
        for entry_id, details in self.entries.items():
            print(f"ID: {entry_id}, Details: {details}")

def main(date, tag, amount, description, choice, main_dict, id):
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
        entry_id = int(input("Enter the ID of the entry to edit: "))
        if entry_id in budget.entries:
            updated_entry = {}
            print("Leave a field blank to keep the current value.")
            date = input("Enter new date (YYYY-MM-DD): ")
            if date:
                updated_entry['date'] = date
            
            tag = input("Enter new tag: ")
            if tag:
                updated_entry['tag'] = tag
            
            amount = input("Enter new amount: ")
            if amount:
                updated_entry['amount'] = amount
            
            description = input("Enter new description: ")
            if description:
                updated_entry['description'] = description

            while True:
                additional_key = input("Enter additional key to update (or 'done' to finish): ")
                if additional_key.lower() == 'done':
                    break
                additional_value = input(f"Enter new value for '{additional_key}' (or 'null' for no value): ")
                if additional_value.lower() == 'null':
                    additional_value = None
                updated_entry[additional_key] = additional_value
            
            budget.edit_entry(entry_id, updated_entry)
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