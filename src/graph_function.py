import numpy as np
import matplotlib.pyplot as plt

from database_dictionary import main_dictionary 

sample_dict = {'id':[1,2,3,4], 'date':[241101, 241102, 241003,241105], 'tag':['snacks','electricity bill','snacks','books'],'amount': [500,1000,50,100], 'description':['chips','bill','noodles','books']}

# Creating a pie chart for the expences in each month.
def pie_individual_tag(main_dict, year_input, month_input):
    tags_list= list()
    amount_list = list()
    tag_set = set(main_dict['tag'])
    for tag in tag_set:
        current_sum = 0
        for i in main_dict['id']:
            index = main_dict['id'].index(i)
            date = str(main_dict['date'][index])
            #Verifiying the month, year and respective tag.
            if (date[0:2] == year_input and date[2:4] == month_input and main_dict['tag'][index] == tag):    
                current_sum += main_dict['amount'][index]
        #Storing the unique value of tags and respective amounts in list.
        tags_list.append(tag)
        amount_list.append(current_sum)
    amount = np.array(amount_list)
    tags = np.array(tags_list)
    data = [amount, tags]
    return data



# Creating a bar graph for the expences in a year by month.
def bar_total(main_dict, year):
    expences = main_dict['amount']
    month_expence = dict()
    for id in main_dict['id']:
        index = main_dict['id'].index(id)
        i = main_dict['date'][index]
        if year in str(i)[0:2]:
            if str(i)[2:4] in month_expence.keys():
                month_expence[str(i)[2:4]] += expences[index]
            else:
                month_expence[str(i)[2:4]] = expences[index]
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