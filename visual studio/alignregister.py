import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
win=Tk()
win.geometry("500x500")
frame=Frame(win,width=200,height=100)
frame.pack()
frame.place(relx=0.3,rely=0)
img=ImageTk.PhotoImage(Image.open("registerimg.jpg"))
label=Label(frame,image=img)
label.pack()

l1=Label(win,text="Name")
l1.place(relx=0.05,rely=0.5)
l2=Label(win,text="Father Name")
l2.place(relx=0.05,rely=0.6)
l3=Label(win,text="Email-ID")
l3.place(relx=0.05,rely=0.7)
l4=Label(win,text="Mobile No")
l4.place(relx=0.05,rely=0.8)

e1=Entry(win)
e1.place(relx=0.2,rely=0.5)
e2=Entry(win)
e2.place(relx=0.2,rely=0.6) 
e3=Entry(win)
e3.place(relx=0.2,rely=0.7)
e4=Entry(win)
e4.place(relx=0.2,rely=0.8)   

r=Label(win,text="Gender")
r.place(relx=0.5,rely=0.5)
var=IntVar()
r1=Radiobutton(win,text="Male",variable=var,value=1)
r1.place(relx=0.6,rely=0.5)
r2=Radiobutton(win,text="Female",variable=var,value=2)
r2.place(relx=0.7,rely=0.5)

c1=Label(win,text="city")
c1.place(relx=0.5,rely=0.6)
combo=ttk.Combobox(win,values=["Mayiladuthurai","Thanjavur","Thiruvarur","Nagapattinam","Madurai","Chennai"])
combo.place(relx=0.6,rely=0.6)

t1=Label(win,text="Address")
t1.place(relx=0.5,rely=0.7)
t2=Text(win,height=2,width=30)
t2.place(relx=0.6,rely=0.7)
t3=Label(win,text="Remarks")
t3.place(relx=0.5,rely=0.8)
t4=Text(win,height=2,width=18)
t4.place(relx=0.6,rely=0.8) 

def func():
    tkinter.messagebox.showwarning("Excellent")

def reg():
    f=open('alignreg.txt','a')
    f.write('\n')
    f.write(e1.get())
    f.write('\t')
    f.write(e2.get())
    f.write('\t')
    f.write(e3.get())
    f.write('\t')
    f.write(e4.get())
    f.write('\t')
    f.write(str(var.get()))
    f.write('\t') 
    f.write(str(combo.get()))
    f.write('\t')
    f.write(str(t2.get(1.0,END)))
    f.write('\t')
    f.write(str(t4.get(1.0,END)))
    f.write('\t')
    
img1=ImageTk.PhotoImage(Image.open("regr.jpg"))
label1=Button(win,image=img1,activebackground="red",command=reg)
label1.place(relx=0.6,rely=0.9)

win.mainloop()


         
         
         