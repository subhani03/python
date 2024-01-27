from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
# default separator style
s=Separator(win)
s.place(relx=0.2,rely=0.5)
# info colored separator style - handle color
s1=Separator(win,bootstyle="info")
s1.place(relx=0.2,rely=0.6)
'''
#sizegrip
# default sizegrip style
Sizegrip()

# info colored sizegrip style - handle color
Sizegrip(bootstyle="info")
'''
win.mainloop()
