from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")

#disabled spinbox
# create the widget in a disabled state
s1=Spinbox(win,state="disabled")
s1.place(relx=0.2,rely=0.5)

# disable the widget after creation
e = Spinbox(win)
e.place(relx=0.2,rely=0.6)
e.configure(state="disabled")

#readonly
# create the widget in a readonly state
s1=Spinbox(win,state="readonly")
s1.place(relx=0.2,rely=0.6)

# set the widget readonly state after creation
e = Spinbox(win)
e.place(relx=0.2,rely=0.7)
e.configure(state="readonly")
win.mainloop()

""" # default Treeview style
t=Treeview(win)
t.place(relx=0.2,rely=0.5)
# info colored treeview style
t1=Treeview(win,bootstyle='info')
t1.place(relx=0.2,rely=0.6)
win.mainloop() """