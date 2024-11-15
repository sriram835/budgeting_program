#Importing pandas
import pandas as pd

#Creating a function that can add tags or reset tags in tags.txt
def setup_tags_file(tags_set, is_reset = False):
    total_tag = ""
    
    if (is_reset == True):
        tags_file = open("budgeting_program/database/tags.txt", "w")
    else:
        tags_file = open("budgeting_program/database/tags.txt", "a")
    
    
    for i in tags_set:
        total_tag = f"{total_tag} {i}" 
    

    tags_file.write(total_tag)
    tags_file.close()

#Creating a fuction that gets all the tags from tags.txt in database 
def get_main_tags_set():
    tags_file = open("budgeting_program/database/tags.txt", "r")
    tag_set = set(map(str, tags_file.read().strip().split()))
    return list(tag_set)

#Function to get main data from database/expenses.xlsx
def main_dictionary():
    data = pd.read_excel('budgeting_program/database/expenses.xlsx')
    main_dict = dict()

    keys_list = list(data.columns)
    for key in keys_list:
        main_dict[key] = data[key].tolist()

    return main_dict    

#Function to upload main dictionary to expenses.xlsx in database folder
def dict_to_database(main_dict):
    data = pd.DataFrame.from_dict(main_dict)
    data.to_excel("budgeting_program/database/expenses.xlsx", index=False)
    

