import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
win=Tk()
win.geometry("500x500")
frame=Frame(win,width=100,height=100)
frame.pack()
frame.place(relx=0.3,rely=0.001)
img=ImageTk.PhotoImage(Image.open("panda.jpg"))
label=Label(frame,image=img)
label.pack()

l1=Label(win,text="Name")
l1.place(relx=0.005,rely=0.5)
l2=Label(win,text="Father Name")
l2.place(relx=0.005,rely=0.6)
l3=Label(win,text="Mother Name")
l3.place(relx=0.005,rely=0.7)
l4=Label(win,text="Email-ID")
l4.place(relx=0.005,rely=0.8)
l5=Label(win,text="Contact")
l5.place(relx=0.005,rely=0.9)

e1=Entry(win)
e1.place(relx=0.2,rely=0.5)
e2=Entry(win)
e2.place(relx=0.2,rely=0.6)
e3=Entry(win)
e3.place(relx=0.2,rely=0.7)
e4=Entry(win)
e4.place(relx=0.2,rely=0.8)
e5=Entry(win)
e5.place(relx=0.2,rely=0.9)

r=Label(win,text="Gender")
r.place(relx=0.5,rely=0.5)
var=IntVar()
r1=Radiobutton(win,text="Male",variable="var",value=1)
r1.place(relx=0.6,rely=0.5)
r2=Radiobutton(win,text="Female",variable="var",value=2)
r2.place(relx=0.7,rely=0.5)

combo1=Label(win,text="country")
combo1.place(relx=0.5,rely=0.6)
combo=ttk.Combobox(win,values=["India","USA","Australia","Europe","Island"])
combo.place(relx=0.6,rely=0.6)

text1=Label(win,text="Remark")
text1.place(relx=0.5,rely=0.7)
text2=Text(win,height=2,width=18)
text2.place(relx=0.6,rely=0.7)

def func():
    tkinter.messagebox.showwarning("Excellent")

b1=Button(win,text="submit",command=func)
b1.place(relx=0.7,rely=0.9)
win.mainloop()