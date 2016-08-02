from tkinter import *
from tkinter import messagebox

                         
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.startScreen()

    def startScreen(self):
        startscreen = PhotoImage(file = "start.gif")

        self.outputBox = Text(self.parent, bg='white', height= 10, fg='green', relief=FLAT, yscrollcommand='TRUE')
        self.outputBox.pack(fill='both', expand=True)

        
        welcome = Label(self.outputBox, image = startscreen, borderwidth = 0)
        welcome.image = startscreen
        welcome.pack(side="left")

        title = Label(self.outputBox,
                      text = "Welcome to SOHO Hockey!",
                      bg = "white",
                      fg = "red",
                      wraplength = 240,
                      font = "Helvetica 40 bold",
                      pady=50,      
                      justify= RIGHT).pack()
        
        self.button1 = Button(self.parent,
                              text='start game',
                              width=20, bg='white',
                              fg='red',
                              activebackground='red',
                              activeforeground='white',
                              command = start)
        self.button1.pack(side=RIGHT, padx=15, pady=10)
        
        self.button2 = Button(self.parent,
                              text='shut down',
                              width=20,
                              bg='white',
                              fg='red',
                              activebackground='red',
                              activeforeground='white',
                              command = shut)
        self.button2.pack(side=LEFT, padx=15, pady=10)

def main():
    root = Tk()
    app = Application(root)
    app.parent.geometry('800x480+100+100')
    app.parent.configure(background = 'black')
    app.mainloop()

def shut():
    print ("shutdown")
    

def start():
    print ("start")
    

main()
