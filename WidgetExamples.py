import tkinter

#window
my_window=tkinter.Tk()
my_window.title("Tkinter Python")
my_window.minsize(width=600,height=600)
my_window.config(padx=20,pady=20)

#label
my_label = tkinter.Label(text="My Label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10,pady=10)
my_label.pack()

#button
def button_clicked():
    print("Button Clicked")
    print(my_text.get("1.0",tkinter.END))

my_button=tkinter.Button(text="Button",command=button_clicked)
my_button.config(padx=10,pady=10)
my_button.pack()

#entry
my_entry=tkinter.Entry(width=20)
my_entry.pack()
#my_entry.focus()

#text
my_text=tkinter.Text(width=30,height=5)
my_text.pack()


def scale_selected(value):
    print(value)

my_scale=tkinter.Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()


def spinbox_selected():
    print(my_spinbox.get())
my_spinbox=tkinter.Spinbox(from_=0,to=50,command=spinbox_selected)
my_spinbox.pack()

def checkbutton_selected():
    print(check_state.get())



check_state=tkinter.IntVar()
my_checkbutton=tkinter.Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()

#radio_button

def radio_selected():
    print(radio_checked_state.get())


radio_checked_state=tkinter.IntVar()
my_radiobutton=tkinter.Radiobutton(text="1.Option",value=10,variable=radio_checked_state,command=radio_selected)
my_radiobutton_2=tkinter.Radiobutton(text="2.Option",value=20,variable=radio_checked_state,command=radio_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox

def listbox_selected():
    print(my_listbox.get(my_listbox.curselection()))

my_listbox=tkinter.Listbox()
name_list=["Atil","ABC","KJF","SKDDfk","KJSFkjda"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>',listbox_selected)
my_listbox.pack()



my_window.mainloop()