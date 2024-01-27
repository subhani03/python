""" from tkinter import *
root = Tk()
text = Text(root,height=2,width=30)
text.insert(INSERT,"hello...")
text.insert(END,"kitty.....")
text.pack()

b=Button(root,text="click")
b.pack()

text.tag_add("here","1.0","1.4")
text.tag_add("start","1.8","1.10")

text.tag_config("here",background="pink",foreground="skyblue")
text.tag_config("start",background="blue",foreground="yellow")
root.mainloop() """

from tkinter import *
import tkinter

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 20 )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 20)
C1.pack()
C2.pack()
top.mainloop()