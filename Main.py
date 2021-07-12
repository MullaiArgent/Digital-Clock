from tkinter import *
from time import strftime

a = Tk()
a.title("My Clock")

b = Label(a)
b.pack(anchor='center')


def time():
    c = strftime('%H:%M:%S')
    b.config(text=c, font=('DS-DIGITAL', 30), background="black", foreground="cyan")
    b.after(1000, time)


time()

mainloop()