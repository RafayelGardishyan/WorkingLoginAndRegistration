__author__ = "Rafayel Gardishyan"

import time
import re
from tkinter import *
from pathlib import Path
import emailsender

def registration():
    registration_form = Tk()
    x = 5

    class Form:

        def submit(self, event):
            global email
            global name
            global surname
            global password
            email = self.entry.get()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.label3["text"] = "Not valid email address!"
            else:
                name = self.entry1.get()
                surname = self.entry2.get()
                password = self.entry4.get()
                with open("data/" + email, "w+") as out_registration:
                    char = "1"
                    for i in range(len(char)):
                        out_string = str(surname + " " + name + "\n" + email + "\n" + password)
                        out_registration.write(out_string)
                emailsender.send_email(email, name, surname, password)

        def __init__(self, main):
            self.label = Label(main, text="E-mail", font="15", bd=x)
            self.entry = Entry(main, width="30", bd=x, font="15", )
            self.label1 = Label(main, text="First Name", font="15", bd=x, )
            self.entry1 = Entry(main, width="30", bd=x, font="15", )
            self.label2 = Label(main, text="Last Name", font="15", bd=x)
            self.entry2 = Entry(main, width="30", bd=x, font="15", )
            self.label4 = Label(main, text="Password", font="15", bd=x)
            self.entry4 = Entry(main, width="30", bd=x, font="15", )
            self.btn = Button(main, fg="blue", width="20", font="15", height="1", text="Submit", bd=x)
            self.label3 = Label(main, text=" ", fg='red', font="15", bd=x)

            self.entry4.config(show="*")

            self.label.grid(row=0, column=0)
            self.entry.grid(row=0, column=1)
            self.label1.grid(row=1, column=0)
            self.entry1.grid(row=1, column=1)
            self.label2.grid(row=2, column=0)
            self.entry2.grid(row=2, column=1)
            self.label4.grid(row=3, column=0)
            self.entry4.grid(row=3, column=1)
            self.btn.grid(row=5, column=1)
            self.label3.grid(row=6, column=1)

            self.btn.bind("<Button-1>", self.submit)

    registration_form.title("Register your account")
    obj = Form(registration_form)

    registration_form.mainloop()


def login():
    login__form = Tk()
    x = 5

    class Form:

        def loginlogin(self, event):

            loginInp = self.entry.get()
            passInp = self.entry4.get()
            check1 = Path("data/" + loginInp)
            if check1.is_file():
                if passInp in open('data/' + loginInp).read():
                    self.label3["text"] = "Successfully logged in"
                    self.label3["fg"] = "blue"
                else:
                    self.label3["text"] = "Error. Check your details."
            else:
                self.label3["text"] = "Error. Check your details."

        def __init__(self, main):
            self.label = Label(main, text="E-mail", font="15", bd=x)
            self.entry = Entry(main, width="30", bd=x, font="15", )
            self.label4 = Label(main, text="Password", font="15", bd=x)
            self.entry4 = Entry(main, width="30", bd=x, font="15", )
            self.btn = Button(main, fg="blue", width="20", height="1", text="Submit", font="15", bd=x)
            self.label3 = Label(main, text=" ", fg='red', font="15", bd=x)

            self.entry4.config(show="*")

            self.label.grid(row=0, column=0)
            self.entry.grid(row=0, column=1)
            self.label4.grid(row=1, column=0)
            self.entry4.grid(row=1, column=1)
            self.btn.grid(row=2, column=1)
            self.label3.grid(row=3, column=1)

            self.btn.bind('<Button-1>', self.loginlogin)

    login__form.title("Login")
    obj = Form(login__form)