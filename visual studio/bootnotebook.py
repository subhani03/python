from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default notebook style
n=Notebook(win)
n.place(relx=0.2,rely=0.5)
# info colored notebook style - inactive tab color
n1=Notebook(win,bootstyle="info")
n1.place(relx=0.2,rely=0.6)
win.mainloop()