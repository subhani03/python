from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
# default date entry
d1=DateEntry(win)
d1.place(relx=0.2,rely=0.5)
# success colored date entry
d2=DateEntry(win,bootstyle="success")
d2.place(relx=0.2,rely=0.6)

#other
# create the date entry in a disabled state
DateEntry(state="disabled")

# disable a date entry after creation
d = DateEntry()
d.configure(state="disabled")
'''
#readonly dateentry
# create the date entry in a readonly state
d1=DateEntry(win,state="readonly")
d1.place(relx=0.2,rely=0.5)
# set the date entry readonly state after creation
d = DateEntry(win)
d.place(relx=0.2,rely=0.6)
d.configure(win,state="readonly")

win.mainloop()