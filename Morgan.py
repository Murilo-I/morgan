import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
import random
from datetime import datetime
from play_music import whato_play
from open_browsers import abrir


# CONFIGURAÇÕES #

hotword = 'morgan'
triggers = [
    'notícias',
    'toca',
    'piada',
    'curiosidade',
    'horas são',
    'você está aí',
    'você é surda',
    'tempo hoje',
    'clima agora',
    'defina um alarme',
    '+', '-', 'x', '/'
]


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

    elif '+' or '-' or 'x' or '/' in trigger:
        responde('Resposta1')
        funcoes_matematicas(trigger)

    if trigger not in triggers:
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


def previsao_tempo(tempo=False, minmax=False):
    site = get(
        'http://api.openweathermap.org/data/2.5/weather?q=barueri&appid=f3df126f823c2d5eadd1de251880b7b1&units=metric'
        '&lang=pt')

    clima = site.json()
    temp = clima['main']['temp']
    min_temp = clima['main']['temp_min']
    max_temp = clima['main']['temp_max']
    desc = clima['weather'][0]['description']
    mensagem = ''

    if tempo:
        mensagem = f'Agora fazem {temp} graus com {desc}'
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
    mensagem = 'Oi, desculpa, estava jogando free fire, o que você quer'
    cria_audio(mensagem)


def main():
    r = random.randint(1, 3)
    responde('ola' + str(r))
    while True:
        monitora_audio()
