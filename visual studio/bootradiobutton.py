from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
# default radiobutton style
r=Radiobutton(win,text="yes")
r.place(relx=0.2,rely=0.5)
# secondary colored radiobutton style
r1=Radiobutton(win,text="No",bootstyle="secondary")
r1.place(relx=0.2,rely=0.6)

#outline
# default outline radio toolbutton style
r=Radiobutton(win,text="yes",bootstyle="outline-toolbutton")
r.place(relx=0.2,rely=0.5)
# info colored outline radio toolbutton style
r1=Radiobutton(win,text="no",bootstyle="info-outline-toolbutton")
r1.place(relx=0.2,rely=0.6)

#solid tool
# default toolbutton style
r=Radiobutton(win,text="yes",bootstyle="toolbutton")
r.place(relx=0.2,rely=0.5)
# danger colored radio toolbutton style
r1=Radiobutton(win,text="no",bootstyle="danger-toolbutton")
r1.place(relx=0.2,rely=0.6)
'''
#disabled
# create the radiobutton in a disabled state
r=Radiobutton(win,text="yes",state="disabled")
r.place(relx=0.2,rely=0.5)
# disable a radiobutton after creation
rb = Radiobutton(win,text="no")
rb.place(relx=0.2,rely=0.6)
rb.configure(state="disabled")
win.mainloop()