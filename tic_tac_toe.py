from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == players[0]:
            
            buttons[row][column]['text'] = player
        
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + "'s turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        else:
            if player == players[1]:
                buttons[row][column]['text'] = player
            
                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0] + "'s turn"))
                elif check_winner() is True:
                    label.config(text=(players[1] + " wins"))
                elif check_winner() == "Tie":
                    label.config(text=("Tie!"))
        

def check_winner():
    
    # Horizontal checks
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for n in range(3):
                buttons[row][n].config(bg="green")
            return True
    
    # Vertical checks
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            for n in range(3):
                buttons[n][column].config(bg="green")
            return True
    
    # Diagonal checks
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        for n in range(3):
            buttons[n][n].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        for n, m in zip(range(3), reversed(range(3))):
            buttons[n][m].config(bg="green")
            return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else: return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    
    player = random.choice(players)
    label.config(text=player + "'s turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X","O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text= player + "'s turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text="",font=('consolas',40),width=5,height=2,
                                      command=lambda row=row,column=column:next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
