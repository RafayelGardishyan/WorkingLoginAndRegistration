import regdef
from tkinter import *
import aboutwindow

def aboutbox():
    aboutwindow.open()




class mainwindow:

    def __init__(self):


        self.lab = Label(main_window, text="Welcome! To continue register or login!", font="15", bd="5")
        self.btn = Button(main_window, fg="blue", width="20", height="1", text="Login", font="15", bd="5")
        self.btn2 = Button(main_window, fg="blue", width="20", height="1", text="Register", font="15", bd="5")
        self.btn3 = Button(main_window, fg="blue", width="2", height="1", text="X", font="15", bd="5")

        self.lab.grid(row=0, columnspan=2, padx=10)
        self.btn.grid(row=1, column=0, pady=5, padx=2)
        self.btn2.grid(row=1, column=1, pady=5, padx=2)
        self.btn3.grid(row=1, column=2, pady=5, padx=2)

        self.btn.bind("<Button-1>", self.login_opener)
        self.btn2.bind("<Button-1>", self.registration_opener)
        self.btn3.bind("<Button-1>", self.quits)

    def login_opener(self, event):
        regdef.login()

    def registration_opener(self, event):
        regdef.registration()

    def quits(self, event):
        quit()


main_window = Tk()

menubar = Menu(main_window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=aboutbox, font="15")
filemenu.add_command(label="Exit", command=main_window.quit, font="15")
menubar.add_cascade(label="Options", menu=filemenu, font="15")

main_window.config(menu=menubar)
main_window.title("Welcome!")
window = mainwindow()
main_window.iconbitmap("images/smile.ico")
main_window.mainloop()
