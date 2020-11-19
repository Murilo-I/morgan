import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
import random
from play_music import whato_play

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
                # trigger -> PALAVRA CHAVE(morgan), esperando comando #
                trigger = microfone.recognize_google(audio, language="pt-BR")
                trigger = trigger.lower()

                if hotword in trigger:
                    print('Comando: ' + trigger)
                    responde('Resposta1')
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
        ultimas_noticias()

    elif 'toca' in trigger:
        whato_play(trigger)

    elif 'clima agora' in trigger:
        previsao_tempo(tempo=True)

    elif 'tempo hoje' in trigger:
        previsao_tempo(minmax=True)

    elif '+' or '-' or 'x' or '/' in trigger:
        funcoes_matematicas(trigger)

    elif 'curiosidade' in trigger:
        curiosidade()

    elif 'piada' in trigger:
        piada()

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
    for item in noticias.findAll('item')[:9]:
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
        mensagem = f'Hoje a mínima é de {min_temp} e a máxima de {max_temp}'

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


def main():
    while True:
        monitora_audio()


main()
