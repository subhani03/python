from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
#Label
# default label style
l=Label(win,text="success")
l.place(relx=0.02,rely=0.1)
# danger colored label style
l2=Label(win,text="hello",bootstyle="success")
l2.place(relx=0.02,rely=0.2)

#inverse label
# default inverse label style
l3=Label(bootstyle="inverse")
l3.place(relx=0.2,rely=0.5)
# danger colored inverse label style
l4=Label(win,text="hello",bootstyle="inverse-danger")
l4.place(relx=0.2,rely=0.6)
'''
#Label frame
# default labelframe style
l5=Labelframe(win,text="hj")
l5.place(relx=0.2,rely=0.5)
# info colored labelframe style
l6=Labelframe(win,bootstyle="info",text="ghf")
l6.place(relx=0.2,rely=0.6)

win.mainloop()