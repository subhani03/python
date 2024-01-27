from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default frame style
#f=Frame(win,bg="red",width=49,height=34)

#f.place(relx=0.2,rely=0.5)
# info colored frame style
f1=Frame(win,bootstyle="info",width=78,height=89)
f1.place(relx=0.2,rely=0.6)
win.mainloop()