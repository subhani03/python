from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
# default solid menubutton style
m=Menubutton(win,text="default")
m.place(relx=0.2,rely=0.5)
# success colored solid menubutton style
m1=Menubutton(win,bootstyle="success",text="default")
m1.place(relx=0.2,rely=0.6)

#outline
# default outline menubutton style
m=Menubutton(win,bootstyle="outline")
m.place(relx=0.2,rely=0.5)
# info colored outline menubutton style
m1=Menubutton(win,bootstyle="info-outline")
m1.place(relx=0.2,rely=0.6)
'''
#disabled
# create the menubutton in a disabled state
m=Menubutton(win,state="disabled")
m.place(relx=0.2,rely=0.5)
# disable a menubutton after creation
b = Menubutton(win)
b.place(relx=0.2,rely=0.6)
b.configure(state="disabled")
win.mainloop()