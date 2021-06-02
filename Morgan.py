import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
import random
from datetime import datetime
from play_music import whato_play
from open_browsers import abrir


# CONFIGURAÇÕES #

hotword = 'morgan'


# FUNÇÕES PRINCIPAIS #

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando Comando: ")
            audio = microfone.listen(source)

            try:
                # trigger -> PALAVRAS CHAVES NA FRASE #
                trigger = microfone.recognize_google(audio, language="pt-BR")
                trigger = trigger.lower()

                if hotword in trigger:
                    print('Comando: ' + trigger)
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Morgan não entendeu o audio")
                r = random.randint(1, 5)
                responde("naoEntendi" + str(r))
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return trigger


def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')


def cria_audio(mensagem):
    tss = gTTS(mensagem, lang='pt-br')
    tss.save('audios/mensagem.mp3')
    print('Morgan: ' + mensagem)
    playsound('audios/mensagem.mp3')
    os.remove('audios/mensagem.mp3')



def executa_comandos(trigger):
    if 'notícias' in trigger:
        responde('Resposta1')
        ultimas_noticias()

    elif 'toca' in trigger:
        responde('Resposta1')
        whato_play(trigger)

    elif 'abrir' in trigger:
        abrir(trigger)

    elif 'piada' in trigger:
        piada()

    elif 'curiosidade' in trigger:
        curiosidade()

    elif 'adolescente' in trigger:
        adolescente()

    elif 'me irrita' in trigger:
        irritando()

    elif 'pedra' and 'papel' and 'tesoura' in trigger:
        jokenpo()

    elif 'horas são' in trigger:
        horacao()

    elif 'você está aí' in trigger:
        tonao()

    elif 'você é surda' in trigger:
        surda()

    elif 'clima agora' in trigger:
        responde('Resposta1')
        previsao_tempo(tempo=True)

    elif 'tempo hoje' in trigger:
        responde('Resposta1')
        previsao_tempo(minmax=True)

    elif 'defina um alarme' in trigger:
        responde('Resposta1')
        agenda(trigger)
        responde('Resposta4')

    elif 'sua linda' or 'você é linda' in trigger:
        linda()

    elif 'um cachorro' in trigger:
        cachorro()

    elif 'Quantos anos você tem?' in trigger:
        anos()

    elif 'Você fica cansada ?' in trigger:
        cansada()

    elif 'Quem foi seu primeiro crush?' in trigger:
        ney()

    elif 'Onde você mora?' in trigger:
        lugar()

    elif 'Você gosta do Google?' in trigger:
        gosto()

    elif 'Você tem sentimentos?' in trigger:
        sentimento()

    elif 'Você gosta da Siri?' in trigger:
        siri()

    elif 'Você gosta da Cortana?' in trigger:
        cortana()

    elif 'Como você se parece?' in trigger:
        aparencia()

    elif 'Por que criaram você?' in trigger:
        ajudar()

    elif 'Você pode rir?' in trigger:
        risada()

    elif 'Você malha?' in trigger:
        malhar()

    elif 'Descreva a sua personalidade.' in trigger:
        game()

    elif 'Você tem namorado?' in trigger:
        namorada()

    elif 'Quem é o seu pai?' in trigger:
        pais()

    elif 'Você prefere Android ou iOS?' in trigger:
        IOS()

    elif 'Por que você trabalha tanto?' in trigger:
        trabalha()

    elif 'Onde você nasceu?' in trigger:
        brasa()

    elif 'Você gosta do Brasil?' in trigger:
        brasil()

    elif 'Você é um robô?' in trigger:
        robô()

    elif 'Quem te criou?' in trigger:
        criou()

    elif 'Você pode prever o futuro?' in trigger:
        futuro()

    elif ' Você vai morrer um dia?' in trigger:
        morre()

    elif 'Você tem imaginação?' in trigger:
        imagina()

    elif 'O que você está vestindo?' in trigger:
        vestindo()

    elif 'Você funciona sem Internet?' in trigger:
        internet()

    elif 'Como você funciona?' in trigger:
        funciona()

    elif 'Quando é seu aniversário?' in trigger:
        niver()

    elif 'Você tem cabelo?' in trigger:
        cabelo()

    elif 'Você dorme?' in trigger:
        dorme()

    elif 'Qual sua coisa preferida na Internet?' in trigger:
        gosta()

    elif 'Qual a sua cor preferida?' in trigger:
        cores()

    elif 'O que você bebe?' in trigger:
        hidra()

    elif 'Qual é o seu sabor de sorvete favorito?' in trigger:
        sorvete()

    elif 'Cachorros ou gatos?' in trigger:
        animal()

    elif 'Você gosta de Naruto ?' in trigger:
        naruto()

    elif 'Nós estamos na Matrix?' in trigger:
        matrix()

    elif '+' or '-' or 'x' or '/' in trigger:
        responde('Resposta1')
        funcoes_matematicas(trigger)

    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('Comando inválido: ', mensagem)
        r = random.randint(2, 3)
        responde('Resposta' + str(r))


# FUNÇÕES COMANDOS #

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&g=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    manchetes = []
    for item in noticias.findAll('item')[:10]:
        manchetes.append(item)

    r = random.randint(1, 9)
    mensagem = manchetes[r].title.text
    cria_audio(mensagem)


def cidade_atual():
    requisicao = get('http://api.ipstack.com/201.92.202.80?access_key=2e9b3b8a0a63c50affc3e72ebfde6aef&format=1')
    dados_localizacao = requisicao.json()
    cidade = dados_localizacao['city']

    return cidade


def previsao_tempo(tempo=False, minmax=False):
    localizacao_atual = cidade_atual()

    site = get(
        f'http://api.openweathermap.org/data/2.5/weather?q={localizacao_atual}&appid=f3df126f823c2d5eadd1de251880b7b1&'
        'units=metric&lang=pt')

    clima = site.json()
    temp = clima['main']['temp']
    min_temp = clima['main']['temp_min']
    max_temp = clima['main']['temp_max']
    desc = clima['weather'][0]['description']
    mensagem = ''

    if tempo:
        mensagem = f'Agora fazem {temp} graus em {localizacao_atual}. Clima: {desc}'
    elif minmax:
        mensagem = f'Hoje a mínima será de {min_temp} e a máxima de {max_temp}'

    cria_audio(mensagem)


def funcoes_matematicas(trigger: str):
    error_msg = 'desculpa, não consegui fazer a conta'

    if '+' in trigger:
        sentenca = trigger.split(sep='+')
        parte1 = sentenca[0].split()

        num1 = parte1[-1]
        num2 = sentenca[1].lstrip()

        if num1.isdigit() & num2.isdigit():
            result = float(num1) + float(num2)
            mensagem = f'{num1} mais {num2} é igual a {result}'
            cria_audio(mensagem)
        else:
            cria_audio(error_msg)

    elif '-' in trigger:
        sentenca = trigger.split(sep='-')
        parte1 = sentenca[0].split()

        num1 = parte1[-1]
        num2 = sentenca[1].lstrip()

        if num1.isdigit() & num2.isdigit():
            result = float(num1) - float(num2)
            mensagem = f'{num1} menos {num2} é igual a {result}'
            cria_audio(mensagem)
        else:
            cria_audio(error_msg)

    elif 'x' in trigger:
        sentenca = trigger.split(sep='x')
        parte1 = sentenca[0].split()

        num1 = parte1[-1]
        num2 = sentenca[1].lstrip()

        if num1.isdigit() & num2.isdigit():
            result = float(num1) * float(num2)
            print(result)
            mensagem = f'{num1} vezes {num2} é igual a {result}'
            cria_audio(mensagem)
        else:
            cria_audio(error_msg)

    elif '/' in trigger:
        sentenca = trigger.split(sep='/')
        parte1 = sentenca[0].split()

        num1 = parte1[-1]
        num2 = sentenca[1].lstrip()

        if num1.isdigit() & num2.isdigit():
            result = float(num1) / float(num2)
            mensagem = f'{num1} dividido por {num2} é igual a {result}'
            cria_audio(mensagem)
        else:
            cria_audio(error_msg)

            # RESPOSTAS #

def curiosidade():
    r = random.randint(1, 3)
    responde('Curiosidade' + str(r))


def piada():
    r = random.randint(1, 3)
    responde('Piada' + str(r))


def missao():
    r = random.randint(1, 3)
    responde('mao' + str(r))


def jokenpo():
    r = random.randint(1, 3)
    responde('missao' + str(r))


def adolescente():
    responde('adolescente')

def cachorro():
    responde('cachorro')

def anos():
    responde('anos')

def cansada():
    responde('cansada')

def ney():
    responde('ney')

def lugar():
    responde('lugar')

def gosto():
    responde('gosto')

def sentimento():
    responde('sentimento')

def siri():
    responde('siri')

def cortana():
    responde('cortana')

def aparencia():
    responde('aparencia')

def ajudar():
    responde('ajudar')

def risada():
    responde('risada')

def malhar():
    responde('malhar')

def game():
    responde('game')

def namorada():
    responde('namorada')

def pais():
    responde('pais')

def IOS():
    responde('IOS')

def brasa():
    responde('brasa')

def brasil():
    responde('brasil')

def robô():
    responde('robô')

def criou():
    responde('criou')

def futuro():
    responde('futuro')

def imagina():
    responde('imagina')

def morre():
    responde('morre')

def vestindo():
    responde('vestindo')

def internet():
    responde('internet')

def funciona():
    responde('funciona')

def niver():
    responde('niver')

def cabelo():
    responde('cabelo')

def dorme():
    responde('dorme')

def gosta():
    responde('gosta')

def core():
    responde('cores')

def hidra():
    responde('hidra')

def sorvete():
    responde('sorvete')

def animal():
    responde('animal')

def naruto():
    responde('naruto')

def matrix():
    responde('matrix')







def irritando():
    responde('irritando')


def agenda(trigger):
    sentenca = trigger.split(sep='para as')
    hora = sentenca[1].lstrip()
    mensagem = f'você tem um compromisso as {hora}, ou seja, agora'
    cria_audio(mensagem)


def horacao():
    horario = datetime.now().strftime('%H:%M')
    mensagem = 'Agora são ' + horario
    cria_audio(mensagem)


def tonao():
    mensagem = 'Não, to não, eu me demiti'
    cria_audio(mensagem)


def surda():
    r = random.randint(1, 2)
    responde('surda' + str(r))


def linda():
    r = random.randint(1, 5)
    responde('linda' + str(r))


def main():
    r = random.randint(1, 3)
    responde('ola' + str(r))
    while True:
        monitora_audio()


main()
