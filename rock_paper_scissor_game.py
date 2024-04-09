from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Game Rock Paper and Scissor")
root.configure(bg="#AC7D88")
root.resizable(False,False)
root.geometry("1300x400")

def msg_update(a):
    final_message['text'] = a
    
def computer_update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)
    
def player_update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)
    
def winner_check(p,c):
    if p == c:
        msg_update("IT's a tie")
    elif p == "rock":
        if c == "paper":
            msg_update("Computer Wins !!")
            computer_update()
        else:
            msg_update("Player Wins !!")
            player_update()
            
    elif p == "paper":
        if c == "scissor":
            msg_update("Computer Wins !!")
            computer_update()
        else:
            msg_update("Player Wins !!")
            player_update()
            
    elif p == "scissor":
        if c == "rock":
            msg_update("Computer Wins !!")
            computer_update()
        else:
            msg_update("Player Wins !!")
            player_update()
    else:
        pass
    
to_select = ["rock","paper","scissor"]

def choice_update(a):
    
    choice_computer = to_select[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image=img_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=img_paper2)
    else:
        label_computer.configure(image=img_scissor2) 
        
    if a == "rock":
        label_player.configure(image=img_rock1)
    elif a == "paper":
        label_player.configure(image=img_paper1)
    else:
        label_player.configure(image=img_scissor1) 
        
    winner_check(a,choice_computer)
        
           
#images
img_rock1 = PhotoImage(file="images/rock.png")
root.iconphoto(False,img_rock1)
img_paper1 = PhotoImage(file="images/paper.png")
root.iconphoto(False,img_paper1)
img_scissor1 = PhotoImage(file="images/scissor.png")
root.iconphoto(False,img_scissor1)
img_rock2 = PhotoImage(file="images/rock1.png")
root.iconphoto(False,img_rock2)
img_paper2 = PhotoImage(file="images/paper1.png")
root.iconphoto(False,img_paper2)
img_scissor2 = PhotoImage(file="images/scissor1.png")
root.iconphoto(False,img_scissor2)

#gameplayers
label_player = Label(root,image=img_scissor1)
label_player.grid(row=1,column=4)
label_computer = Label(root,image=img_scissor2)
label_computer.grid(row=1,column=0)

#scoreboard
computer_score = Label(root,text=0,font=("Arial",60,"bold"),fg="black")
computer_score.grid(row=1,column=1)
player_score = Label(root,text=0,font=("Arial",60,"bold"),fg="black")
player_score.grid(row=1,column=3)

#players
player_indicator = Label(root,font=("Arial",40,"bold"),text="PLAYER",bg="#9ADE7B",fg="black")
player_indicator.grid(row=0,column=3)
computer_indicator = Label(root,font=("Arial",40,"bold"),text="COMPUTER",bg="#9ADE7B",fg="black") 
computer_indicator.grid(row=0,column=1)

final_message = Label(root,font=("Arial",40,"bold"),bg="#A0153E",fg="white")
final_message.grid(row=3,column=2)

#buttons
button_rock = Button(root,width=16,height=3,text="ROCK",font=("Arial",20,"bold"),bg="#F9F07A",fg="black",command=lambda:choice_update("rock"))
button_rock.grid(row=2,column=1)

button_paper = Button(root,width=16,height=3,text="PAPER",font=("Arial",20,"bold"),bg="#F9F07A",fg="black",command=lambda:choice_update("paper"))
button_paper.grid(row=2,column=2)

button_scissor = Button(root,width=16,height=3,text="SCISSOR",font=("Arial",20,"bold"),bg="#F9F07A",fg="black",command=lambda:choice_update("scissor"))
button_scissor.grid(row=2,column=3)


root.mainloop()
