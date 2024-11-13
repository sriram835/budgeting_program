import numpy as np
import matplotlib.pyplot as plt

d = {'id':[1,2,3], 'date':[241101, 241102, 241003,241005], 'tag':['snacks','electricity bill','snacks','books'],'amount': [500,1000,50,100], 'description':['chips','bill','noodles','books']}


def pie_individual_tag(main_dict, year_input, month_input):
    tags_list= list()
    amount_list = list()
    for i in main_dict['date']:
        if str(i)[0:2] == year_input :
            if str(i)[2:4] == month_input:
                l1 = main_dict['tag']
                l2 = main_dict['amount']
                if l1[main_dict['date'].index(i)] not in tags_list:
                    tags_list.append(l1[main_dict['date'].index(i)])
                    amount_list.append( l2[main_dict['date'].index(i)])
                else:
                    amount_list[tags_list.index(l1[main_dict['date'].index(i)])] +=  l2[main_dict['date'].index(i)]
    amount = np.array(amount_list)
    tags = np.array(tags_list)
    # plt.figure(figsize=(8,5))
    
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
