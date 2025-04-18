"""
Author Name: SM Atiqur RAhman Limon
Date: 10/04/2025
Mobile: +8801321358921
E-mail: scienceandtechnologylab24@gmail.com
"""
import tkinter as tk
from tkinter import*
import pyttsx3

root=Tk()
root.title("Text to speech")
root.geometry("400x200")
root.resizable(False,False)

engin=pyttsx3.init()
def speak():
    engin.say(textv.get())
    engin.runAndWait()
    engin.stop()

obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=20,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

textv=StringVar()
text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="speak",font=20,bg="black",fg="white",command=speak)
btn.pack(side=tk.LEFT,padx=5)

root.mainloop()