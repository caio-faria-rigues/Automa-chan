import webbrowser
from functions import separa_maiusculo, temperatura, city, pesquisa_musica, pesquisa_questao


materia = ''
question_bool = False
materias = ['português', 'matemática', 'história']
question = []
humor = ''


def reco(voz):
    global question_bool, materia, materias, question

    user_voice = voz.lower()

    # |||||||||||||||||||||||||||||||||||||||||||||||reconhecimento||||||||||||||||||||||||||||||||||||||||||||||||||||
    if question_bool:

        if "próxima" in user_voice:
            return pesquisa_questao(materia)[0]
        if "outra" in user_voice:
            return pesquisa_questao(materia)[0]
        if "obrigado" in user_voice:
            question_bool = False
            return "De nada! Sempre que quiser estudar basta me chamar!"
        if "resposta" in user_voice:
            question_bool = False
            return pesquisa_questao(materia)[1]
        else:
            return question[0]

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
                    question_bool = True
                    question = pesquisa_questao(materia)
                    question.append('Abrindo ambiente de estudos...')
                    return question
            ### resolver isso depois
        elif "sword" in str(user_voice):
            webbrowser.open("https://www.youtube.com/watch?v=uWmhG_LHxDw&t=46s&ab_channel=NeroNightcore")
            return """I am The bone of my sword
            Steel is my body, and fire is my blood
            I have created over a thousand blades
            Unkow to death, nor known to life
            Have whisthood pain to build many weapons
            Yet, those hands will never hold anything
            So, as I pray
            UNLIMITED BLADE WORKS
            """

        else:
            pass


def verify_question():
    global question_bool
    if question_bool:
        return True
    else:
        return False
