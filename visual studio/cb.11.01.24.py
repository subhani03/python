from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("400x400")
root.title("Computer Science")
combo=ttk.Combobox(root,values=["Digital image processing","Machine Learning","IOT","Artificial Intelligence","Blockchain Technology"])
combo.pack()

def option_selected(event):
    selected_option=combo.get()
    print("you are selected: ",  selected_option)
combo.bind("<<ComboboxSelected>>",option_selected)
root.mainloop()
