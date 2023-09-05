# Import the customtkinter library for creating customized tkinter widgets.
from customtkinter import *

# Import the tkinter library for importing messagebox or message prompts.
from tkinter import messagebox

# Import the random module for generating random colors.
import random

# Import the PIL (Python Imaging Library) module for working with images.
from PIL import Image

# Import the sounddevice module for audio recording.
import sounddevice

# Import the scipy.io.wavfile module for working with WAV audio files.
from scipy.io.wavfile import *

# Import the customtkinter filedialog for customized file dialog boxes.
from customtkinter import filedialog

# Import the pygame.mixer module for playing audio sounds.
from pygame import mixer

# Import the time module for time-related functionality.
import time

# Create the main application window
App = CTk()
App.geometry("490x500+500+150")
App.resizable(False, False)
App._set_appearance_mode("Light")
App.title("VOICE RECORDER APP")
App.iconbitmap("images/app_icon.ico")

add = " "
mixer.init()

# ------------------ All Functions ----------------

# Function to select the file path for saving recordings
def file_path():
    global add
    add = filedialog.askdirectory()

# Function to handle the voice recording process
def voice_Record():
    global add
    if add == " ":
        messagebox.showerror("Path Not Found","Please Add a Path before proceeding")
    else:
        try:
            time1 = int(duration.get())
        except ValueError:
            messagebox.showerror("Invalid Input","Please enter a valid integer for the recording time.")
            return

        if time1 <= 0:
            messagebox.showerror("Invalid Input","Recording time should be greater than 0 seconds.")
        else:
            addr = add + '/' + "record.wav"
            mixer.music.load("audio_file/recording_start.mp3")
            mixer.music.play()
            messagebox.showinfo("Recording Started", "Recording has started.")



            try:
                rece = sounddevice.rec(int(time1 * 44100), samplerate=44100, channels=2)
                while time1>0:
                    App.update()
                    time.sleep(1)
                    time1=time1-1
                    time_label.configure(text=f"{str(time1)}")
                    if (time1==0):
                        mixer.music.load("audio_file/successful.mp3")
                        mixer.music.play()
                        messagebox.showinfo("Recording Completed", "Recording has stopped and saved as 'record.wav'.")
                        time_label.configure(text=" ")
                        duration.set("")
                sounddevice.wait()
                write(addr, 44100, rece)

            except Exception as e:
                print("Error:", e)
                messagebox.showerror("Error", "An error occurred during recording.")


# Function to change the color of title
def color_Change():
    choices1 = ["#342D7E", "#49413F", "#483C32", "#E30B5D"]
    color = random.choice(choices1)
    title.configure(fg_color=color)
    title_image.configure(fg_color=color)
    title_image2.configure(fg_color=color)
    title, title_image, title_image2.after(200, color_Change)

 # Function to exit the application
def exit_App():
    exiting=messagebox.askyesno("Exit Voice Recorder","Are You Sure You Want To Close This Voice Recorder")
    if exiting==True:
        App.destroy()


# Function to handle button hover
def hover(e):
    recording_btn.configure(image=record_hover_image, text="", fg_color="#ebebeb", bg_color="#ebebeb")


# Function to handle button hover (back to default)
def hoverBack(e):
    recording_btn.configure(image=record_image, text="", fg_color="#ebebeb", bg_color="#ebebeb", hover=True,
                            hover_color="#ebebeb")

# ------------------- All Images -------------------------------
recorder_title1 = CTkImage(Image.open("images/recorder_icon.png"), size=(50, 50))
recorder_title2 = CTkImage(Image.open("images/recorder_icon.png"), size=(50, 50))
record_image = CTkImage(Image.open("images/recording_button.png"), size=(110, 110))
record_hover_image = CTkImage(Image.open("images/hover_recorder_btn.png"), size=(110, 110))
file_path_image = CTkImage(Image.open("images/path_icon.png"), size=(55, 55))
voice_graph_img = CTkImage(Image.open("images/graph_img.png"), size=(450, 120))

# --------------------- All labels ---------------------------------

title = CTkLabel(App, text="VOICE RECORDER", text_color="white", width=490, font=("Bookman Old Style", 30, "bold"),
                 bg_color="#ebebeb", height=50)
title.place(x=0, y=2)

title_image = CTkLabel(App, text="", image=recorder_title1)
title_image.place(x=400, y=2)

title_image2 = CTkLabel(App, text="", image=recorder_title2)
title_image2.place(x=40, y=2)

voice_graph_label = CTkLabel(App,image=voice_graph_img,text=" ",fg_color="#DADBDD", bg_color="#ebebeb")
voice_graph_label.place(x=0, y=52, relwidth=1)

user_label = CTkLabel(App, text="Enter Time In Seconds....", text_color="#151B54", fg_color="#ebebeb",
                      bg_color="#ebebeb", font=("Helvetica", 16, "bold"))
user_label.place(x=155, y=245)

time_label = CTkLabel(App,text=" ", text_color="black",fg_color="#ebebeb",
                      bg_color="#ebebeb",font=("Helvetica", 25, "bold"))
time_label.place(x=233, y=280)

# ------------------EntryBox-------------------------------

# Create an entry box for the user to input the recording duration.
duration=StringVar()
duration.set("")
user_entry = CTkEntry(App, width=170, height=30,textvariable=duration,fg_color="white", corner_radius=5,
                      text_color="#34282C", bg_color="#ebebeb", justify="center",font=("bookman old style", 20, "bold"),
                      border_width=4, border_color="#3D0C02")
user_entry.place(x=160, y=200)
user_entry.focus()

# ---------------------------- Buttons --------------------------------

# Recording Button
recording_btn = CTkButton(App, image=record_image,text="",fg_color="#ebebeb", bg_color="#ebebeb",hover_color="#ebebeb",command=voice_Record)
recording_btn.place(x=30, y=310)
recording_btn.bind("<Enter>", hover)
recording_btn.bind("<Leave>", hoverBack)

# Path Button
path_btn = CTkButton(App, text="Select File Path", image=file_path_image, text_color="black", fg_color="#87AFC7",
                     border_width=3, command=file_path, border_color="black", bg_color="#ebebeb", hover_color="#A2AD9C",
                     font=("Poppins", 20, "bold"), corner_radius=10)
path_btn.place(x=220, y=335)

#Exit Button
exit_btn=CTkButton(App,text="EXIT",text_color="#F5F5F5",fg_color=("#5E5A80","#151B54"),bg_color="#ebebeb",
                   font=("Poppins",23,"bold"),corner_radius=20,width=120,command=exit_App,height=45,border_width=2,
                   border_color="black",hover_color="#357EC7")
exit_btn.place(x=182,y=437)

# Create an entry box for the user to input the recording duration.
color_Change()

# Create an entry box for the user to input the recording duration.
App.mainloop()
