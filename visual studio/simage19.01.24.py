from tkinter import *
from PIL import ImageTk,Image
from PIL.ImageTk import PhotoImage
win=Tk()
win.geometry("400x400")
frame=Frame(win,width=400,height=400)
frame.pack()
frame.place(relx=0.001,rely=0.001)
img=PhotoImage(Image.open("panda.jpg"))
label=Label(frame,image=img)
label.pack()
frame1=Frame(win,width=400,height=400)
frame1.pack()
frame1.place(relx=0.75,rely=0.75)
img1=PhotoImage(Image.open("kitkat.jpg"))
label1=Label(frame1,image=img1)
label1.pack()
win.mainloop()