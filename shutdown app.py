"""
Author Name: SM Atiqur Rahman Limon
Date: 10/04/2025
Mobile: +880132358921
E-mail: scienceandtechnologylab24@gmail.com
"""
from tkinter import*
import os

root=Tk()
root.title("Shutdown App")
root.geometry("400x580")

############################End function #######################################
def restarttime():
    os.system("shutdown /r /t 30")

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown -1")
################################ End function ######################################
#Restart with time button
restart_time_button=PhotoImage(file="restart time.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2",command=restarttime)
first_button.place(x=10,y=10)

#close button
close_button=PhotoImage(file="close.png")
second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2",command=root.destroy)
second_button.place(x=200,y=10)

#Restart button
restart_button=PhotoImage(file="restart.png")
third_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2",command=restart)
third_button.place(x=10,y=200)

#Shutdown button
shutdown_button=PhotoImage(file="shutdown.png")
fourth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2",command=shutdown)
fourth_button.place(x=200,y=200)

#log out button
logout_button=PhotoImage(file="log out.png")
fifth_button=Button(root,image=logout_button,borderwidth=0,cursor="hand2",command=logout)
fifth_button.place(x=10,y=400)

root.mainloop()