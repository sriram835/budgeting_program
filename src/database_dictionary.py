import pandas as pd

sample_tag_set = {"snacks", "bills", "subscription"}


def setup_tags_file(tags_set):
    total_tag = ""
    tags_file = open("budgeting_program/database/tags.txt", "w")
    for i in tags_set:
        total_tag = f"{total_tag} {i}" 
    tags_file.write(total_tag)
    tags_file.close()

def get_main_tags_set():
    tags_file = open("budgeting_program/database/tags.txt", "r")
    tag_set = set(map(str, tags_file.read().strip().split()))
    return list(tag_set)

def main_dictionary():
    data = pd.read_excel('budgeting_program/database/sample_database.xlsx')
    main_dict = dict()

    keys_list = list(data.columns)
    for key in keys_list:
        main_dict[key] = data[key].tolist()

    return main_dict    

def dict_to_database():
    main_dict = main_dictionary()
    data = pd.DataFrame.from_dict(main_dict)
    data.to_excel("budgeting_program/database/expenses.xlsx", index=False)
    