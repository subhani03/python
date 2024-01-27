from tkinter import font
from tkinter import *
import webbrowser as wb
import speech_recognition as sr
import pyttsx3
def main1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell something")
        audio=r.listen(source)
        try:
            print("Hearing..")
            text=str(r.recognize_google(audio))
            label_font=font.Font(weight="bold",family="Times New Roman",size=10)
            Label(r1,text=text,font=label_font).place(relx=0.5,rely=0.35)
        except Exception as e:
            print("error: "+str(e))

def main2():
    r=sr.Recognizer()
    url="https://www.google.co.in/search?1="
    with sr.Microphone() as source:
        print("Google Search...")
        audio=r.listen(source)
        try:
            get=r.recognize_google(audio)
            print(get)
            label_font=font.Font(weight="bold",family="Times New Roman",size=10)
            Label(r1,text=get,font=label_font).place(relx=0.5,rely=0.45)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print('failed'.format(e))
        except:
            print("Microphone not detected")

def main3():
    r=sr.Recognizer()
    url="https://www.youtube.com/results?search_querry="
    with sr.Microphone() as source:
        print("Youtube search...")
        audio=r.listen(source)
        try:
            get=r.recognize_google(audio)
            print(get)
            label_font=font.Font(weight="bold",family="Times New Roman",size=10)
            Label(r1,text=get,font=label_font).place(relx=0.5,rely=0.55)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print('failed'.format(e))
        except:
            print("Microphone not detected")

def main4():
    engine=pyttsx3.init()
    engine.setProperty('rate',200)
    engine.setProperty('volume',1.0)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(a1.get('1.0',END))
    engine.runAndWait()
    engine.stop()

r1=Tk()
r1.geometry("400x400")

lable_font=font.Font(weight="bold",family="Helvetica",size=30)
l1=Label(r1,text="speech recognition gui",font=lable_font,bg="skyblue",fg="red")
l1.place(anchor="center",relx=0.5,rely=0.1)

lable_font=font.Font(weight="bold",family="Times New Roman",size=20)
l2=Label(r1,text="google gui",font=lable_font,bg="green",fg="red")
l2.place(anchor="center",relx=0.5,rely=0.25)

lable_font=font.Font(weight="bold",family="Times New Roman",size=10)
b=Button(r1,text="speech recognition",command=lambda:main1(),font=lable_font)
b.place(relx=0.1,rely=0.35)

lable_font=font.Font(weight="bold",family="Times New Roman",size=10)
b=Button(r1,text="google search",command=lambda:main2(),font=lable_font)
b.place(relx=0.1,rely=0.45)

lable_font=font.Font(weight="bold",family="Times New Roman",size=10)
b=Button(r1,text="youtube search",command=lambda:main3(),font=lable_font)
b.place(relx=0.1,rely=0.55)

lable_font=font.Font(weight="bold",family="Times New Roman",size=10)
b1=Button(r1,text="Text to speak",command=lambda:main4(),font=lable_font)
b1.place(relx=0.8,rely=0.65)

a1=Text(r1,height=2,width=30)
a1.place(relx=0.1,rely=0.65)

r1.mainloop()