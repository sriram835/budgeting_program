from tkinter import *
from tkcalendar import DateEntry
import customtkinter
from time import sleep
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 

#Importing other pages in src folder
from database_dictionary import *
from sorting_dict import *
from input_edit_functions import main
from graph_function import *

# Sample data for demonstration purposes
sample_dict = {
    'id': [1,2,3],
    'date': [241101,241102,241103],
    'tag': ['snacks','electricity bill','snacks'],
    'amount': [250,1000,50],
    'description': ['chips', 'bill', 'noodles']
}

sample_tag = ["snacks","bills","subcriptions"]





# Function to create and display the dashboard page, to be called later in main.py
def dashboard_page():
    #Creating the main window of dashboard page and setting its width and height to full screen
    dash_root = Tk()
    dash_root.config(bg="white")
    dash_root.geometry("{0}x{1}".format(dash_root.winfo_screenwidth(), dash_root.winfo_screenheight()))
    
    #setting 5 columns and 6 rows in dash root(main window)
    for i in range(0, 5):
        dash_root.columnconfigure(i, weight=1)  
    for i in range(0, 7):
        dash_root.rowconfigure(i, weight=1)

    #Creating a label in the dashboard page with text "dashboard" and setting its font and inserting it in row 0 and column 2
    dashboard_label = Label(dash_root, 
                            text = "Dashboard",
                            font=("Arial bold", 26),
                            bg="#e0f7fa",
                            fg="#00796b"
                            )
    dashboard_label.grid(row=0, column=2)

    #Creating a button to open input page in the dashboard page with text "Enter Data" and inserting it in row 2 and column 1
    input_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="white",
        bg="#00796b",
        borderwidth=3,
        relief="raised",
        text="Enter Data",
        padx = 10,
        pady = 10,
        command = lambda: [dash_root.destroy(), input_page(main_dictionary(), get_main_tags_set())]
        )
    input_button.grid(row=2, column=1)

    #Creating a button to open edit page in the dashboard page with text "Edit Data" and inserting it in row 2 and column 3
    edit_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="white",
        bg="#00796b",
        activebackground="#005f4f",
        borderwidth=3,
        relief="raised", 
        text="Edit Data",
        padx = 10,
        pady = 10,
        command= lambda: [dash_root.destroy(), edit_page(main_dictionary())]
        )
    edit_button.grid(row=2, column=3)

    #Creating a button to open graph page in the dashboard page with text "See data as graphs" and inserting it in row 4 and column 1
    graph_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="white",
        bg="#00796b",
        activebackground="#005f4f",        
        borderwidth=3,
        relief="raised",
        text="See data as graphs",
        padx = 10,
        pady = 10,        command= lambda: [dash_root.destroy(), graph_page()]
        )
    graph_button.grid(row=4, column=1)

    #Creating a button to open tabs page in the dashboard page with text "See data as tabs" and inserting it in row 4 and column 3
    tabs_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="white",
        bg="#00796b",
        activebackground="#005f4f",    
        borderwidth=3,
        relief="raised",
        text="See data as tabs",
        padx = 10,
        pady = 10,
        command= lambda: [dash_root.destroy(), sorting_page()]
        )
    tabs_button.grid(row=4, column=3)

    #Button to open change tags open
    change_tag_button = Button(dash_root, 
        width= int(dash_root.winfo_screenwidth()*0.015), 
        height= int(dash_root.winfo_screenheight()*0.01),
        font=("Arial",16),
        fg="white",
        bg="#00796b",
        activebackground="#005f4f",    
        borderwidth=3,
        relief="raised",
        text="Change tags", 
        padx = 10,
        pady = 10, 
        command = lambda: [dash_root.destroy(), change_tags_page()]
        )
    change_tag_button.grid(row=6, column=2)
    
    #Starting a loop to run the dash_root (main window)  
    dash_root.mainloop()




# Function to create and display the input page
def input_page(main_dict, main_tag, index=0, is_edit=False):
    # Create the main window for the input page
    input_root = Tk()
    input_root.geometry("{}x{}".format(input_root.winfo_screenwidth(), 
                                       input_root.winfo_screenheight()))
    input_root.config(bg="#e0f7fa")  # Light cyan background

    # Configure column and row weights
    input_root.columnconfigure(0, weight=1)
    for i in range(0, 6):
        input_root.rowconfigure(i, weight=1)

    # Frame for Date Entry
    cal_frame = Frame(input_root, bg="#e0f7fa")
    cal_frame.grid(column=0, row=0)
    cal_frame.columnconfigure(0, weight=1)
    cal_frame.columnconfigure(1, weight=1)
    cal_frame.rowconfigure(0, weight=1)
    
    # Frame for tag selection buttons
    tag_frame2 = Frame(input_root, bg="#e0f7fa")
    tag_frame2.grid(column=0, row=1)

    # Frame for displaying the selected tag
    tag_frame1 = Frame(input_root, bg="#e0f7fa")
    tag_frame1.grid(column=0, row=2)

    # Frame for entering amount
    amount_frame =Frame(input_root, 
                        bg="#e0f7fa")
    amount_frame.columnconfigure(0, weight=1)
    amount_frame.columnconfigure(1, weight=1)
    amount_frame.rowconfigure(0, weight=1)
    amount_frame.grid(column=0,row=3)
    
    # Frame for data entry button 
    enter_data_frame = Frame(input_root, 
                            bg="#e0f7fa")
    enter_data_frame.grid(column=0, row=4)

    # Dictionary to store tag buttons
    tag_button = dict()
    

    # Create a Date Entry widget
    cal = DateEntry(cal_frame, 
                    width=12, 
                    background="darkblue", 
                    foreground="white", 
                    borderwidth=2)
    cal.grid(row=0,column=1)

    # Label for date entry
    cal_label = Label(cal_frame, 
                      text="Enter date",
                      font=("Arial bold", 15))
    cal_label.grid(column=0, row=0)

    # Function to update the selected tag display
    def tag_updation(new_tag):
        global tag
        tag = new_tag
        tag_selection.configure(state=NORMAL)
        tag_selection.delete(0, END)
        tag_selection.insert(0,new_tag)
        tag_selection.configure(state=DISABLED, 
                                disabledbackground="white", 
                                disabledforeground="black", 
                                cursor="arrow")
    
    
    # Labels for tag selection
    tag_label = Label(tag_frame2, 
                      text="Select the tag",
                      font=("Arial bold", 15)
                      )
    tag_label.grid(column=0, row=0)

    tag_label_selected = Label(tag_frame1, 
                               text="Selected tag:",
                               font=("Arial bold", 15)
                               )
    tag_label_selected.grid(column=0, row=0)

    # Entry to display the selected tag
    tag_selection = Entry(tag_frame1, 
                          state=DISABLED,
                          font=("Arial bold", 15)
                          )
    tag_selection.grid(column=1, row=0)

    # Initialize with the first tag in the list
    tag_updation(main_tag[0])

    # Create tag buttons for each tag in main_tag list
    for i in range(len(main_tag)):
        def action(x = main_tag[i]):
            return tag_updation(x)
        
        tag_button[main_tag[i]] = Button(tag_frame2,
                                         font=("Arial bold", 15), 
                                         text=main_tag[i], 
                                         command=action)
        tag_button[main_tag[i]].grid(column=i,row=1)


    # Label and Entry for amount input
    amount_label = Label(amount_frame, 
                         text="Enter amount: ",
                         font=("Arial bold", 15)
                         )
    amount_label.grid(column=0,row=0)
    amount_entry = Entry(amount_frame,
                         font=("Arial bold", 15)
                         ) 
    amount_entry.grid(column=1, row=0)
    
    # Function to check if data is valid and excute description function afterwards
    def enter_data():
        # Error window for invalid data
        if (amount_entry.get() == "" or not amount_entry.get().isnumeric()):
            root2 = Tk()
            root2.geometry("{}x{}".format(int(root2.winfo_screenheight()*0.5), 
                                          int(root2.winfo_screenheight()*0.5)))
            
            message_label = Label(root2, 
                                  text="Enter proper data",
                                  font=("Arial bold", 15))
            message_label.pack()
            
            root2.mainloop()

        else:
            # Store amount and open description entry window
            global amount
            amount = amount_entry.get()

            # New window for description entry
            root2 = Tk()
            root2.geometry("{}x{}".format(int(root2.winfo_screenheight()), 
                                          int(root2.winfo_screenheight()*0.5)))
            root2.columnconfigure(0, weight=1)
            root2.rowconfigure(0, weight=1)
            root2.rowconfigure(1, weight=1)
            root2.rowconfigure(2, weight=1)

            description_label = Label(root2, 
                                      text="Enter Description",
                                      font=("Arial bold", 15)
                                      )
            description_label.grid(column=0, row=0)

            description_entry = Entry(root2, 
                                    width=int(root2.winfo_screenheight()*0.1),
                                    font=("Arial bold", 15)
                                    )
            description_entry.grid(column=0, row=1)

            # Finalize entry and call main function with data
            def enter_button():
                    global description

                    # Storing the initial date to year, month, day as integers 
                    uncut_date = str(cal.get_date())
                    uncut_date = uncut_date.split("-")
                    year = int(uncut_date[0][2:4])
                    month = int(uncut_date[1])
                    day = int(uncut_date[2])

                    # Format date as integer in YYMMDD
                    date = year*10000 + month*100 + day

                    # Default description if none entered
                    if (description_entry.get() == ""):
                        description = "None"
                    else:
                        description = description_entry.get()
                    
                    # Call main function for adding or editing data
                    if (is_edit == True):
                        main(date, tag, amount, description, '2', main_dict, index)
                    else:
                        main(date, tag, amount, description, '1', main_dict, 0)
                    

                        
            # Button to store the description entry    
            description_button = Button(root2, 
                                        text="Enter", 
                                        command=enter_button,
                                        font=("Arial bold", 15)
                                        )
            description_button.grid(column=0, row=2)


            
            root2.mainloop()

    # Button to store data, and start decription window
    enter_data_button = Button(enter_data_frame, 
                               text="Enter the data",
                               command= lambda: [enter_data()],
                               font=("Arial bold", 15)
                               )
    enter_data_button.grid(column=2, row=4)


    
    # Start main window loop
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
    for i in range(0, 11):
        selection_frame.columnconfigure(i, weight=1)
    selection_frame.rowconfigure(0, weight=1)

    # Initial sorting settings
    key_selected = "id"
    order_selected = "Ascending"
    color_configure="white"

    # Function to change the selected sorting key and order, and display sorted items 
    def change_selected_sort(key_selected, order_selected): 
        
        key_selected = key_clicked.get() # Get the selected key from dropdown
        order_selected = order_clicked.get() # Get the selected order from dropdown
        
        # Sort and display items based on the selected order
        if (order_selected == "Ascending"):
            Sort(main_dict).Ascend_Sorting(key_selected)
            
        else:
            Sort(main_dict).Descend_Sorting(key_selected)
            
        # Display each item in sorted order    
        for i in range(0,len(main_dict["id"])):
            dict_item(i)
        

    #Changes color of background
    def color_change(color_selected):
        color_selected=color_clicked.get().lower()
        sort_root.configure(bg=color_selected)
        sorting_frame0.configure(fg_color=color_selected)
        selection_frame.configure( bg=color_selected)
    
    # Getting main dictionary and options for sorting 
    main_dict = main_dictionary()
    key_options = list(main_dict.keys())
    order_options = ["Ascending","Descending"]
    color_options=["Black","White","Lightblue","Red","Pink","Gray","Orange","Blue"]

    # Variables to store dropdown menu selections 
    key_clicked = StringVar() 
    order_clicked = StringVar()
    color_clicked= StringVar()

    # Set initial menu text  
    key_clicked.set("id")
    order_clicked.set("Ascending") 
    color_clicked.set("White")
    
    # Create Dropdown menus for key and order, and  colors
    order_drop = OptionMenu(selection_frame , 
                            order_clicked, 
                            *order_options,
                            ) 
    order_drop.config(font=("Arial bold",10))
    key_drop = OptionMenu(selection_frame, 
                            key_clicked, 
                            *key_options,
                            )
    key_drop.config(font=("Arial bold",10))
    colors_drop=OptionMenu(selection_frame, 
                            color_clicked, 
                            *color_options,
                            )
    colors_drop.config(font=("Arial bold",10))

    # Create button, it start the sorting 
    button = Button( selection_frame , 
                    text = "Sort", 
                    command = lambda: change_selected_sort(key_selected, order_selected),
                    font=("Arial bold",10) 
                    )
    button_color=Button(selection_frame,text="Change Color",
                        command=lambda: color_change(color_clicked), 
                        font=("Arial bold",10)
                        )

    # Place dropdown menus and button in grid
    key_drop.grid(column=1, row=0,padx=2)
    order_drop.grid(column=3, row=0,padx=2)
    colors_drop.grid(column=5,row=0,padx=2)
    button.grid(column=7, row=0,padx=2)
    button_color.grid(column=9, row=0,padx=2)


    #Creating and configuring a frame separate for displaying sorted dictionary
    sorting_frame0 = customtkinter.CTkScrollableFrame(sort_root,
                                                     orientation="vertical", 
                                                     width=sort_root.winfo_screenwidth()*0.95,
                                                     height=sort_root.winfo_screenheight()*0.80,
                                                     fg_color="white"
                                                     )
    
    sorting_frame0.grid(column=0, row=1)
    sorting_frame0.columnconfigure(0, weight=1)
    # Configure rows based on number of items in dictionary
    for i in range(0, len(main_dict["id"])+1):
        sorting_frame0.rowconfigure(i, weight=1)
    
    # Dictionary to hold item frames and buttons for displaying full data
    dict_frame = dict()
    full_data_button = dict()

    # Function to display each item in the sorted dictionary
    def dict_item(index):

        # Create a frame for each item
        dict_frame[index] = Frame(sorting_frame0, width=sorting_frame0.winfo_screenwidth())
        dict_frame[index].grid(column=0,row=index+1)
        
        # Set layout for item information in columns
        for i in range(0,5):
            dict_frame[index].columnconfigure(i, weight=1)
        dict_frame[index].rowconfigure(0, weight=1)

        # Function to display the description in a new window
        def display_description(index = index):
            sort_root = Tk()
            sort_root.geometry("{}x{}".format(sort_root.winfo_screenheight(), sort_root.winfo_screenheight()))
            description_label = Label(sort_root, text=main_dict["description"][index])
            description_label.pack()
            sort_root.mainloop()
            sorting_page()
        
        # Button to view description
        full_data_button[index] = Button(dict_frame[index], 
                                        text=">", 
                                        command=lambda: [sort_root.destroy(),display_description(index)], 
                                        width=int(dict_frame[index].winfo_screenwidth()*(0.2)))
        full_data_button[index].grid(column=0, row=0)

        id_label = Label(dict_frame[index], 
                        text=main_dict['id'][index], 
                        width=int(dict_frame[index].winfo_screenwidth()*(9/40))
                        )
        id_label.grid(column=1, row=0)

        # Converting date from YYMMDD to DD/MM/YY
        date = str(main_dict['date'][index])
        day = date[4:6]
        month = date[2:4]
        year = date[0:2]
        date_label = Label(dict_frame[index], 
                            text=f"{day}/{month}/{year}", 
                            width=int(dict_frame[index].winfo_screenwidth()*(9/40))
                            )
        date_label.grid(column=2,row=0)

        tag_label = Label(dict_frame[index], 
                            text=main_dict["tag"][index], 
                            width=int(dict_frame[index].winfo_screenwidth()*(9/40))
                            )
        tag_label.grid(column=3,row=0)

        amount_label = Label(dict_frame[index], 
                            text=main_dict["amount"][index], 
                            width=int(dict_frame[index].winfo_screenwidth()*(9/40))
                            )
        amount_label.grid(column=4,row=0)

    # Frame header for displaying labels of the columns (id, date, tag, amount)
    dict_frame0 = Frame(sorting_frame0)
    dict_frame0.grid(column=0,row=0)
    for i in range(0, 5):
        dict_frame0.columnconfigure(i, weight=1)
    dict_frame0.rowconfigure(0, weight=1)

    # Header labels for the columns
    description_button_label = Label(dict_frame0, 
                              text="Description", 
                              width=int(dict_frame0.winfo_screenwidth()*0.2), 
                              padx=5
                              )
    description_button_label.grid(column=0, row=0)
    id_label0 = Label(dict_frame0, 
                      text="id",
                      width=int(dict_frame0.winfo_screenwidth()*(9/40)),
                      highlightbackground='black', 
                      highlightthickness=1
                      )
    id_label0.grid(column=1, row=0)
    date_label0 = Label(dict_frame0, 
                        text="date",
                        width=int(dict_frame0.winfo_screenwidth()*(9/40)),
                        highlightbackground='black', 
                        highlightthickness=1
                        )
    date_label0.grid(column=2,row=0)
    tag_label0 = Label(dict_frame0, 
                       text="tags",
                       width=int(dict_frame0.winfo_screenwidth()*(9/40)),
                       highlightbackground='black', 
                       highlightthickness=1
                       )
    tag_label0.grid(column=3,row=0)
    amount_label0 = Label(dict_frame0, 
                          text="amount",
                          width=int(dict_frame0.winfo_screenwidth()*(9/40)),
                          highlightbackground='black', 
                          highlightthickness=1
                          )
    amount_label0.grid(column=4,row=0)
    
    # Perform sorting and display items based on initial selected order
    if (order_selected == "Ascending"):
        Sort(main_dict).Ascend_Sorting(key_selected)
    else:
        Sort(main_dict).Descend_Sorting(key_selected)

    for i in range(0,len(main_dict["id"])):
            dict_item(i)

    # Start the Tkinter main loop 
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
    edit_data_button = dict()
    delete_data_button = dict()
    def dict_item(index):

        dict_frame[index] = Frame(edit_frame, width=edit_frame.winfo_screenwidth())
        dict_frame[index].grid(column=0,row=index+1)
        for i in range(0, 6):
            dict_frame[index].columnconfigure(i, weight=1)

        dict_frame[index].rowconfigure(0, weight=1)

        def edit_command(selected_id):
            input_page(main_dict, get_main_tags_set(), index=selected_id, is_edit=True)

        def delete_command(selected_id):
            pass
        

        edit_button_width = int(edit_frame.winfo_screenwidth()*(1.44/100))
        edit_data_button[index] = Button(dict_frame[index], 
                                        text="Edit", 
                                        command=lambda: [edit_root.destroy(), edit_command(main_dict['id'][index])], 
                                        width=edit_button_width,
                                        )
        edit_data_button[index].propagate(0)
        edit_data_button[index].grid(column=0, row=0)

        delete_button_width = int(edit_frame.winfo_screenwidth()*(1.44/100))
        delete_data_button[index] = Button(dict_frame[index], 
                                        text="delete", 
                                        command=lambda: [edit_root.destroy(), delete_command(main_dict['id'][index])], 
                                        width=delete_button_width,
                                        fg="black",
                                        )
        delete_data_button[index].propagate(0)
        delete_data_button[index].grid(column=1, row=0)

        labels_width = int(edit_frame.winfo_screenwidth()*(4/100))
        id_label = Label(dict_frame[index], 
                        text=main_dict['id'][index], 
                        width=labels_width
                        )
        id_label.propagate(0)
        id_label.grid(column=2, row=0)

        date = str(main_dict['date'][index])
        day = date[4:6]
        month = date[2:4]
        year = date[0:2]
        date_label = Label(dict_frame[index], text=f"{day}/{month}/{year}", 
                           width=labels_width
                           )
        date_label.propagate(0)
        date_label.grid(column=3,row=0)

        tag_label = Label(dict_frame[index], 
                          text=main_dict["tag"][index], 
                          width=labels_width
                          )
        tag_label.propagate(0)
        tag_label.grid(column=4,row=0)

        amount_label = Label(dict_frame[index], 
                            text=main_dict["amount"][index], 
                            width=labels_width
                            )
        amount_label.propagate(0)
        amount_label.grid(column=5,row=0)

        



    
    dict_frame0 = Frame(edit_frame, width=edit_frame.winfo_screenwidth())
    dict_frame0.grid(column=0,row=0)
    dict_frame0.columnconfigure(0, weight=1)
    dict_frame0.columnconfigure(1, weight=1)
    dict_frame0.columnconfigure(2, weight=1)
    dict_frame0.columnconfigure(3, weight=1)
    dict_frame0.columnconfigure(4, weight=1)
    dict_frame0.rowconfigure(0, weight=1)


    edit_button_width0 = int(edit_frame.winfo_screenwidth()*(3/100))
    edit_data_button0 = Button(dict_frame0, 
                            text="Edit",
                            padx=12,
                            width=edit_button_width0,
                            )
    edit_data_button0.propagate(0)
    edit_data_button0.grid(column=0, row=0)

    delete_button_width0 = int(edit_frame.winfo_screenwidth()*(3/100))
    delete_data_label0 = Button(dict_frame0, 
                                text="delete", 
                                width=delete_button_width0,
                                fg="black",
                                padx=12,
                                )
    delete_data_label0.propagate(0)
    delete_data_label0.grid(column=1, row=0)

    labels_width0 = int(edit_frame.winfo_screenwidth()*(4.8/100))
    id_label0 = Label(dict_frame0, 
                    text="id",
                    width=labels_width0,
                    padx=20
                    )
    id_label0.propagate(0)
    id_label0.grid(column=2, row=0)

    date_label0 = Label(dict_frame0, text="date",
                        width=labels_width0
                        )
    date_label0.propagate(0)
    date_label0.grid(column=3,row=0)

    tag_label0 = Label(dict_frame0, 
                        text="tags",
                        width=labels_width0
                        )
    tag_label0.propagate(0)
    tag_label0.grid(column=4,row=0)

    amount_label0 = Label(dict_frame0, 
                          text="amount",
                          width=labels_width0
                          )
    amount_label0.propagate(0)
    amount_label0.grid(column=5,row=0)

   
    
    for i in range(0, len(main_dict["id"])):
        dict_item(i)

    # Execute tkinter 
    edit_root.mainloop()


def graph_page():
    main_dict = main_dictionary().copy()
    graph_root = Tk()
    graph_root.geometry("{}x{}".format(graph_root.winfo_screenwidth(), graph_root.winfo_screenheight()))
    graph_root.columnconfigure(0, weight=1)
    graph_root.rowconfigure(0, weight=1)
    graph_root.rowconfigure(1, weight=1)
    graph_root.rowconfigure(2, weight=1)


    #Creating the graph label
    graph_main_label = Label(graph_root, text="Graph Page")
    graph_main_label.grid(column=0, row=0)

    #Creating and configuring a frame separate for selecting key in dictionary to sort by
    selection_frame = Frame(graph_root)
    selection_frame.grid(column=0, row=1)
    selection_frame.columnconfigure(0, weight=1)
    selection_frame.columnconfigure(1, weight=1)
    selection_frame.columnconfigure(2, weight=1)
    selection_frame.columnconfigure(3, weight=1)
    selection_frame.rowconfigure(0, weight=1)

    graph_frame1 = Frame(graph_root)
    graph_frame1.grid(column=0, row=2)
    
    graph_selected = 'pie'
    year_selected = '24'
    month_selected = '11'
    # Change the selected sorting 
    def change_graph(graph_selected, year_selected): 
        graph_selected = graph_clicked.get()
        year_selected = year_clicked.get()
        month_selected = month_clicked.get()


        fig = Figure()

        plot1 = fig.add_subplot(111)
        

        if (graph_selected == 'pie chart'):
            print(main_dict)
            amount, tag = pie_individual_tag(main_dict, year_selected, month_selected)
            plot1.pie(amount, labels=tag, autopct='%1.1f%%')


        elif (graph_selected == 'bar chart'):
            data1, data2 = bar_total(main_dict, year_selected)
            
            plot1.bar(data1, data2)
            

        canvas = FigureCanvasTkAgg(fig, master=graph_frame1) 
        canvas.get_tk_widget().grid(column=0,row=0)


    year_set = set()
    month_set = set()
    for index in range(0, len(main_dict['date'])): 
        date = str(main_dict['date'][index])
        month_set.add(date[2:4])
        year_set.add(date[0:2])

    # Dropdown menu options 
    graph_options = ["bar chart", 'pie chart']
    year_options = year_set
    month_options=month_set

    # datatype of menu text 
    graph_clicked = StringVar() 
    year_clicked = StringVar()
    month_clicked = StringVar()
    
    # initial menu text 
    graph_clicked.set("bar chart")
    year_clicked.set(list(year_set)[0])
    month_clicked.set(list(month_set)[0]) 
    
    # Create Dropdown menu 
    year_drop = OptionMenu(selection_frame , year_clicked, *year_options) 
    graph_drop = OptionMenu(selection_frame , graph_clicked, *graph_options)
    month_drop = OptionMenu(selection_frame , month_clicked, *month_options)  
    
    # Create button, it start the sorting 
    button = Button( selection_frame , text = "change" , command = lambda: change_graph(graph_selected, year_selected) )
    
    #Assigning grid placement to each element
    graph_drop.grid(column=0, row=0)
    year_drop.grid(column=1, row=0)
    month_drop.grid(column=2,row=0)
    button.grid(column=3, row=0)

        

    graph_root.mainloop()


def change_tags_page():
    tag_page_root = Tk()
    tag_page_root.geometry("{}x{}".format(tag_page_root.winfo_screenwidth(), tag_page_root.winfo_screenheight()))
    tag_page_root.columnconfigure(0, weight=1)
    tag_page_root.rowconfigure(0, weight=1)
    tag_page_root.rowconfigure(1, weight=1)

    selection_frame = Frame(tag_page_root)
    selection_frame.grid(column=0, row=1)
    selection_frame.columnconfigure(0, weight=1)
    selection_frame.columnconfigure(1, weight=1)
    selection_frame.rowconfigure(0, weight=1)

    tag_enter_frame = Frame(tag_page_root)
    tag_enter_frame.grid(column=0, row=0)
    tag_enter_frame.columnconfigure(0, weight=1)
    tag_enter_frame.rowconfigure(0, weight=1)
    tag_enter_frame.rowconfigure(1, weight=1)

    def change_tag(is_reset = False):
        tags_set = set()
        tags = tag_entry.get()
        
        for tag in tags.split():
            tags_set.add(tag)

        
        if (is_reset == True):
            setup_tags_file(tags_set, True)
        else:
            setup_tags_file(tags_set, False)

    

    reset_tag_button = Button(selection_frame, text="Reset tags", command=lambda: change_tag(True))
    add_tag_button = Button(selection_frame, text="Add tags", command=lambda: change_tag(False))

    reset_tag_button.grid(column=0, row=0)
    add_tag_button.grid(column=1, row=0)

    tag_label = Label(tag_enter_frame, text="Enter tags with space between each tag")    
    tag_entry = Entry(tag_enter_frame, width=int(tag_enter_frame.winfo_screenheight()*0.1))

    tag_label.grid(column=0, row=0)
    tag_entry.grid(column=0, row=1)

    tag_page_root.mainloop()



#dashboard_page()
#input_page(main_dictionary(), get_main_tags_set())
#sorting_page()
#edit_page()
#graph_page()
#change_tags_page()

