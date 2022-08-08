from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

janela = Tk()
janela.title("Hinário Adventista")
janela.geometry("920x670+290+85")
janela.configure(bg="#0f1a2b")
janela.resizable(False, False)

mixer.init()


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        ##       print(songs)
        for songs in songs:
            if songs.endswith(".mp3"):
                playlist.insert(END, songs)


def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])


# Icones

image_icon = PhotoImage(file="imagens/logo.png")
janela.iconphoto(False, image_icon)

Top = PhotoImage(file="imagens/top.png")
Label(janela, image=Top, bg="#0f1a2b").pack()

# Logo
Logo = PhotoImage(file="hinario/teaser.png")
Label(janela, image=Logo, bg="#0f1a2b").place(x=65, y=115)

# Butões
play_butao = PhotoImage(file="imagens/play.png")
Button(janela, image=play_butao, bg="#0f1a2b", bd=0, command=play_song).place(x=100, y=400)

stop_butao = PhotoImage(file="imagens/stop.png")
Button(janela, image=stop_butao, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

resume_butao = PhotoImage(file="imagens/resume.png")
Button(janela, image=resume_butao, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause_butao = PhotoImage(file="imagens/pause.png")
Button(janela, image=pause_butao, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200, y=500)

# Label
music = Label(janela, text="", font=("arial", 15), fg="white", bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

# Musicas
Menu = PhotoImage(file="imagens/menu.png")
Label(janela, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

music_frame = Frame(janela, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=250)

Button(janela, text="Abrir Pasta", width=15, height=2, font=("arial", 10, "bold"), fg="white", bg="#21b3de",
       command=open_folder).place(x=330, y=300)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue",
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

janela.mainloop()
