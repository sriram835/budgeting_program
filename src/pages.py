from tkinter import *
from tkcalendar import DateEntry

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
        command=lambda: [input_page(sample_dict, sample_tag)]
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
        text="See data as tabs"
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

    tag_frame1 = Frame(root)
    tag_frame1.grid(column=0, row=2)

    tag_frame2 = Frame(root)
    tag_frame2.grid(column=0, row=1)

    cal_frame = Frame(root)
    cal_frame.grid(column=0, row=0)

    date = int()
    tag_button = dict()
    amount = int()
    description = ""

    def tag_updation(new_tag):
        tag_selection.configure(state=NORMAL)
        tag_selection.delete(0, END)
        tag_selection.insert(0,new_tag)
        tag_selection.configure(state=DISABLED, disabledbackground="white",disabledforeground="black", cursor="arrow")
        global tag
        tag = new_tag
    
    

    tag_label = Label(tag_frame2, text="Select the tag")
    tag_label.grid(column=0, row=0)

    tag_label_selected = Label(tag_frame1, text="Selected tag:")
    tag_label_selected.grid(column=0, row=0)

    tag_selection = Entry(tag_frame1, state=DISABLED)
    tag_selection.grid(column=1, row=0)

    tag_updation("")
    
    # Create a Date Entry widget
    cal = DateEntry(cal_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
    cal.grid(row=0,column=0)

    for i in range(len(main_tag)):
        def action(x = main_tag[i]):
            return tag_updation(x)
        
        tag_button[main_tag[i]] = Button(tag_frame2, text=main_tag[i], command=action)
        tag_button[main_tag[i]].grid(column=i,row=1)


    def input_amount():
        amount = amount_entry.get()
        return amount

    #amount_entry = Entry(root)
    #amount_entry.insert(0, "Enter the amount")
    #amount_entry.bind("<FocusIn>", lambda args: [amount_entry.delete('0', 'end')])
    #amount_entry.bind("<FocusOut>", lambda args: [input_amount()])
    
   
    #amount_entry.grid(column=0, row=4)
    

    def enter_data():
        pass

    #enter_data_button = Button(root, text="Enter the data",command=enter_data)
    #enter_data_button.grid(column=2, row=4)


    root.mainloop()


input_page(sample_dict, sample_tag)