#Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
import tkinter.messagebox
from tkinter import *
import os
os.system('cls')


# выход из приложения

def exit_(event):
    root.destroy()


# начать заново
def begin(event):
    global butn
    global field
    global numButton
    for b in butn:
        b.config(bg="gold", text='')
    field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    numButton = []


# логика приложения
def logik():
    global field
    global numButton
    if len(numButton) == 9:
        tkinter.messagebox.showinfo("Конец игры", "  Ничья!!!  ")
    else:
        end = False
        if field[0] == field[1] == field[2] > 0:
            winner = field[0]
            end = True
        elif field[3] == field[4] == field[5] > 0:
            winner = field[3]
            end = True
        elif field[6] == field[7] == field[8] > 0:
            winner = field[6]
            end = True
        elif field[0] == field[3] == field[6] > 0:
            winner = field[0]
            end = True
        elif field[1] == field[4] == field[7] > 0:
            winner = field[1]
            end = True
        elif field[2] == field[5] == field[8] > 0:
            winner = field[2]
            end = True
        elif field[0] == field[4] == field[8] > 0:
            winner = field[0]
            end = True
        elif field[2] == field[4] == field[6] > 0:
            winner = field[2]
            end = True
        if end:
            if winner == 1:
                user = "O"
            elif winner == 2:
                user = "X"
            tkinter.messagebox.showinfo("Конец игры", "Выиграл " + user)
            begin(None)

# нажатие на кнопки


def click(button, num):
    global numButton
    if num not in numButton:
        global Oksana
        if Oksana == 1:
            button.config(text='O')
            button.config(bg='blue')
            field[num] = Oksana
            Oksana = 2
        else:
            button.config(text='X')
            button.config(bg='red')
            field[num] = Oksana
            Oksana = 1
        numButton.append(num)
        logik()


field = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # список значений 1 или 2
Oksana = 1  # крестик - 1, нолик - 2
numButton = []  # список нажатых кнопок


root = Tk()
root.title("Крестики-нолики")
root.geometry("233x238")
root.resizable(False, False)

ris0 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris0, 0)) 
ris0.place(x=0, y=0)
ris1 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris1, 1))
ris1.place(x=81, y=0)
ris2 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris2, 2))
ris2.place(x=162, y=0)

ris3 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris3, 3))
ris3.place(x=0, y=81)
ris4 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris4, 4))
ris4.place(x=81, y=81)
ris5 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris5, 5))
ris5.place(x=162, y=81)

ris6 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris6, 6))
ris6.place(x=0, y=162)
ris7 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris7, 7))
ris7.place(x=81, y=162)
ris8 = Button(root, width=10, height=5, bg="gold",
               command=lambda: click(ris8, 8))
ris8.place(x=162, y=162)

butn = [ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8]


root.mainloop()