import os
from tkinter import *
from tkinter import messagebox
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")

#solid button(default)
# default style
b=Button(win,text="hello")
b.place(relx=0.01,rely=0.2)
# success style
a=Button(win,bootstyle="success")
a.place(relx=0.01,rely=0.3)

#Line button
b=Button(win,text="success")
b.place(relx=0.2,rely=0.5)
b=Button(win,bootstyle="success-outline")
b.place(relx=0.2,rely=0.6)

#Link button
b=Button(win,text="success")
b.place(relx=0.3,rely=0.7)
b=Button(win,bootstyle="success-link")
b.place(relx=0.3,rely=0.8)

win.mainloop()