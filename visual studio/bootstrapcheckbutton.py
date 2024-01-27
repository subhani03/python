from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
#checkbutton(default)
c=Checkbutton(win,text="success")
c.place(relx=0.02,rely=0.1)
c1=Checkbutton(win,bootstyle="success")
c1.place(relx=0.02,rely=0.2)

#Toolbutton
#default toolbutton style
c1=Checkbutton(win,bootstyle="toolbutton")
c1.place(relx=0.02,rely=0.1)
# success toolbutton style
c2=Checkbutton(bootstyle="success-toolbutton")
c2.place(relx=0.02,rely=0.1)

#Outline toolbutton
# default outline toolbutton style
c1=Checkbutton(win,text="success")
c1.place(relx=0.02,rely=0.1)
# success outline toolbutton style
c2=Checkbutton(win,text="success",bootstyle="success-outline-toolbutton")
c2.place(relx=0.02,rely=0.2)

#Round toggle button
# default round toggle style
c1=Checkbutton(win,text="primary",bootstyle="round-toggle")
c1.place(relx=0.02,rely=0.3)
# success round toggle style
c2=Checkbutton(win,text="secondary",bootstyle="success-round-toggle")
c2.place(relx=0.02,rely=0.4)

#square toggle button
# default square toggle style
c1=Checkbutton(win,text="ON",bootstyle="square-toggle")
c1.place(relx=0.02,rely=0.4)
# success square toggle style
c2=Checkbutton(win,text="OFF",bootstyle="success-square-toggle")
c2.place(relx=0.02,rely=0.5)
'''
#other checkbutton(disabled button)
# create the checkbutton in a disabled state
c1=Checkbutton(state="disabled")
c1.place(relx=0.02,rely=0.3)
# disable a checkbutton after creation
cb = Checkbutton(win,text="disabled")
cb.place(relx=0.02,rely=0.4)
cb.configure(state="disabled")

win.mainloop()
