from tkinter import *
from tkinter import messagebox

def try_login():               # this my login function
    if username.get()==default_name and password.get() == default_password:
       log.destroy()

    else:
       messagebox.showwarning("Login failed","Please try again")

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

redbutton = Button(bottomframe, text="Info", bg = "black", fg="white", relief = GROOVE, height = 3, width = 11)
redbutton.pack(side = LEFT)

greenbutton = Button(bottomframe, text="Calendar", bg = "black", fg="white",relief=GROOVE, height = 3, width = 11)
greenbutton.pack(side = LEFT)

homebutton = Button(bottomframe, text="Account", bg = "black", fg="white",relief=GROOVE, height = 3, width = 11)
homebutton.pack(side = LEFT)
windowtitle = Label(mainwindow, bg = "black", fg = "white", text = "Ryan's Account",width= 100, height = 2)
windowtitle.pack(side = TOP)

space1 = LabelFrame(mainwindow, height = 20,width = 260, bg = "gray")
space1.pack(side=TOP)

subtitle1 = Label(mainwindow, text = "Information",width= 100,anchor = 'w')
subtitle1.pack(side=TOP)

midspace = Frame(mainwindow)
midspace.pack(side=TOP)

basics1= Label(mainwindow, text = " Name and Address",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
basics1.pack(side=TOP)
basics2= Label(mainwindow, text = " Credit Card Information",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
basics2.pack(side=TOP)
basics3= Label(mainwindow, text = " Family Information",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
basics3.pack(side=TOP)
basics4= Label(mainwindow, text = " Income Information",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
basics4.pack(side=TOP)

subtitle2 = Label(mainwindow, text = "Other Settings",width= 100,anchor = 'w')
subtitle2.pack(side=TOP)

pref1= Label(mainwindow, text = " Eating Restrictions",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
pref1.pack(side=TOP)
pref2= Label(mainwindow, text = " Enable/Disable",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
pref2.pack(side=TOP)
pref3= Label(mainwindow, text = " Feedback",width= 200,bd = 5, bg = "dark grey",anchor = 'w')
pref3.pack(side=TOP)

mainwindow.mainloop()

