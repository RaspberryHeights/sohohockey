from tkinter import *
import tkinter as Tk
 
########################################################################
class OtherFrame(Tk.Toplevel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("800x480")
        self.title("otherFrame")
        self.config(bg="black")
        
 
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()
 
    #----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()
 
########################################################################
class MyApp(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()

        self.root.config(bg = "white")
        startscreen = PhotoImage(file = "start.gif")
        welcome = Label(self.root, image = startscreen, borderwidth = 0)
        welcome.image = startscreen
        welcome.pack(side="left")
        
        
        title = Label(self.root,
              text = "Welcome to SOHO Hockey!",
              bg = "white",
              fg = "red",
              wraplength = 240,
              font = "Helvetica 40 bold",
              pady=50,      
              justify= RIGHT).pack()

        startMenu = Label(self.frame,
                          bg="black",
                          width=800,
                          ).pack(side ="bottom")



        btn = Tk.Button(self.frame,
                              text='start game',
                              width=20, bg='white',
                              fg='red',
                              activebackground='red',
                              activeforeground='white',
                              command=self.openFrame)
        btn.pack(side=RIGHT, padx=15, pady=10)
        
        btn2 = Tk.Button(self.frame,
                              text='shut down',
                              width=20,
                              bg='white',
                              fg='red',
                              activebackground='red',
                              activeforeground='white',
                              command=self.openFrame)
        btn2.pack(side=LEFT, padx=15, pady=10)


 
        btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()
 
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
 
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        subFrame = OtherFrame(self)
 
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x480")
    app = MyApp(root)
    root.mainloop()
