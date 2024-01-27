import os
from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("400x400")
l1=Label(text="Username")
l1.place(relx=0.05,rely=0.5)
l2=Label(text="Password")
l2.place(relx=0.05,rely=0.6)

e1=Entry()
e1.place(relx=0.2,rely=0.5)
e2=Entry()
e2.place(relx=0.2,rely=0.6)

def log():
    username=e1.get()
    password=e2.get()
    
    if os.path.exists('alignreg.txt'):
        print(":")
        with open('alignreg.txt')as file:
           
            lines=file.readlines()
            for x in lines:
                h=x.split()
                print(h)
                username1=h[0]
                password1=h[1]
                
            if(username1==username and password1==password):
                messagebox.showinfo("Welcome","Login successfully")
                return
            else:
                messagebox.showwarning("Invalid","Incorrect Username or Password")

b1=Button(win,text="GO",command=log)
b1.place(relx=0.3,rely=0.7)
win.mainloop()