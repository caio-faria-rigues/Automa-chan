import requests
from bs4 import BeautifulSoup
from googlesearch import search
import webbrowser

maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U',
              'V', 'W', 'X', 'Y', 'Z']


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

    # reconhecimento

    if "ei" in user_voice:
        if "bom dia" in str(user_voice):
            print("Olá")
            return "Olá! Bom dia!"

        elif "temperatura" in user_voice:
            cidade = separa_maiusculo(str(voz))
            cidade2 = cidade.replace("Ei", '')
            print(temperatura(city(cidade)))
            temp = temperatura((city(cidade)))
            return f"Em {cidade2} faz {temp}!"

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
