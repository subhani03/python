""" from tkinter import *
import tkinter
root=Tk()
checkbox1=IntVar
checkbox2=IntVar
checkbox3=IntVar
c1=Checkbutton(root,text="Music",variable=checkbox1,onvalue=1,offvalue=0,height=1,width=10)
c2=Checkbutton(root,text="video",variable=checkbox2,onvalue=1,offvalue=0,height=1,width=10)
c3=Checkbutton(root,text="Movie",variable=checkbox3,onvalue=1,offvalue=0,height=1,width=10)
c1.pack()
c2.pack()
c3.pack()


root.mainloop() """


from tkinter import *

def save_to_file():
    with open("checked_items.txt", "w") as file:
        if checkbox1.get():
            file.write("Music\n")
        if checkbox2.get():
            file.write("Video\n")
        if checkbox3.get():
            file.write("Movie\n")

root = Tk()
checkbox1 = IntVar()
checkbox2 = IntVar()
checkbox3 = IntVar()

c1 = Checkbutton(root, text="Music", variable=checkbox1, onvalue=1, offvalue=0, height=1, width=10)
c2 = Checkbutton(root, text="Video", variable=checkbox2, onvalue=1, offvalue=0, height=1, width=10)
c3 = Checkbutton(root, text="Movie", variable=checkbox3, onvalue=1, offvalue=0, height=1, width=10)

c1.pack()
c2.pack()
c3.pack()

save_button = Button(root, text="Save to File", command=save_to_file)
save_button.pack()

root.mainloop()
