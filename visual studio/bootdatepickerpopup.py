from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default popup
d=DatePickerPopup(win)
d.place(relx=0.2,rely=0.5)
# warning colored popup
d1= DatePickerPopup(win,bootstyle="warning")
d1.place(relx=0.2,rely=0.6)
win.mainloop()