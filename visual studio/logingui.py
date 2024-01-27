from tkinter import *
from tkinter import messagebox
import os
root=Tk()

l1=Label(root,text="username")
l1.grid(row=0,column=1)
l2=Label(root,text="password")
l2.grid(row=1,column=1)

e1=Entry(root)
e1.grid(row=0,column=2,padx=10,pady=10)
e2=Entry(root)
e2.grid(row=1,column=2,padx=10,pady=10)



def show(root,data):
    print(data)
    root.destroy()
    root=Tk()
    a="Name : "+data[0]
    label=Label(root,text=a)
    label.pack()
    a="Father's Name : "+data[1]
    label=Label(root,text=a)
    label.pack()
    a="Age : "+data[2]
    label=Label(root,text=a)
    label.pack()

    b=""
    if(data[3]=="1"):
        b="Male"
    elif(data[3]=="2"):
        b="Female"
    elif(data[3]=="3"):
        b="Transgender"
    a="Gender : "+b
    label=Label(root,text=a)
    label.pack()
    
    b=""
    if(data[4]=="1"):
        b="Yes"
    elif(data[4]=="2"):
        b="No"
    a="Physically Challenged Person: "+b
    label=Label(root,text=a)
    label.pack()
    
    b=""
    if(data[5]=="1"):
        b="Yes"
    elif(data[5]=="2"):
        b="No"
    a="Sports Quota : "+b
    label=Label(root,text=a)
    label.pack()
    

    a="Address: "+data[6]
    label=Label(root,text=a)
    label.pack()
    root.mainloop()





def login():
    username=e1.get()
    password=e2.get()
    if os.path.exists('subha.txt'):
        with open ('subha.txt','r') as file:
            lines=file.readlines()
            for x in lines:
                y=x.split()
                username1=x.split()
                password1=x.split()
                print(username1,password1)
            if(username==username and password==password):
                messagebox.showinfo('login','successfully login')
                show(root,y)
            else:
                messagebox.showinfo('invalid','incorrect username or password')



b=Button(root,text="Login",command=login)
b.grid(row=5,column=2)

root.mainloop()