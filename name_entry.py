from tkinter import *

def show_entry_fields():
   print("pass these variables to hockey.py")
   print("player 1: %s\nplayer2: %s" % (p1.get(), p2.get()))
   p1.delete(0,END)
   p2.delete(0,END)

def begin():
   print("link to main hockey")

def back():
   print("link back to start screen")

master = Tk()
master.geometry("800x480")
master.title("SOHO TABLE HOCKEY")
master.config(bg= "black")

Label(master, text="To Begin Enter Players Names and tap BEGIN",
      fg="red", bg="black", font = "Helvetica 30 bold").grid(row=0, column=1, padx=10, pady=40, columnspan=3)

Label(master, text="Enter Player1 Name",
      fg="white", bg="black",
      font = "Helvetica 20 bold").grid(row=3, column=1, pady=4)

Label(master, text="Enter Player2 Name",
      fg="white", bg="black",
      font = "Helvetica 20 bold").grid(row=4, column=1, pady=4, padx=10)

p1 = Entry(master)
p2 = Entry(master)
p1.insert(10,"Player1")
p2.insert(10,"Player2")

p1.grid(row=3, column=3)
p2.grid(row=4, column=3)

Button(master, text='BACK', command=back).grid(row=6, column=3, sticky=W, pady=50, padx=4)
Button(master, text='BEGIN', command=show_entry_fields).grid(row=6, column=4, sticky=W, pady=50, padx=4)

mainloop( )
