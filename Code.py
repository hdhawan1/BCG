from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
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

root.maxsize(260,600)
root.mainloop()