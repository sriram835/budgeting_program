import numpy as np
import matplotlib.pyplot as plt

from src.database_dictionary import main_dictionary 

d = {'id':[1,2,3,4], 'date':[241101, 241102, 241003,241105], 'tag':['snacks','electricity bill','snacks','books'],'amount': [500,1000,50,100], 'description':['chips','bill','noodles','books']}
main_dict1 = main_dictionary().copy()
print(main_dict1)

def pie_individual_tag(main_dict, year_input, month_input):
    tags_list= list()
    amount_list = list()
    tag_set = set(main_dict['tag'])
    for tag in tag_set:
        current_sum = 0
        for i in main_dict['id']:
            index = main_dict['id'].index(i)
            date = str(main_dict['date'][index])
            if (date[0:2] == year_input and date[2:4] == month_input and main_dict['tag'][index] == tag):    
                current_sum += main_dict['amount'][index]
        tags_list.append(tag)
        amount_list.append(current_sum)
                    
            
    print(amount_list, tags_list)
    amount = np.array(amount_list)
    tags = np.array(tags_list)


    data = [amount, tags]
    return data




def bar_total(main_dict, year):
    expences = main_dict['amount']
    month_expence = dict()
    for i in main_dict['date']:
        if year in str(i)[0:2]:
            if str(i)[2:4] in month_expence.keys():
                month_expence[str(i)[2:4]] += expences[main_dict['date'].index(i)]
            else:
                month_expence[str(i)[2:4]] = expences[main_dict['date'].index(i)]
    l3 = list(month_expence.keys())
    l3.sort()
    l4  = list()
    for i in l3:
        l4.append(month_expence[i])
    plt.figure(figsize=(12,5))
    plt.xlabel('$Month$ $number$')
    plt.ylabel('$Total$ $expence$')
    data = [l3,l4]
    return data
