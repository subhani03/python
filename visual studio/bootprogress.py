from tkinter import *
from ttkbootstrap import *
win=Tk()
win.geometry("400x400")
'''
# default solid progressbar style
p=Progressbar(win,cursor="5")
p.place(relx=0.2,rely=0.5)
# success colored solid progressbar style
p1=Progressbar(win,bootstyle="danger")
p1.place(relx=0.2,rely=0.5)
'''
#striped
# default striped progressbar style
p=Progressbar(win,bootstyle="striped")
p.place(relx=0.2,rely=0.5)
# danger colored striped progressbar style
p1=Progressbar(win,bootstyle="danger-striped")
p1.place(relx=0.2,rely=0.6)
win.mainloop()
