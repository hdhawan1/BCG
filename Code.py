from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def try_login():               # this my login function
    if username.get()==default_name and password.get() == default_password:
       log.destroy()

    else:
       messagebox.showwarning("Login failed","Please try again")

def cancel_login():
    log.destroy()

default_name=("Ryan Li")      #DEFAULT LOGIN ENTRY
default_password=("rli123")

log=Tk()                   #this login ui
log.title("basq't")
log.geometry("260x400")
log.resizable (width=FALSE,height=FALSE)

frame = Frame(log)
frame.pack()

upperframe = LabelFrame(log, height = 125)
upperframe.pack(side = TOP)
midframe = Frame(log)
midframe.pack(side = TOP)
lowframe = LabelFrame(log, height = 180)
lowframe.pack(side = TOP)
uname = StringVar()
username = Entry(midframe, textvariable = uname)
username.pack()
pword = StringVar()
password = Entry(midframe, show = "*", textvariable = pword)
password.pack()
cont = Button(midframe, text = "Continue -->", command = lambda: try_login())
cont.pack()

log.mainloop()

mainwindow = Tk()
mainwindow.title("basq't")
mainwindow.geometry("260x400")
mainwindow.resizable (width=FALSE,height=FALSE)
bottomframe = Frame(mainwindow)
bottomframe.pack(side = BOTTOM)

redbutton = Button(bottomframe, text="Red", bg = "black", fg="white", relief = GROOVE, height = 3, width = 6)
redbutton.pack(side = LEFT)

greenbutton = Button(bottomframe, text="Brown", bg = "black", fg="white",relief=GROOVE, height = 3, width = 6)
greenbutton.pack(side = LEFT)

homebutton = Button(bottomframe, text="Home", bg = "black", fg="white",relief=GROOVE, height = 3, width = 6)
homebutton.pack(side = LEFT)

bluebutton = Button(bottomframe, text="Blue", bg = "black", fg="white",relief=GROOVE, height = 3, width = 6)
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text="Black", bg = "black", fg="white",relief=GROOVE, height = 3, width = 6)
blackbutton.pack(side = LEFT)


mainwindow.mainloop()