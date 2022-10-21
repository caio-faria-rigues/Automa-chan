import requests
from bs4 import BeautifulSoup
from googlesearch import search
import speech_recognition as sr
import webbrowser
from time import sleep

""""""
r = sr.Recognizer()

voice = ''

maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U',
              'V', 'W', 'X', 'Y', 'Z']


def city(cidade):
    for resultado in search(f'"{cidade}" accuweather', stop=1):
        citylink = resultado

    return citylink


def temperatura(citylink):
    url = str(citylink)
    headers = {
                "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    citytemp = soup.find('div', class_='temp').get_text()

    return citytemp


def pesquisa_musica(musica):
    for resultado in search(f'"{musica}" youtube', stop=1):
        music = resultado

    return music


def separa_maiusculo(frase):
    cidade = []
    lista = frase.split(" ")
    for palavra in lista:
        if palavra[0] in maiusculas:
            cidade.append(palavra)
    cidadestr = " ".join(cidade)
    return cidadestr

""""""


class Voice:
    def voicereco(self):
        with sr.Microphone() as source:
            while voice != 'sair':
                try:
                    audio = self.listen(source)

                    voice = self.recognize_google(audio, language='pt')
                    print(f">>{voice}")
                    if "ei" in voice:
                        if "Bom dia" in str(voice):
                            print("Olá")
                        elif "temperatura" in voice:
                            cidade = separa_maiusculo(str(voice))
                            print(temperatura(city(cidade)))
                        elif "graus" in voice:
                            cidade = separa_maiusculo(str(voice))
                            print(temperatura(city(cidade)))
                        elif "Chainsaw Man" in str(voice):
                            print("Fujima God simplesmente")
                        else:
                            pass
                    if "Ei" in voice:
                        if "Bom dia" in str(voice):
                            print("Olá")
                        elif "temperatura" in voice:
                            cidade = separa_maiusculo(str(voice))
                            print(temperatura(city(cidade)))
                        elif "graus" in voice:
                            cidade = separa_maiusculo(str(voice))
                            print(temperatura(city(cidade)))
                        elif "Chainsaw Man" in str(voice):
                            print("Fujima God simplesmente")
                        elif "ouvir" in str(voice):
                            musica = str(voice)
                            url = pesquisa_musica(musica)
                            webbrowser.open(url)
                        else:
                            pass
                except:
                    pass


class Listener:
    def __init__(self, voz):
        user_voice = voz
        if "ei" in user_voice:
            if "Bom dia" in str(user_voice):
                print("Olá")
            elif "temperatura" in user_voice:
                cidade = separa_maiusculo(str(user_voice))
                print(temperatura(city(cidade)))
            elif "graus" in user_voice:
                cidade = separa_maiusculo(str(user_voice))
                print(temperatura(city(cidade)))
            elif "Chainsaw Man" in str(user_voice):
                print("Fujima God simplesmente")
            else:
                pass
        if "Ei" in user_voice:
            if "Bom dia" in str(user_voice):
                print("Olá")
            elif "temperatura" in user_voice:
                cidade = separa_maiusculo(str(user_voice))
                print(temperatura(city(cidade)))
            elif "graus" in user_voice:
                cidade = separa_maiusculo(str(user_voice))
                print(temperatura(city(cidade)))
            elif "Chainsaw Man" in str(user_voice):
                print("Fujima God simplesmente")
            elif "ouvir" in str(user_voice):
                musica = str(user_voice)
                url = pesquisa_musica(musica)
                webbrowser.open(url)
            else:
                pass

    def city(cidade):
        for resultado in search(f'"{cidade}" accuweather', stop=1):
            citylink = resultado

        return citylink

    def temperatura(citylink):
        url = str(citylink)
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        citytemp = soup.find('div', class_='temp').get_text()

        return citytemp

    def pesquisa_musica(musica):
        for resultado in search(f'"{musica}" youtube', stop=1):
            music = resultado

        return music

    def separa_maiusculo(frase):
        cidade = []
        lista = frase.split(" ")
        for palavra in lista:
            if palavra[0] in maiusculas:
                cidade.append(palavra)
        cidadestr = " ".join(cidade)
        return cidadestr


def reco(voz):
    def city(cidade):
        for resultado in search(f'"{cidade}" accuweather', stop=1):
            citylink = resultado

        return citylink

    def temperatura(citylink):
        url = str(citylink)
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        citytemp = soup.find('div', class_='temp').get_text()

        return citytemp

    def pesquisa_musica(musica):
        for resultado in search(f'"{musica}" youtube', stop=1):
            music = resultado

        return music

    def separa_maiusculo(frase):
        cidade = []
        lista = frase.split(" ")
        for palavra in lista:
            if palavra[0] in maiusculas:
                cidade.append(palavra)
        cidadestr = " ".join(cidade)
        return cidadestr

    user_voice = voz.lower()
    if "ei" in user_voice:
        if "bom dia" in str(user_voice):
            print("Olá")
            return "Olá! Bom dia!"

        elif "temperatura" in user_voice:
            cidade = separa_maiusculo(str(voz))
            print(temperatura(city(cidade)))
            return temperatura((city(cidade)))

        elif "graus" in user_voice:
            cidade = separa_maiusculo(str(voz))
            print(temperatura(city(cidade)))
            return temperatura((city(cidade)))

        elif "ouvir" in str(user_voice):
            musica = str(user_voice)
            url = pesquisa_musica(musica)
            webbrowser.open(url)
            return "Certo! Abrindo o YouTube!"
        else:
            pass
