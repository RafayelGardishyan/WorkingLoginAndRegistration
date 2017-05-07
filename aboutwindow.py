from tkinter import *
def open():
    aboutwindow = Tk()
    x = 5
    text = "This is a simple Registration and login program that works local\nIt is made by Rafayel Gardishyan."
    class abbox:


        def __init__(self, main):
            self.label = Label(main, text=text, font="15", bd=x)
            self.label.grid(row=0, columnspan=2)


    aboutwindow.title("About")
    aboutwindow.iconbitmap("images/smile.ico")
    obj = abbox(aboutwindow)