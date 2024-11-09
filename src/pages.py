from tkinter import *
from tkcalendar import DateEntry
import customtkinter
from src.database_dictionary import *
from src.sorting_dict import *
import time

sample_dict = {
    'id': [1,2,3],
    'date': [241101,241102,241103],
    'tag': ['snaks','electricity bill','snacks'],
    'amount': [250,1000,50],
    'description': ['chips', 'bill', 'noodles']
}

sample_tag = ["snacks","bills","subcriptions"]

def dashboard_page():
    root = Tk()
    root.geometry("{0}x{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    dashboard_label = Label(root, text = "Dashboard")
    
    input_button = Button(root, 
        pady=50, 
        padx=50, 
        text="Enter Data", 
        command=lambda: [root.destroy(), input_page(sample_dict, sample_tag)]
        )
    
    edit_button = Button(root, 
        pady=50, 
        padx=50, 
        text="Edit Data"
        )
    
    graph_button = Button(root, 
        pady=50, 
        padx=50, 
        text="See data as graphs"
        )
    
    tabs_button = Button(root, 
        pady=50, 
        padx=50, 
        text="See data as tabs",
        command= lambda: [root.destroy(), sorting_page()]
        )

    dashboard_label.grid(row=0, column=2)
    input_button.grid(row=1, column=1)
    edit_button.grid(row=1, column=3)
    graph_button.grid(row=2, column=1)
    tabs_button.grid(row=2, column=3)

    root.mainloop()


def input_page(main_dict, main_tag):
    root = Tk()
    root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)


    cal_frame = Frame(root)
    cal_frame.grid(column=0, row=0)
    cal_frame.columnconfigure(0, weight=1)
    cal_frame.columnconfigure(1, weight=1)
    cal_frame.rowconfigure(0, weight=1)
    
    tag_frame2 = Frame(root)
    tag_frame2.grid(column=0, row=1)

    tag_frame1 = Frame(root)
    tag_frame1.grid(column=0, row=2)

    amount_frame =Frame(root)
    amount_frame.columnconfigure(0, weight=1)
    amount_frame.columnconfigure(1, weight=1)
    amount_frame.rowconfigure(0, weight=1)
    amount_frame.grid(column=0,row=3)
    
    enter_data_frame = Frame(root)
    enter_data_frame.grid(column=0, row=4)

    tag_button = dict()
    

    # Create a Date Entry widget
    cal = DateEntry(cal_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
    cal.grid(row=0,column=1)

    cal_label = Label(cal_frame, text="Enter date")
    cal_label.grid(column=0, row=0)

    uncut_date = str(cal.get_date())
    uncut_date = uncut_date.split("-")
    year = int(uncut_date[0][2:4])
    month = int(uncut_date[1])
    day = int(uncut_date[2])

    date = year*10000 + month*100 + day

    def tag_updation(new_tag):
        global tag
        tag = new_tag
        tag_selection.configure(state=NORMAL)
        tag_selection.delete(0, END)
        tag_selection.insert(0,new_tag)
        tag_selection.configure(state=DISABLED, disabledbackground="white",disabledforeground="black", cursor="arrow")
    
    

    tag_label = Label(tag_frame2, text="Select the tag")
    tag_label.grid(column=0, row=0)

    tag_label_selected = Label(tag_frame1, text="Selected tag:")
    tag_label_selected.grid(column=0, row=0)

    tag_selection = Entry(tag_frame1, state=DISABLED)
    tag_selection.grid(column=1, row=0)

    
    tag = main_tag[0]
    
    tag_updation(tag)


    for i in range(len(main_tag)):
        def action(x = main_tag[i]):
            return tag_updation(x)
        
        tag_button[main_tag[i]] = Button(tag_frame2, text=main_tag[i], command=action)
        tag_button[main_tag[i]].grid(column=i,row=1)



    amount_label = Label(amount_frame, text="Enter amount: ")
    amount_label.grid(column=0,row=0)
    amount_entry = Entry(amount_frame) 
    amount_entry.grid(column=1, row=0)
    

    def enter_data():

        if (amount_entry.get() == "" or not amount_entry.get().isnumeric()):
            root2 = Tk()
            root2.geometry("{}x{}".format(int(root2.winfo_screenheight()*0.5), int(root2.winfo_screenheight()*0.5)))
            
            message_label = Label(root2, text="Enter proper data")
            message_label.pack()
            
            root2.mainloop()


        else:
            global amount
            amount = amount_entry.get()

            root2 = Tk()
            root2.geometry("{}x{}".format(int(root2.winfo_screenheight()), int(root2.winfo_screenheight()*0.5)))
            root2.columnconfigure(0, weight=1)
            root2.rowconfigure(0, weight=1)
            root2.rowconfigure(1, weight=1)
            root2.rowconfigure(2, weight=1)

            description_label = Label(root2, text="Enter Description")
            description_label.grid(column=0, row=0)

            description_entry = Entry(root2, 
                                    width=int(root2.winfo_screenheight()*0.1)
                                    )
            description_entry.grid(column=0, row=1)

            def enter_button():
                    global description
                    if (description_entry.get() == ""):
                        description = "None"
                    else:
                        description = description_entry.get()
                    
                    print(date, tag, amount)
                        
                
            description_button = Button(root2, text="Enter", command=enter_button)
            description_button.grid(column=0, row=2)



            root2.mainloop()

    enter_data_button = Button(enter_data_frame, text="Enter the data",command=enter_data)
    enter_data_button.grid(column=2, row=4)


    

    root.mainloop()
    dashboard_page()






def sorting_page():
    #Creating the main window, setting its size and assigning each row and coloumn length
    root = Tk()
    root.geometry("{}x{}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    
    #Creating and configuring a frame separate for selecting key in dictionary to sort by
    selection_frame = Frame(root)
    selection_frame.grid(column=0, row=0)
    selection_frame.columnconfigure(0, weight=1)
    selection_frame.columnconfigure(1, weight=1)
    selection_frame.columnconfigure(2, weight=1)
    selection_frame.rowconfigure(0, weight=1)


    
    key_selected = "id"
    order_selected = "Ascending"
    # Change the selected sorting 
    def change_selected_sort(key_selected, order_selected): 
        key_selected = key_clicked.get()
        order_selected = order_clicked.get()
        if (order_selected == "Ascending"):
            Sort(main_dict).Ascend_Sorting(key_selected)
            for i in range(0,len(main_dict["id"])):
                dict_item(i)
        else:
            Sort(main_dict).Descend_Sorting(key_selected)
            for i in range(0,len(main_dict["id"])):
                dict_item(i)

    
    # Dropdown menu options 
    main_dict = main_dictionary()
    key_options = list(main_dict.keys())
    order_options = ["Ascending","Descending"]

    # datatype of menu text 
    key_clicked = StringVar() 
    order_clicked = StringVar()
    
    # initial menu text 
    key_clicked.set("id")
    order_clicked.set("Ascending") 
    
    # Create Dropdown menu 
    order_drop = OptionMenu(selection_frame , order_clicked, *order_options) 
    key_drop = OptionMenu(selection_frame , key_clicked, *key_options) 
    
    # Create button, it start the sorting 
    button = Button( selection_frame , text = "Sort" , command = lambda: change_selected_sort(key_selected, order_selected) )
    
    #Assigning grid placement to each element
    key_drop.grid(column=0, row=0)
    order_drop.grid(column=1, row=0)
    button.grid(column=2, row=0)


    #Creating and configuring a frame separate for displaying sorted dictionary
    sorting_frame0 = customtkinter.CTkScrollableFrame(root,
                                                     orientation="vertical", 
                                                     width=root.winfo_screenwidth()*0.95,
                                                     height=root.winfo_screenheight()*0.80,
                                                     fg_color="white"
                                                     )
    
    sorting_frame0.grid(column=0, row=1)
    sorting_frame0.columnconfigure(0, weight=1)
    #for i in range(0, len(main_dict["id"])+1):
        #sorting_frame0.rowconfigure(i, weight=1)
    sorting_frame0.rowconfigure(0, weight=1)
    

    dict_frame = dict()
    full_data_button = dict()
    def dict_item(index):

        dict_frame[index] = Frame(sorting_frame0, width=sorting_frame0.winfo_screenwidth())
        dict_frame[index].grid(column=0,row=index+1)
        dict_frame[index].columnconfigure(0, weight=1)
        dict_frame[index].columnconfigure(1, weight=1)
        dict_frame[index].columnconfigure(2, weight=1)
        dict_frame[index].columnconfigure(3, weight=1)
        dict_frame[index].columnconfigure(4, weight=1)
        dict_frame[index].rowconfigure(0, weight=1)

        def display_description(index = index):
            root = Tk()
            root.geometry("{}x{}".format(root.winfo_screenheight(), root.winfo_screenheight()))
            description_label = Label(root, text=main_dict["description"][index])
            description_label.pack()
            root.mainloop()
        
        full_data_button[index] = Button(dict_frame[index], text=">", command=lambda: display_description(index), width=int(dict_frame[index].winfo_screenwidth()*(0.2)))
        full_data_button[index].grid(column=0, row=0)

        id_label = Label(dict_frame[index], text=main_dict['id'][index], width=int(dict_frame[index].winfo_screenwidth()*(9/40)))
        id_label.grid(column=1, row=0)

        date = str(main_dict['date'][index])
        day = date[4:6]
        month = date[2:4]
        year = date[0:2]
        date_label = Label(dict_frame[index], text=f"{day}/{month}/{year}", width=int(dict_frame[index].winfo_screenwidth()*(9/40)))
        date_label.grid(column=2,row=0)

        tag_label = Label(dict_frame[index], text=main_dict["tag"][index], width=int(dict_frame[index].winfo_screenwidth()*(9/40)))
        tag_label.grid(column=3,row=0)

        amount_label = Label(dict_frame[index], text=main_dict["amount"][index], width=int(dict_frame[index].winfo_screenwidth()*(9/40)))
        amount_label.grid(column=4,row=0)



    
    dict_frame0 = Frame(sorting_frame0)

    dict_frame0.grid(column=0,row=0)
    dict_frame0.columnconfigure(0, weight=1)
    dict_frame0.columnconfigure(1, weight=1)
    dict_frame0.columnconfigure(2, weight=1)
    dict_frame0.columnconfigure(3, weight=1)
    dict_frame0.columnconfigure(4, weight=1)
    dict_frame0.rowconfigure(0, weight=1)
    full_data_button0 = Button(dict_frame0, text=">", width=int(dict_frame0.winfo_screenwidth()*0.2))
    full_data_button0.grid(column=0, row=0)

    id_label0 = Label(dict_frame0, text="id",width=int(dict_frame0.winfo_screenwidth()*(9/40)))
    id_label0.grid(column=1, row=0)

    date_label0 = Label(dict_frame0, text="date",width=int(dict_frame0.winfo_screenwidth()*(9/40)))
    date_label0.grid(column=2,row=0)

    tag_label0 = Label(dict_frame0, text="tags",width=int(dict_frame0.winfo_screenwidth()*(9/40)))
    tag_label0.grid(column=3,row=0)

    amount_label0 = Label(dict_frame0, text="amount",width=int(dict_frame0.winfo_screenwidth()*(9/40)))
    amount_label0.grid(column=4,row=0)
    
    if (order_selected == "Ascending"):
        Sort(main_dict).Ascend_Sorting(key_selected)
        for i in range(0,len(main_dict["id"])):
            dict_item(i)
    else:
        Sort(main_dict).Descend_Sorting(key_selected)
        for i in range(0,len(main_dict["id"])):
            dict_item(i)


    # Execute tkinter 
    root.mainloop()
    dashboard_page()     


#dashboard_page()
#input_page(sample_dict, sample_tag)
#sorting_page()


