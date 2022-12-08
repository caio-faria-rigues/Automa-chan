import webbrowser
from functions import separa_maiusculo, temperatura, city, pesquisa_musica, pesquisa_questao, calcular
from word2number import w2n
from py_trans import PyTranslator
from AppOpener import run
from datetime import datetime

materia = ''
question_bool = False
materias = ['linguagens', 'matemática', 'história', 'biologia', 'quimica', 'fisica', ]
question = []
humor = ''
pytranslator = PyTranslator(provider="google")


def reco(voz):
    global question_bool, materia, materias, question

    user_voice = voz.lower()

    # |||||||||||||||||||||||||||||||||||||||||||||||reconhecimento||||||||||||||||||||||||||||||||||||||||||||||||||||

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
            cidade2 = cidade.replace("Ei", '')
            print(temperatura(city(cidade)))
            temp = temperatura((city(cidade)))
            return f"Em {cidade2} faz {temp}!"

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

        elif "quanto" in str(user_voice):
            operacao = str(user_voice[11::])
            operator_list = operacao.split()
            num1 = operator_list[0]
            num2 = operator_list[len(operator_list) - 1]
            del(operator_list[0])
            del(operator_list[len(operator_list) - 1])
            operador = operator_list[0]
            return str(calcular(num1, operador, num2))

        elif "abrir" in str(user_voice):
            run(str(user_voice[9::]))
            return f"Abrindo {str(user_voice[9::])}"

        elif "horas" in str(user_voice):
            now = datetime.now()
            return f"São {now.hour} horas e {now.minute} minutos"

        elif "hoje" in str(user_voice):
            now = datetime.now()
            return f"Hoje é dia {now.day} do mês {now.month} de {now.year}"

        elif "futebol" in str(user_voice):
            return "Há, todo mundo tenta, mas só o Brasil é penta (por enquanto)"

        elif "jogador" in str(user_voice):
            return "Com apenas 21 anos, Takefusa Kubo se tornou o jogador mais jovem com nome de figura geométrica\n" \
                   + " adisputar uma Copa do Mundo, superando o argentino Redondo que estreou \ncom 25 anos em 1994 e" \
                   + "o colombiano Cuadrado, que estreou com 26 em 2014."

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
