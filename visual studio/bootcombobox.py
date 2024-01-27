from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
#combobox(default)
# default combobox style
Combobox()
# danger colored combobox style
c1=Combobox(win,values=["Myd","tvr"],bootstyle="success")
c1.place(relx=0.02,rely=0.1)

#other combobox
# create the combobox in a disabled state
c1=Combobox(state="disabled")
c1.place(relx=0.02,rely=0.4)
# disable a combobox after creation
cb = Combobox(win,text="disabled")
cb.place(relx=0.02,rely=0.5)
cb.configure(state="disabled")
'''
#readonly combobox
# create the combobox in a readonly state
c1=Combobox(state="readonly")
c1.place(relx=0.02,rely=0.3)
# set the combobox readonly state after creation
cb = Combobox()
cb.place(relx=0.02,rely=0.4)
cb.configure(state="readonly")

win.mainloop()