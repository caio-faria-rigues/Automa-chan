import requests
from bs4 import BeautifulSoup
from googlesearch import search
import webbrowser
from functions import separa_maiusculo, temperatura, city, pesquisa_musica, pesquisa_questao


materia = ''
question = False
materias = ['português', 'matemática', 'história']


def reco(voz):
    global question, materia

    user_voice = voz.lower()

    # |||||||||||||||||||||||||||||||||||||||||||||||reconhecimento||||||||||||||||||||||||||||||||||||||||||||||||||||
    if question:
        if "próxima" in user_voice:
            return pesquisa_questao(materia)[0]
        if "outra" in user_voice:
            return pesquisa_questao(materia)[0]
        if "obrigado" in user_voice:
            question = False
            return "De nada! Sempre que quiser estudar basta me chamar!"
        if "resposta" in user_voice:
            question = False
            return pesquisa_questao(materia)[1]

    if "ei" in user_voice:
        if "bom dia" in user_voice:
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

        elif "pesquise" in str(user_voice):
            user_voice_search = user_voice[12].upper() + user_voice[13::]
            url = f"www.google.com/search?q={user_voice_search}"
            webbrowser.open(url)
            return f"Pesquisando {user_voice[11::]} no Google"

        elif "questão" in str(user_voice):
            phrase_list = user_voice.split()
            for word in phrase_list:
                if word in materias:
                    materia = word
                    question = True
                    return pesquisa_questao(materia)[0]
            ### resolver isso depois
        else:
            pass
