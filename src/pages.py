from tkinter import *
from tkcalendar import DateEntry
import customtkinter
from src.database_dictionary import *
from src.sorting_dict import *
from src.input_edit_functions import *
from time import sleep
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 


sample_dict = {
    'id': [1,2,3],
    'date': [241101,241102,241103],
    'tag': ['snaks','electricity bill','snacks'],
    'amount': [250,1000,50],
    'description': ['chips', 'bill', 'noodles']
}

sample_tag = ["snacks","bills","subcriptions"]




#Creating the dashboard page as a page to be called later in main.py
def dashboard_page():
    #Creating the main window of dashboard page and setting its width and height to full screen
    dash_root = Tk()
    dash_root.config(bg="white")
    dash_root.geometry("{0}x{1}".format(dash_root.winfo_screenwidth(), dash_root.winfo_screenheight()))
    #setting 5 columns and 6 rows in dash root(main window)
    dash_root.columnconfigure(0, weight=1)
    dash_root.columnconfigure(1, weight=1)
    dash_root.columnconfigure(2, weight=1)
    dash_root.columnconfigure(3, weight=1)
    dash_root.columnconfigure(4, weight=1)
    dash_root.rowconfigure(0, weight=1)
    dash_root.rowconfigure(1, weight=1)
    dash_root.rowconfigure(2, weight=1)
    dash_root.rowconfigure(3, weight=1)
    dash_root.rowconfigure(4, weight=1)
    dash_root.rowconfigure(5, weight=1)

    #Creating a label in the dashboard page with text "dashboard" and setting its font and inserting it in row 0 and column 2
    dashboard_label = Label(dash_root, 
                            text = "Dashboard",
                            font=("Arial bold", 26),
                            bg="white"
                            )
    dashboard_label.grid(row=0, column=2)

    #Creating a button to open input page in the dashboard page with text "Enter Data" and inserting it in row 2 and column 1
    input_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="#2B332B",
        bg="white",
        borderwidth=3,
        relief="raised",
        text="Enter Data", 
        command = lambda: [dash_root.destroy(), input_page(sample_dict, sample_tag)]
        )
    input_button.grid(row=2, column=1)

    #Creating a button to open edit page in the dashboard page with text "Edit Data" and inserting it in row 2 and column 3
    edit_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="#2B332B",
        bg="white",
        borderwidth=3,
        relief="raised", 
        text="Edit Data",
        command= lambda: [dash_root.destroy(), edit_page(sample_dict)]
        )
    edit_button.grid(row=2, column=3)

    #Creating a button to open graph page in the dashboard page with text "See data as graphs" and inserting it in row 4 and column 1
    graph_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="#2B332B", 
        bg="white",
        borderwidth=3,
        relief="raised",
        text="See data as graphs",
        command= lambda: [dash_root.destroy()]
        )
    graph_button.grid(row=4, column=1)

    #Creating a button to open tabs page in the dashboard page with text "See data as tabs" and inserting it in row 4 and column 3
    tabs_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="#2B332B",
        bg="white",
        borderwidth=3,
        relief="raised",
        text="See data as tabs",
        command= lambda: [dash_root.destroy(), sorting_page()]
        )
    tabs_button.grid(row=4, column=3)
    
    
    
    
    
    #Starting a loop to run the dash_root (main window)  
    dash_root.mainloop()


def input_page(main_dict, main_tag, index=0, is_edit=False):
    
    input_root = Tk()
    input_root.geometry("{}x{}".format(input_root.winfo_screenwidth(), input_root.winfo_screenheight()))
    input_root.columnconfigure(0, weight=1)
    input_root.rowconfigure(0, weight=1)
    input_root.rowconfigure(1, weight=1)
    input_root.rowconfigure(2, weight=1)
    input_root.rowconfigure(3, weight=1)
    input_root.rowconfigure(4, weight=1)
    input_root.rowconfigure(5, weight=1)


    cal_frame = Frame(input_root)
    cal_frame.grid(column=0, row=0)
    cal_frame.columnconfigure(0, weight=1)
    cal_frame.columnconfigure(1, weight=1)
    cal_frame.rowconfigure(0, weight=1)
    
    tag_frame2 = Frame(input_root)
    tag_frame2.grid(column=0, row=1)

    tag_frame1 = Frame(input_root)
    tag_frame1.grid(column=0, row=2)

    amount_frame =Frame(input_root)
    amount_frame.columnconfigure(0, weight=1)
    amount_frame.columnconfigure(1, weight=1)
    amount_frame.rowconfigure(0, weight=1)
    amount_frame.grid(column=0,row=3)
    
    enter_data_frame = Frame(input_root)
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

    
    tag_updation(main_tag[0])


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
                    
                    if (is_edit == True):
                        main(date, tag, amount, description, '2', main_dict, index)
                    else:
                        main(date, tag, amount, description, '1', main_dict)
                    

                        
                
            description_button = Button(root2, text="Enter", command=enter_button)
            description_button.grid(column=0, row=2)



            root2.mainloop()

    enter_data_button = Button(enter_data_frame, text="Enter the data",command= lambda: [enter_data(),print(tag)])
    enter_data_button.grid(column=2, row=4)


    

    input_root.mainloop()
    dashboard_page()






def sorting_page():
    #Creating the main window, setting its size and assigning each row and coloumn length
    sort_root = Tk()
    sort_root.geometry("{}x{}".format(sort_root.winfo_screenwidth(), sort_root.winfo_screenheight()))
    sort_root.columnconfigure(0, weight=1)
    sort_root.rowconfigure(0, weight=1)
    sort_root.rowconfigure(1, weight=1)
    
    #Creating and configuring a frame separate for selecting key in dictionary to sort by
    selection_frame = Frame(sort_root)
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
    sorting_frame0 = customtkinter.CTkScrollableFrame(sort_root,
                                                     orientation="vertical", 
                                                     width=sort_root.winfo_screenwidth()*0.95,
                                                     height=sort_root.winfo_screenheight()*0.80,
                                                     fg_color="white"
                                                     )
    
    sorting_frame0.grid(column=0, row=1)
    sorting_frame0.columnconfigure(0, weight=1)
    for i in range(0, len(main_dict["id"])+1):
        sorting_frame0.rowconfigure(i, weight=1)
    
    

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
            sort_root = Tk()
            sort_root.geometry("{}x{}".format(sort_root.winfo_screenheight(), sort_root.winfo_screenheight()))
            description_label = Label(sort_root, text=main_dict["description"][index])
            description_label.pack()
            sort_root.mainloop()
            sorting_page()
        
        full_data_button[index] = Button(dict_frame[index], text=">", command=lambda: [sort_root.destroy(),display_description(index)], width=int(dict_frame[index].winfo_screenwidth()*(0.2)))
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
    sort_root.mainloop()
    dashboard_page()     





def edit_page(main_dict):
    edit_root = Tk()
    edit_root.geometry("{}x{}".format(edit_root.winfo_screenwidth(), edit_root.winfo_screenheight()))
    edit_root.columnconfigure(0, weight=1)
    edit_root.rowconfigure(0, weight=1)


    edit_frame = customtkinter.CTkScrollableFrame(edit_root,
                                                     orientation="vertical", 
                                                     width=edit_root.winfo_screenwidth()*0.95,
                                                     height=edit_root.winfo_screenheight()*0.80,
                                                     fg_color="white"
                                                     )
    edit_frame.grid(column=0, row=0)
    edit_frame.columnconfigure(0, weight=1)
    for i in range(0, len(main_dict["id"])+1):
        edit_frame.rowconfigure(i, weight=1)
    
    

    dict_frame = dict()
    full_data_button = dict()
    def dict_item(index):

        dict_frame[index] = Frame(edit_frame, width=edit_frame.winfo_screenwidth())
        dict_frame[index].grid(column=0,row=index+1)
        dict_frame[index].columnconfigure(0, weight=1)
        dict_frame[index].columnconfigure(1, weight=1)
        dict_frame[index].columnconfigure(2, weight=1)
        dict_frame[index].columnconfigure(3, weight=1)
        dict_frame[index].columnconfigure(4, weight=1)
        dict_frame[index].rowconfigure(0, weight=1)

        def edit_command(index = index):
            input_page(sample_dict, sample_tag, index=index, is_edit=True)
            pass
        
        full_data_button[index] = Button(dict_frame[index], text=">", command=lambda: [edit_root.destroy(), edit_command(index)], width=int(dict_frame[index].winfo_screenwidth()*(0.2)))
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



    
    dict_frame0 = Frame(edit_frame)

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
    
    for i in range(0, len(main_dict["id"])):
        dict_item(i)

    # Execute tkinter 
    edit_root.mainloop()


def graph_page():
    graph_root = Tk()
    graph_root.geometry("{}x{}".format(graph_root.winfo_screenwidth(), graph_root.winfo_screenheight()))
    graph_root.columnconfigure(0, weight=1)
    graph_root.rowconfigure(0, weight=1)
    graph_root.rowconfigure(1, weight=1)
    graph_root.rowconfigure(2, weight=1)



    graph_main_label = Label(graph_root, text="Graph Page")
    graph_main_label.grid(column=0, row=0)

    
    graph_frame1 = Frame(graph_root)
    graph_frame1.grid(column=0, row=1)
        
    fig = Figure()
    
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plot1 = fig.add_subplot(111) 
    
    plot1.plot(xpoints, ypoints)
    

    canvas = FigureCanvasTkAgg(fig, master=graph_frame1)
    
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, graph_frame1)
    toolbar.update()

    canvas.get_tk_widget().pack()

    graph_root.mainloop()


#dashboard_page()
#input_page(sample_dict, sample_tag)
#sorting_page()
#edit_page()
#graph_page()

