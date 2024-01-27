from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
# default Scale style
s=Scale(win)
s.place(relx=0.2,rely=0.5)
# info colored label style
s1=Scale(win,bootstyle="info")
s1.place(relx=0.2,rely=0.6)
'''
# create the scale in a disabled state
s=Scale(win,state="disabled")
s.place(relx=0.2,rely=0.5)
# disable a scale after creation
scale = Scale()
scale.place(relx=0.2,rely=0.6)
scale.configure(state="disabled")

win.mainloop()
