import requests
from bs4 import BeautifulSoup
from googlesearch import search
import webbrowser
from random import shuffle

maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}


def humor(querry):
    if querry == 'normal':
        return 'normal'
    else:
        return 'angry'


def city(cidade):
    for resultado in search(f'"{cidade}" accuweather', stop=1):
        citylink = resultado

    return citylink


def temperatura(citylink):
    global headers
    url = str(citylink)

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


# ---------------------questões------------------------------


def spaces(quest_beta):
    espacos = ["						", "                        ", "                         ",
               "	", "						 ", "						 ", "						 "]
    for voids in espacos:
        if voids in quest_beta:
            quest_beta = quest_beta.replace(voids, "")
    return quest_beta


def multiplereplace(text):
    return "".join([char if char in "ABCDE" else "" for char in text])


def resposta(link, num):
    global headers
    url = link

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = str(soup.find_all('table', id='tabela-respostas'))
    gridslist = list(grids)
    grid = multiplereplace(gridslist)
    return grid[num]


def pesquisa_questao(materia):
    global headers
    for resultado in search(f'"{materia} questões" projetoagathaedu', stop=1):
        url = resultado

    # lista de matérias
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    grids = soup.find_all('div', class_='opcao')

    # pega um indice de matéria aleatória
    index_list = list(range(41))
    shuffle(index_list)
    index = index_list.pop()

    # pega a caixa da matéria
    grid = grids[index]

    # pega o link da matéria
    str_link = str(grid.find('a', href=True))
    list_link = str_link.split("\n")
    href = list_link[0]
    link = href[11:len(href) - 2]
    url2 = f'https://projetoagathaedu.com.br{link}'

    # quantidade de questões da matéria
    quest_qtd = grid.find('div', class_='lista-tema-numero').get_text()

    # lista de questões
    quest_bank = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(quest_bank.content, 'html.parser')
    quest_head = soup2.find_all('div', class_='questoes-enem-vestibular')

    # pega o indice da questão
    quests_list = list(range(int(quest_qtd)))
    shuffle(quests_list)
    quest_index = quests_list.pop()

    # pega uma questão
    try:
        quest_beta = (quest_head[quest_index]).get_text().strip()
    except:
        quest_beta = 'Não achei essa questão :(. Tente Novamente'

    # pega a resposta
    try:
        ans = f"A resposta correta é a letra {resposta(url2, quest_index)}!"
    except:
        ans = f"Algo deu errado. Tente novamente ou verifique a resposta em: {url2}"

    quest = spaces(quest_beta)
    return [str(quest), ans]
