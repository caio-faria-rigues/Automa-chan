from tkinter import *
from voice_functions import reco
import threading
import speech_recognition as sr
from time import sleep

r = sr.Recognizer()
voice = ''


def hear():
    global voice
    print("ready!")
    with sr.Microphone() as source:
        while voice != 'sair':
            try:
                audio = r.listen(source)
                voice = r.recognize_google(audio, language='pt')
            except:
                pass


root = Tk()
root.title("Automa-chan")
root.minsize(1280, 720)
root.maxsize(1280, 720)
background_image = PhotoImage(
    file=r'C:\Users\Cliente\PycharmProjects\guppe\Projetos\Automa-chan alpha 2.0\src\background1.png')
canvas1 = Canvas(root)
canvas1.pack(fill="both", expand = True)
canvas1.create_image(0, 0, image=background_image, anchor="nw")

automa_write = Label(root, text='', font=("Retro Gaming", 12), background="#e9d0d6")
automa_write.place(y=550, x=18)

automa_hear = Text(root, font=("Retro Gaming", 12), background="#e9d0d6", height=22, width=25)
automa_hear.place(y=12, x=968)

threading.Thread(target=hear).start()


def recognizer():
    global automa_write
    global voice
    while voice != "sair":
        response = reco(voice)
        print(response) if voice is not None else print('')
        automa_write.config(text=response)

        automa_hear.insert(END, voice + '\n') if voice != '' else None
        voice = ''
        sleep(1)


threading.Thread(target=recognizer).start()

root.mainloop()
