from tkinter import *
root=Tk()

l1=Label(root,text="username")
l1.grid(row=0,column=1)
l2=Label(root,text="password")
l2.grid(row=1,column=1)

e1=Entry(root)
e1.grid(row=0,column=2,padx=10,pady=10)
e2=Entry(root)
e2.grid(row=1,column=2,padx=10,pady=10)


