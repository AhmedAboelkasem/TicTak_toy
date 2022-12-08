from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
root = Tk()
root.title("X_O : player 1")
# global variables
active = 1
p1 = []    # list for player 1
p2 = []    # list for player 2
style = ttk.Style()
style.theme_use('classic')

bu1 = ttk.Button(root, text=" ")
bu1.grid(row=0, column=0, sticky="snew", ipadx=40, ipady=40)
bu1.config(command=lambda: Buttonclick(1))

bu2 = ttk.Button(root, text=" ")
bu2.grid(row=0, column=1, sticky="snew", ipadx=40, ipady=40)
bu2.config(command=lambda: Buttonclick(2))

bu3 = ttk.Button(root, text=" ")
bu3.grid(row=0, column=2, sticky="snew", ipadx=40, ipady=40)
bu3.config(command=lambda: Buttonclick(3))

bu4 = ttk.Button(root, text=" ")
bu4.grid(row=1, column=0, sticky="snew", ipadx=40, ipady=40)
bu4.config(command=lambda: Buttonclick(4))

bu5 = ttk.Button(root, text=" ")
bu5.grid(row=1, column=1, sticky="snew", ipadx=40, ipady=40)
bu5.config(command=lambda: Buttonclick(5))

bu6 = ttk.Button(root, text=" ")
bu6.grid(row=1, column=2, sticky="snew", ipadx=40, ipady=40)
bu6.config(command=lambda: Buttonclick(6))

bu7 = ttk.Button(root, text=" ")
bu7.grid(row=2, column=0, sticky="snew", ipadx=40, ipady=40)
bu7.config(command=lambda: Buttonclick(7))

bu8 = ttk.Button(root, text=" ")
bu8.grid(row=2, column=1, sticky="snew", ipadx=40, ipady=40)
bu8.config(command=lambda: Buttonclick(8))

bu9 = ttk.Button(root, text=" ")
bu9.grid(row=2, column=2, sticky="snew", ipadx=40, ipady=40)
bu9.config(command=lambda: Buttonclick(9))


def Buttonclick(id):
    global active
    global p1
    global p2
    if active == 1:
        putSympol(id, "X")
        p1.append(id)
        root.title("X_O : player 2")
        active = 2
        print("P1:{}".format(p1))
        AutoPlay()

    elif active == 2:
        putSympol(id, "O")
        p2.append(id)
        root.title("X_O : player 1")
        active = 1
        print("P2:{}".format(p2))
    check()


def putSympol(id, s):
    if id == 1:
        bu1.config(text=s)
        bu1.state(['disabled'])
    elif id == 2:
        bu2.config(text=s)
        bu2.state(['disabled'])
    elif id == 3:
        bu3.config(text=s)
        bu3.state(['disabled'])
    elif id == 4:
        bu4.config(text=s)
        bu4.state(['disabled'])
    elif id == 5:
        bu5.config(text=s)
        bu5.state(['disabled'])
    elif id == 6:
        bu6.config(text=s)
        bu6.state(['disabled'])
    elif id == 7:
        bu7.config(text=s)
        bu7.state(['disabled'])
    elif id == 8:
        bu8.config(text=s)
        bu8.state(['disabled'])
    elif id == 9:
        bu9.config(text=s)
        bu9.state(['disabled'])


def check():
    winer = -1
    if(1 in p1) and (2 in p1) and (3 in p1):
        winer=1
    if (1 in p2) and (2 in p2) and (3 in p2):
        winer = 2
    if(4 in p1) and (5 in p1) and (6 in p1):
        winer=1
    if (4 in p2) and (5 in p2) and (6 in p2):
        winer = 2
    if(7 in p1) and (8 in p1) and (9 in p1):
        winer=1
    if (7 in p2) and (8 in p2) and (9 in p2):
        winer = 2
    if(1 in p1) and (4 in p1) and (7 in p1):
        winer=1
    if (1 in p2) and (4 in p2) and (7 in p2):
        winer = 2
    if(2 in p1) and (5 in p1) and (8 in p1):
        winer=1
    if (2 in p2) and (5 in p2) and (8 in p2):
        winer = 2
    if (3 in p1) and (6 in p1) and (9 in p1):
            winer = 1
    if (3 in p2) and (6 in p2) and (9 in p2):
            winer = 2
    if(1 in p1) and (5 in p1) and (9 in p1):
        winer=1
    if (1 in p2) and (5 in p2) and (9 in p2):
        winer = 2
    if(3 in p1) and (5 in p1) and (7 in p1):
        winer=1
    if (3 in p2) and (5 in p2) and (7 in p2):
        winer = 2

    if winer == 1:
        messagebox.showinfo(title="Congrat.", message="Player 1 is the winer")
    elif winer == 2:
        messagebox.showinfo(title="Congrat.", message="Player 2 is the winer")


def AutoPlay():
    global p1
    global p2
    EmptyCells = []
    for cell in range(9):
        if (not( ( cell+1 in p1) or (cell+1 in p2))):
            EmptyCells.append(cell+1)

    RandIndex=randint(0, len(EmptyCells)-1)
    Buttonclick(EmptyCells[RandIndex])


root.mainloop()