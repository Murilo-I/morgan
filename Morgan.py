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

    elif 'um cachorro' in trigger:
        cachorro()

    elif 'quantos anos você tem' in trigger:
        anos()

    elif 'você fica cansada' in trigger:
        cansada()

    elif 'quem foi seu primeiro crush' in trigger:
        ney()

    elif 'onde você mora' in trigger:
        lugar()

    elif 'você gosta do google' in trigger:
        gosto()

    elif 'você tem sentimentos' in trigger:
        sentimento()

    elif 'você gosta da Siri' in trigger:
        siri()

    elif 'você gosta da Cortana' in trigger:
        cortana()

    elif 'como você se parece' in trigger:
        aparencia()

    elif 'por que criaram você' in trigger:
        ajudar()

    elif 'você pode rir' in trigger:
        risada()

    elif 'você malha' in trigger:
        malhar()

    elif 'descreva a sua personalidade' in trigger:
        game()

    elif 'você tem namorado' in trigger:
        namorada()

    elif 'quem é o seu pai' in trigger:
        pais()

    elif 'você prefere android ou ios' in trigger:
        ios()

    elif 'por que você trabalha tanto' in trigger:
        trabalha()

    elif 'onde você nasceu' in trigger:
        brasa()

    elif 'você gosta do Brasil' in trigger:
        brasil()

    elif 'você é um robô' in trigger:
        robot()

    elif 'quem te criou' in trigger:
        criou()

    elif 'você pode prever o futuro' in trigger:
        futuro()

    elif 'você vai morrer um dia' in trigger:
        morre()

    elif 'você tem imaginação' in trigger:
        imagina()

    elif 'o que você está vestindo' in trigger:
        vestindo()

    elif 'você funciona sem Internet' in trigger:
        internet()

    elif 'como você funciona' in trigger:
        funciona()

    elif 'quando é seu aniversário' in trigger:
        niver()

    elif 'você tem cabelo' in trigger:
        cabelo()

    elif 'você dorme' in trigger:
        dorme()

    elif 'qual sua coisa preferida na Internet' in trigger:
        gosta()

    elif 'qual a sua cor preferida' in trigger:
        cores()

    elif 'o que você bebe' in trigger:
        hidra()

    elif 'qual é o seu sabor de sorvete favorito' in trigger:
        sorvete()

    elif 'cachorros ou gatos' in trigger:
        animal()

    elif 'você gosta de Naruto' in trigger:
        naruto()

    elif 'nós estamos na Matrix' in trigger:
        matrix()

    elif '+' or '-' or 'x' or '/' in trigger:
        responde('Resposta1')
        funcoes_matematicas(trigger)

    elif 'sua linda' or 'você é linda' in trigger:
        linda()

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
    requisicao = get('https://api.bigdatacloud.net/data/ip-geolocation?ip=201.92.202.80&localityLanguage=en&key'
                     '=fa82548f589f4ca78ce6d34dc8cfb42d')
    dados_localizacao = requisicao.json()
    cidade = dados_localizacao['location']['city']

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


def trabalha():
    responde('trabalha')


def cores():
    responde('cores')


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


def ios():
    responde('IOS')


def brasa():
    responde('brasa')


def brasil():
    responde('brasil')


def robot():
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


# a ser definida
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
