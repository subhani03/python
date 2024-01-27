'''
import tkinter
top=tkinter.Tk()
top.mainloop()

from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
root.mainloop()

from tkinter import *
root=Tk()
frame=Frame(root,width=500,height=500,bg="blue")
frame.pack()
root.mainloop()

import tkinter
from tkinter import messagebox

def helloCallBack():
   tkinter.messagebox.showinfo( "welcome", "login")

top = tkinter.Tk()
B = tkinter.Button(top,text="hello",command=helloCallBack)
B.pack()
top.mainloop()

import tkinter
t=tkinter.Tk()
frame=tkinter.Frame(t,bg='skyblue',width=500,height=500)
B=tkinter.Button(t,text='hello',activebackground='green')
B.pack()
frame.pack()
t.mainloop()

import tkinter
t=tkinter.Tk()
f1=tkinter.Frame(t)
f2=tkinter.Frame(t)
l=tkinter.Label(f1,text='hello')
l.pack()
b=tkinter.Button(f2,text='livewire')
b.pack()
f1.pack(padx=5,pady=10)
f2.pack(padx=10,pady=50)
t.mainloop()

from tkinter import *
root=Tk()
for x in['orange','white','green']:
    Frame(height=20,width=300,bg=x).pack()
root.mainloop()
'''
from tkinter import *
r=Tk()
r.geometry("400x400")

l1=Label(r,text="Enter the First Value")
l1.grid(row=0,column=1)
l2=Label(r,text="Enter the Second Value")
l2.grid(row=1,column=1)
l3=Label(r,text="Result")
l3.grid(row=2,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    print(a,b,c)
    e3.delete(0,END)
    e3.insert(0,c)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    print(a,b,c)
    e3.delete(0,END)
    e3.insert(0,c)
def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    print(a,b,c)
    e3.delete(0,END)
    e3.insert(0,c)
def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    print(a,b,c)
    e3.delete(0,END)
    e3.insert(0,c)

b=Button(r,text="Add",command=lambda:e3.insert(0,add(int(e1.get()),int(e2.get()))))
b.grid(row=0,column=3)
b=Button(r,text="subtraction",command=lambda:sub())
b.grid(row=1,column=3)
b=Button(r,text="multiplication",command=lambda:mul())
b.grid(row=2,column=3)
b=Button(r,text="division",command=lambda:div())
b.grid(row=3,column=3)
r.mainloop()


