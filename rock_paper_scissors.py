#-------------------------Importing necessary modules----------------------------------

# CustomTKinter: A module used to create customized GUI elements in Python.
from customtkinter import *

# CTkMessagebox: A module providing custom message box functionality for GUI
from CTkMessagebox import CTkMessagebox

# Random: A standard library module for generating random numbers and making random selections.
import random

# PIL: PIL stands for Python Image Library is a powerful library for image processing in Python.
# Used to work with images, load them, and manipulate them.
from PIL import Image

# Time: A standard library module for working with time-related functions.
from time import strftime

# pygame: A popular library module used for multimedia applications especially in game development
# used to load and play soundeffect when any button is clicked
from pygame import mixer
mixer.init()

# Creating the main application window
App=CTk()
App.geometry("900x550+270+100")
App._set_appearance_mode("Light")
App.iconbitmap("Images/app_icon.ico")
App.title("ROCK PAPER SCISSORS GAME BY DC")
App.resizable(False,False)

#----------------------All Functions---------------------------------
compScore=0
userScore=0

# Function to update the computer's score
def compUpdateScore():
    global compScore
    compScore+=1
    comp_var.set(f"COMPUTER\n SCORE: {compScore}")

# Function to update the user's score
def userUpdateScore():
    global userScore
    userScore+=1
    user_var.set(f"USER\nSCORE: {userScore}")

# Function for the "Rock" button
def rock(a):
    global compScore
    comp_choice=random.choice(['rock','paper','scissor'])
    update_image(a,comp_choice)
    if comp_choice==a:
        show_lbl.configure(text="OOPS! Its a Tie")
        mixer.music.load("sounds/tie.mp3")
        mixer.music.play()
    elif comp_choice=="paper":
        show_lbl.configure(text="YOU LOOSE! Computer Paper Wraps Rock")
        mixer.music.load("sounds/comp_sound.mp3")
        mixer.music.play()
        compUpdateScore()
    elif comp_choice=="scissor":
        show_lbl.configure(text="YOU WIN! Rock Crushes Scissors")
        mixer.music.load("sounds/user_sound.wav")
        mixer.music.play()
        userUpdateScore()

# Function for the "paper" button
def paper(b):
    global compScore
    comp_choice=random.choice(['rock','paper','scissor'])
    update_image(b,comp_choice)
    if comp_choice==b:
        show_lbl.configure(text="OOPS! Its a Tie")
        mixer.music.load("sounds/tie.mp3")
        mixer.music.play()
    elif comp_choice=="scissor":
        show_lbl.configure(text="YOU LOOSE! Computer Scissors Cuts Paper")
        mixer.music.load("sounds/comp_sound.mp3")
        mixer.music.play()
        compUpdateScore()
    elif comp_choice=="rock":
        show_lbl.configure(text="YOU WIN! Paper Wraps Rock")
        mixer.music.load("sounds/user_sound.wav")
        mixer.music.play()
        userUpdateScore()

# Function for the "scissor" button
def scissor(c):
    comp_choice=random.choice(['rock','paper','scissor'])
    update_image(c,comp_choice)
    if comp_choice==c:
        show_lbl.configure(text="OOPS! Its a Tie")
        mixer.music.load("sounds/tie.mp3")
        mixer.music.play()
    elif comp_choice=="rock":
        show_lbl.configure(text="YOU LOOSE! Computer Rock Crushes Scissor")
        mixer.music.load("sounds/comp_sound.mp3")
        mixer.music.play()
        compUpdateScore()
    elif comp_choice=="paper":
        show_lbl.configure(text="YOU WIN! Scissor Cuts Paper")
        mixer.music.load("sounds/user_sound.wav")
        mixer.music.play()
        userUpdateScore()


# Function to update the images of user's and computer's choices
def update_image(x,comp):
    # ------ For User ------
    if x=="rock":
        user_image_label.configure(image=rock_image)
        user_1.configure(text="Rock")
    elif x=="paper":
        user_image_label.configure(image=paper_image)
        user_1.configure(text="Paper")
    elif x=="scissor":
        user_image_label.configure(image=scissors_image)
        user_1.configure(text="Scissors")

    # ----- For Computer ----
    if  comp == "rock":
        compu_image_label.configure(image=comp_rock_image)
        computer_1.configure(text="Rock")
    elif comp == "paper":
        compu_image_label.configure(image=comp_paper_image)
        computer_1.configure(text="Paper")
    elif comp == "scissor":
        compu_image_label.configure(image=comp_scissors_image)
        computer_1.configure(text="Scissors")

# Function to activate Dark Mode
def darkMode():
    switch.configure(text="Dark Mode", button_hover_color="#F5F5F5", text_color="black", bg_color="#91a3b0")
    title_lbl.configure(bg_color="#91A3B1", text_color="black")
    time_label.configure(fg_color="#91A3B1")
    user_image_label.configure(fg_color="#242424")
    compu_image_label.configure(fg_color="#242424")
    vs_label.configure(fg_color="#242424")
    user_1.configure(fg_color="#242424", text_color="#B7CEEC")
    computer_1.configure(fg_color="#242424", text_color="#B7CEEC")
    user_indicator.configure(fg_color="#242424", text_color="#F7E7CE")
    computer_indicator.configure(fg_color="#242424", text_color="#F7E7CE")
    rock_btn.configure(bg_color="#242424")
    paper_btn.configure(bg_color="#242424")
    scissor_btn.configure(bg_color="#242424")
    reset_btn.configure(bg_color="#242424")
    quit_btn.configure(bg_color="#242424")
    show_btn.configure(bg_color="#242424")
    user_score.configure(fg_color="#EAEEE9", text_color="black")
    computer_score.configure(fg_color="#EAEEE9", text_color="black")

# Function to activate Light Mode
def lightmode():
    switch.configure(text="Light Mode", button_hover_color="#34282C", bg_color="#321414", text_color="white")
    title_lbl.configure(bg_color="#321414", text_color="#b2ffff")
    time_label.configure(fg_color="#321414")
    user_image_label.configure(fg_color="#ebebeb")
    compu_image_label.configure(fg_color="#ebebeb")
    vs_label.configure(fg_color="#ebebeb")
    user_1.configure(fg_color="#ebebeb", text_color="#2C3539")
    computer_1.configure(fg_color="#ebebeb", text_color="#2C3539")
    user_indicator.configure(fg_color="#ebebeb", text_color="navy blue")
    computer_indicator.configure(fg_color="#ebebeb", text_color="navy blue")
    rock_btn.configure(bg_color="#ebebeb")
    paper_btn.configure(bg_color="#ebebeb")
    scissor_btn.configure(bg_color="#ebebeb")
    reset_btn.configure(bg_color="#ebebeb")
    quit_btn.configure(bg_color="#ebebeb")
    show_btn.configure(bg_color="#ebebeb")
    user_score.configure(fg_color="#483c32", text_color="white")
    computer_score.configure(fg_color="#483c32", text_color="white")

#Function to switch between light and dark modes
def switchColor():
    if switch_var.get()=="off":
        mixer.music.load("sounds/toggle_sound.mp3")
        mixer.music.play()
        App._set_appearance_mode("Dark")
        darkMode()

    else:
        mixer.music.load("sounds/toggle_sound.mp3")
        mixer.music.play()
        App._set_appearance_mode("Light")
        lightmode()

#Function to reset the game
def reset():
    global userScore
    global compScore

    mixer.music.load("sounds/button.mp3")
    mixer.music.play()

    msg=CTkMessagebox(title="RESET GAME",message="Are You Sure You Want To Reset This Game At This Point ? ",
                      option_1="Yes",icon="warning",option_2="No")
    if msg.get()=="Yes":
        userScore=0
        compScore=0
        user_var.set(f"USER\nSCORE: {userScore}")
        comp_var.set(f"COMPUTER\nSCORE: {compScore}")
        show_lbl.configure(text="")
        user_image_label.configure(image=rock_image)
        compu_image_label.configure(image=rock_image)
        user_1.configure(text="Rock")
        computer_1.configure(text="Rock")
    else:
        user_var.set(f"USER\nSCORE: {userScore}")
        comp_var.set(f"COMPUTER\nSCORE: {compScore}")

#Function to show the result of the game
def showResult():
    global userScore
    global compScore

    mixer.music.load("sounds/button.mp3")
    mixer.music.play()

    if userScore>compScore:
        mixer.music.load("sounds/user_win_result.mp3")
        mixer.music.play()
        CTkMessagebox(title="RPS RESULT",message="YOU WIN ! THIS GAME",icon="Images/user_won.png")
    elif compScore>userScore:
        mixer.music.load("sounds/comp_win_result.mp3")
        mixer.music.play()
        CTkMessagebox(title="RPS RESULT",message="YOU LOOSE ! COMPUTER WIN THIS GAME",icon="Images/comp_win.png")

    else:
        mixer.music.load("sounds/tie_btwn.mp3")
        mixer.music.play()
        CTkMessagebox(title="RPS RESULT",message="ITS A TIE BETWEEN YOU AND COMPUTER",icon="Images/tie_img.png")

#Function to quit the game
def quitGame():

    mixer.music.load("sounds/button.mp3")
    mixer.music.play()
    msg=CTkMessagebox(title="QUIT GAME ?",message="Are you sure You Want to quit This Game?",icon="question",
                      option_1="Yes",option_2="No",fade_in_duration=1)
    if msg.get()=="Yes":
        msg2=CTkMessagebox(title="SUCCESSFUL", icon="Images/message_icon.png",message="Thanks For Playing This Game")
        if msg2.get()=="OK":
            App.destroy()
        else:
            App.mainloop()

#Function to display the current time
def time_func():
    time_string=strftime("%H:%M:%S %p ")
    time_label.configure(text=time_string)
    time_label.after(1000,time_func)


# ------------------- All Images -------------------------
# Load user's choice images
rock_image =CTkImage(Image.open("Images/rock.png"),size=(150,150))
paper_image=CTkImage(Image.open("Images/paper.png"),size=(150,150))
scissors_image=CTkImage(Image.open("Images/scissors.png"),size=(150,150))

# Load computer's choice images
comp_rock_image =CTkImage(Image.open("Images/rock.png"),size=(150,150))
comp_paper_image=CTkImage(Image.open("Images/paper.png"),size=(150,150))
comp_scissors_image=CTkImage(Image.open("Images/scissors.png"),size=(150,150))

# Load versus (vs) image
vs_image=CTkImage(Image.open("Images/vs_image.png"),size=(200,230))


#------------Adding Title , User and Computer Indicator ------------------

#Create and place the title label
title_lbl=CTkLabel(App,text="ROCK PAPER SCISSORS GAME",width=900,bg_color="#321414",
                   font=("Public Sans",30,"bold"),text_color="#b2ffff")
title_lbl.place(x=0,y=2)

#Create and place the title label
user_indicator=CTkLabel(App,text="User Choose:",bg_color="#ebebeb",font=("Bookman Old Style",30,"bold"),
                        text_color="navy blue")
user_indicator.place(x=30,y=50)

computer_indicator=CTkLabel(App,text="Computer Choose:",bg_color="#ebebeb",font=("Bookman Old Style",30,"bold"),
                            text_color="navy blue")
computer_indicator.place(x=600,y=50)

# ---------------- Switch or toggle Button for light and dark mode---------------
switch_var = StringVar(value="on")
switch = CTkSwitch(App ,variable=switch_var,text="Light Mode", onvalue="on", offvalue="off",hover=True,
                   button_hover_color="#fdf5e6",bg_color="#321414",corner_radius=10,progress_color="#ffbf00",
                   font=("Poppins",15,"bold"),command=switchColor)
switch.place(x=760,y=8)

#-------------- Adding Images of Rock ,Paper,Scissors , and V/s ------------------------

# Create and place labels to display user and computer choices images
user_image_label=CTkLabel(App,image=rock_image,text="",bg_color='#ebebeb')
user_image_label.place(x=50,y=90)

compu_image_label=CTkLabel(App,image=comp_rock_image,text="",bg_color='#ebebeb')
compu_image_label.place(x=670,y=90)


vs_label=CTkLabel(App,image=vs_image,text="",bg_color='#ebebeb',justify="center")
vs_label.place(x=350,y=40)

#--------------------------- All Labels --------------------------------------------

# Create and place a label to display the current time
time_label=CTkLabel(App,bg_color="#321414",font=("times",20,"bold"),text_color="white")
time_label.place(x=11,y=6)
time_func()

# Create and place labels to display user and computer choices
user_1=CTkLabel(App,text="Rock",bg_color="#ebebeb",font=("Public Sans",30,"bold"),text_color="#2C3539")
user_1.place(x=85,y=245)

computer_1=CTkLabel(App,text="Rock",bg_color="#ebebeb",font=("Public Sans",30,"bold"),text_color="#2C3539")
computer_1.place(x=705,y=245)

# Create and place labels to display User and Computer Score
user_var=StringVar()
user_var.set(f"USER\nSCORE: {userScore}")
user_score=CTkLabel(App,bg_color="#483C32",width=200,font=("Poppins",25,"bold"),
                    text_color="white",justify="left",textvariable=user_var)
user_score.place(x=-20,y=340)

comp_var=StringVar()
comp_var.set(f"COMPUTER\nSCORE: {compScore}")
computer_score=CTkLabel(App,bg_color="#483C32",width=200,font=("Poppins",25,"bold"),text_color="white",
                        justify="left",textvariable=comp_var)
computer_score.place(x=705,y=340)
show_lbl=CTkLabel(App,fg_color="white",text="",font=("Aerial",20,"bold"),text_color="black",width=460)
show_lbl.place(x=213,y=287)

# --------------------------------------All buttons ----------------------------------------------

# Create a Rock button to allow the user to choose "Rock"
rock_btn=CTkButton(App, text="Rock",bg_color='#ebebeb',hover_color='#033E3E',corner_radius=50,width=100,height=55,
                   border_width=3,border_color="#F433FF", command=lambda:rock("rock"), font=("Aerial", 25, "bold"))
rock_btn.place(x=207,y=343)

# Create a Paper button to allow the user to choose "Paper"
paper_btn=CTkButton(App, text="Paper", bg_color='#ebebeb', hover_color='#033E3E', corner_radius=50, width=100,height=55, 
                    border_width=3, border_color="#16F529", command=lambda:paper("paper"), font=("Aerial", 25, "bold"))
paper_btn.place(x=362,y=343)

# Create scissors button to allow the user to choose "Scissors"
scissor_btn=CTkButton(App, text="Scissors", bg_color='#ebebeb', hover_color='#033E3E', corner_radius=50, width=60, 
                      height=55,border_width=3,border_color="#4EE2EC", command=lambda:scissor("scissor"), 
                      font=("Aerial", 25, "bold"))
scissor_btn.place(x=521,y=343)

# Create a Reset button to reset the game.
reset_btn=CTkButton(App,text="RESET",bg_color='#ebebeb',fg_color="#123456",hover_color='#997070',corner_radius=50,
                    width=100,height=50,border_width=3,border_color="#123456",font=("Aerial",25,"bold"),command=reset)
reset_btn.place(x=60,y=470)

# Create a Show Result button to show result of the game.
show_btn=CTkButton(App,text="SHOW RESULT",fg_color="#123456",bg_color='#ebebeb',hover_color='#997070',corner_radius=50,
                   width=50,height=50,border_width=3,command=showResult,border_color="#123456",font=("Aerial",25,"bold"))
show_btn.place(x=330,y=470)

# Create a Quit button to quit the game
quit_btn=CTkButton(App,text="QUIT",bg_color='#ebebeb',fg_color="#123456",hover_color='#997070',corner_radius=50,
                   width=60,height=50,border_width=3, border_color="#123456",font=("Aerial",25,"bold"),command=quitGame)
quit_btn.place(x=700,y=470)

App.mainloop()


