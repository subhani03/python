from tkinter import *
from guimod import *
r=Tk()
r.geometry("400x400")
l1=Label(r,text="enter the first value")
l1.grid(row=0,column=1)
l2=Label(r,text="enter the second value")
l2.grid(row=1,column=1)
l3=Label(r,text="Answer")
l3.grid(row=2,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)

b=Button(r,text="Add",activebackground="blue",command=lambda:e3.insert(0,add(int(e1.get()),int(e2.get()),e3.delete(0,END))))
b.grid(row=0,column=3)
b=Button(r,text="Sub",activebackground="red",command=lambda:e3.insert(0,sub(int(e1.get()),int(e2.get()),e3.delete(0,END))))
b.grid(row=1,column=3)
b=Button(r,text="Mul",activebackground="purple",command=lambda:e3.insert(0,mul(int(e1.get()),int(e2.get()),e3.delete(0,END))))
b.grid(row=2,column=3)
b=Button(r,text="Div",activebackground="sky blue",command=lambda:e3.insert(0,div(int(e1.get()),int(e2.get()),e3.delete(0,END))))
b.grid(row=3,column=3)
r.mainloop()