import pygame   #import pygame module
from pygame import mixer #for playing music
from tkinter import * #Gui module
from tkinter import filedialog #fileDialog module for file selection
from tkinter.messagebox import showinfo #messagebox or alert


root = Tk() #our main frame
root.geometry("400x400") #dimensions of our frame
root.title("Music Player") #title of our player
root.iconbitmap("player.ico") #player icon name
root.configure(bg='lavender') #bg color

def refresh(root):
    root.destroy() #to destroy the root window
    root.__init__() #to initialize/start the root window again

def select():
    #Select the file through this line of code
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("MP3 files","*.mp3"),("all files","*.*")))
    return True

def play():
    mixer.init() #Initialize Mixer
    mixer.music.load(root.filename) #load the file selected from the directory
    mixer.music.play() #play the selected file
    Label(root, text="Now Playing:\n"+root.filename, bg='lavender', font =("Arial", 8, "italic")).pack() #will display the name of song playing
    showinfo("SUP","Your Music is playing, Enjoy it ;)") #alert that you song is being played
    return True

def stop(tog=[0]):
    #toggle button for play and pause the music
    tog[0]= not tog[0]
    if tog[0]:
        mixer.music.pause()
    else:
        mixer.music.unpause()
    return True


#Heading
Label(root, text="Play Your Song!", bg='lavender', font =("Times", 20, "bold")).pack()
Label(root, text="Select the song you wanna play!", bg='lavender', font =("Times", 12, "bold")).pack()

#file selection button with image on it
selecta = PhotoImage(file = r"C:\Users\DELL\Desktop\My Work\GUI MP3\select.png")
button1=Button(root, text="Select",image= selecta, compound=LEFT,width=12,font =("Times", 11, "bold"), command=select).pack(ipadx=50, pady=10)

#start button to start playing the music with image on it
start = PhotoImage(file = r"C:\Users\DELL\Desktop\My Work\GUI MP3\play.png")
button2=Button(root, text="Start",image= start, compound=LEFT,width=12,font =("Times", 11, "bold"), command=play).pack(ipadx=50, pady=10)

#play/pause button with image on it to play/stop the song
pause = PhotoImage(file = r"C:\Users\DELL\Desktop\My Work\GUI MP3\pause.png")
button3=Button(root, text="Play/Pause",image= pause, compound=LEFT,width=12,font =("Times", 11, "bold"), command=stop).pack(ipadx=50, pady =10)

#refresh button to refresh the window with image on it
refresher = PhotoImage(file = r"C:\Users\DELL\Desktop\My Work\GUI MP3\refresh.png")
button4=Button(root, text="Refresh",image= refresher, compound=LEFT,width=12,font =("Times", 11, "bold"), command=refresh).pack(ipadx=50, pady =10)

#Exit Button
button5=Button(root, text="Exit",width=12,font =("Times", 11, "bold"), command=exit).pack(padx=30, pady =10)

root.mainloop()



