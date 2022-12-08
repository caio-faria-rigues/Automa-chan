from tkinter import *
from tkinter import messagebox
from voice_functions import reco, verify_question
import threading
import speech_recognition as sr
from time import sleep
from win32com.client import Dispatch

r = sr.Recognizer()
voice = ''
response = ''
config_window = None
question_window = None
deb_num = 0
debug_status = False
reading = False

speak = Dispatch("SAPI.SpVoice").Speak


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
sprite_front_default = PhotoImage(
    file=r'C:\Users\Cliente\PycharmProjects\guppe\Projetos\Automa-chan alpha 2.0\src\sprites\sprite_front_default.png')

canvas1 = Canvas(root)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=background_image, anchor="nw")
canvas1.create_image(350, 23, image=sprite_front_default, anchor='nw')

automa_write = Label(root, text='', font=("Retro Gaming", 12), background="#e9d0d6")
automa_write.place(y=550, x=18)

# sprites


# historico de entradas
automa_hear = Text(root, font=("Retro Gaming", 12), background="#e9d0d6", height=22, width=25)
automa_hear.place(y=12, x=968)
# IMPORANTE CONSERTAR DEPOIS
if reading:
    last_read = automa_hear.get("end-1c linestart", END)
    print(last_read)


# botao de configuração:


def open_config_window():
    global config_window

    config_window.destroy() if config_window else None
    config_window = Toplevel(root)
    config_window.title = "Configurações"
    config_window.minsize(720, 480)
    config_window.maxsize(720, 480)
    config_window.config(bg="#e9d0d6")


def open_question_window():
    global question_window, response
    contador = 0
    breaker_ = False

    question_window.destroy() if question_window else None

    def breaker():
        breaker_ = True

    while True:
        if not question_window:
            question_window = Toplevel(root)
            question_window.title = "Ambiente de estudos"
            question_window.minsize(1040, 585)
            question_window.maxsize(1280, 720)
            question_window.config(bg="#e9d0d6")
            response_question = response[0]
            response_question_charlist = list(response_question)

            segments = round(len(response_question_charlist) / 100)

            while contador != segments:
                response_question_charlist.insert(contador * 100, '\n')
                contador += 1

            response_question = ''.join(response_question_charlist)
            print(response_question)

            reponse_answer = response[1]
            question = Label(
            question_window,
            text=response_question, font=("Retro Gaming", 12), background="#e9d0d6", justify='left')
            question.place(y=0, x=0)
            speak(response_question) if response is not None else None
            question_window.protocol("WM_DELETE_WINDOW", breaker)
            if breaker_:
                break
        else:
            pass


config_button_image = PhotoImage(
    file=r'C:\Users\Cliente\PycharmProjects\guppe\Projetos\Automa-chan alpha 2.0\src\config button2.png')
config_button = Button(root, image=config_button_image, borderwidth=0, bg="#e9d0d6", command=open_config_window).place(
    y=467, x=968)

# botao de depuração


debug_button_image = PhotoImage(
    file=r'C:\Users\Cliente\PycharmProjects\guppe\Projetos\Automa-chan alpha 2.0\src\debug button.png')


def debugger():
    global deb_num, automa_hear, debug_status
    if deb_num % 2 != 0:
        automa_hear.insert(END, "[debugger mode disabled]\n" + '\n')
        debug_status = False
    else:
        automa_hear.insert(END, "[debugger mode enabled]\n" + '\n')
        debug_status = True
    deb_num = deb_num + 1


debug_button = Button(root, image=debug_button_image, borderwidth=0, bg="#e9d0d6", command=debugger).place(y=467,
                                                                                                           x=1068)


# botao de info


def open_info_window():
    messagebox.showinfo("Info", "Automa-chan v1.0.2\nCriada por Caio Faria Rigues, terceiro ano do curso de Automação"
                        + " Industrail do IFF Pádua")


info_button_image = PhotoImage(
    file=r'C:\Users\Cliente\PycharmProjects\guppe\Projetos\Automa-chan alpha 2.0\src\info button.png')
info_button = Button(root, image=info_button_image, borderwidth=0, bg="#e9d0d6",
                     command=open_info_window).place(y=467, x=1168)

threading.Thread(target=hear).start()


def recognizer():
    global automa_write, voice, debug_status, reading, response
    while voice != "sair":
        response = reco(voice)
        if str(type(response)) == "<class 'list'>":
            response_question_command = response[2]
            speak(response_question_command) if response is not None else None
            automa_write.config(text=response_question_command)
        else:
            automa_write.config(text=response)
            speak(response) if response is not None else None
        print(response) if voice is not None else print('')

        if verify_question():
            open_question_window()

        if debug_status:
            automa_hear.insert(END, voice + '\n') if voice != '' else None
            reading = True
        if not debug_status:
            if "ei" in voice.lower():
                automa_hear.insert(END, voice + '\n') if voice != '' else None
            else:
                pass
        voice = ''
        sleep(1)
        automa_hear.yview_pickplace("end")


threading.Thread(target=recognizer).start()

root.mainloop()
