import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic-Tac-Toe Game")

player = "X"
buttons = []

def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  
        (0,3,6),(1,4,7),(2,5,8),  
        (0,4,8),(2,4,6)           
    ]

    for a,b,c in wins:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            return buttons[a]["text"]
    return None


def reset_game():
    global player
    player = "X"
    for b in buttons:
        b["text"] = ""


def click(i):
    global player

    if buttons[i]["text"] == "":
        buttons[i]["text"] = player

        winner = check_winner()

        if winner:
            messagebox.showinfo("Winner", winner + " wins!")
            reset_game()
            return

        if player == "X":
            player = "O"
        else:
            player = "X"


for i in range(9):
    button = tk.Button( window, text="", width=10, height=5,
                       command=lambda i=i: click(i),font=("arial",20,"bold"))

    button.grid(row=i//3, column=i%3)
    buttons.append(button)
 


window.mainloop()