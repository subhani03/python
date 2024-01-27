from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default meter style
m=Meter()
m.place(relx=0.2,rely=0.5)
# info colored meter
m1=Meter(bootstyle="info")
m1.place(relx=0.2,rely=0.6)
# danger color subtext
m2=Meter(subtextstyle="danger")
m2.place(relx=0.2,rely=0.7)
# success colored meter with warning colored subtext
m3=Meter(bootstyle="success", subtextstyle="warning")
m3.place(relx=0.2,rely=0.8)

win.mainloop()