import regdef
from tkinter import *


class mainwindow:
    def __init__(self):
        self.lab = Label(main_window, text="Welcome! To continue register or login!", font="15", bd="5")
        self.btn = Button(main_window, fg="blue", width="20", height="1", text="Login", font="15", bd="5")
        self.btn2 = Button(main_window, fg="blue", width="20", height="1", text="Register", font="15", bd="5")

        self.lab.grid(row=0, columnspan=2)
        self.btn.grid(row=1, column=0)
        self.btn2.grid(row=1, column=1)

        self.btn.bind("<Button-1>", self.login_opener)
        self.btn2.bind("<Button-1>", self.registration_opener)

    def login_opener(self, event):
        regdef.login()

    def registration_opener(self, event):
        regdef.registration()


main_window = Tk()
main_window.title("Welcome!")
window = mainwindow()
main_window.iconbitmap("images/smile.ico")
main_window.mainloop()
