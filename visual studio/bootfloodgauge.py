from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default floodgauge style
f=Floodgauge(win)
f.place(relx=0.2,rely=0.5)
# success colored floodguage style
f1=Floodgauge(win,bootstyle="success",text="default")
f1.place(relx=0.2,rely=0.6)
win.mainloop()