from tkinter import *
from tkcalendar import DateEntry

sample_dict = {
    'id': [1,2,3],
    'date': [241101,241102,241103],
    'tag': ['snaks','electricity bill','snacks'],
    'amount': [250,1000,50],
    'description': ['chips', 'bill', 'noodles']
}

sample_tag = ["snacks","bills","subcription"]

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
    
    date = int()
    tag = ""
    tag_button = dict()
    amount = int()
    description = ""

    def tag_updation(new_tag):
        tag_label.configure(state=NORMAL)
        tag_label.delete(0, END)
        tag_label.insert(0,new_tag)
        tag_label.configure(state=DISABLED)

    
    tag_label = Entry(root, state=DISABLED)
    tag_label.grid(column=0, row=2)

    # Create a Date Entry widget
    cal = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
    cal.grid(row=0,column=0)

    for i in range(len(main_tag)):
        def action(x = main_tag[i]):
            return tag_updation(x)
        
        tag_button[main_tag[i]] = Button(root, text=main_tag[i], command=action)
        tag_button[main_tag[i]].grid(column=i,row=1)

    


    root.mainloop()