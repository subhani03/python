from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default panedwindow style
p=Panedwindow(win)
p.place(relx=0.2,rely=0.5)
# info colored panedwindow style
p1=Panedwindow(win,bootstyle="info")
p1.place(relx=0.2,rely=0.6)
win.mainloop()