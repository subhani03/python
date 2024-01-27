from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
# default entry style
e=Entry(win)
e.place(relx=0.2,rely=0.5)
# danger colored entry style
e1=Entry(win,bootstyle="danger")
e1.place(relx=0.2,rely=0.6)
'''
#other disabled
# create the widget in a disabled state
e1=Entry(win,state="disabled")
e1.place(relx=0.2,rely=0.5)
# disable the widget after creation
e = Entry(win)
e.place(relx=0.2,rely=0.6)
e.configure(state="disabled")
'''
# create the widget in a readonly state
e1=Entry(win,state="readonly")
e1.place(relx=0.2,rely=0.5)
# set the widget readonly state after creation
e = Entry(win)
e.place(relx=0.2,rely=0.6)
e.configure(state="readonly")
'''
win.mainloop()