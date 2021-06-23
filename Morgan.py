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
morgan_msg = ''


# FUNÇÕES PRINCIPAIS #

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            microfone.adjust_for_ambient_noise(source)
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


def salva_msg_global(msg):
    global morgan_msg
    morgan_msg = msg


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

    elif 'você gosta da google' in trigger:
        google()

    elif 'você tem sentimentos' in trigger:
        sentimento()

    elif 'você gosta da siri' in trigger:
        siri()

    elif 'você gosta da cortana' in trigger:
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

    elif 'você tem pais' in trigger:
        pais()

    elif 'você prefere android ou ios' in trigger:
        ios()

    elif 'por que você trabalha tanto' in trigger:
        trabalha()

    elif 'onde você nasceu' in trigger:
        brasa()

    elif 'você gosta do brasil' in trigger:
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

    elif 'você funciona sem internet' in trigger:
        internet()

    elif 'como você funciona' in trigger:
        funciona()

    elif 'quando é seu aniversário' in trigger:
        niver()

    elif 'você tem cabelo' in trigger:
        cabelo()

    elif 'você dorme' in trigger:
        dorme()

    elif 'qual sua coisa preferida na internet' in trigger:
        gostanet()

    elif 'qual a sua cor preferida' in trigger:
        cores()

    elif 'o que você bebe' in trigger:
        hidratado()

    elif 'qual é o seu sabor de sorvete favorito' in trigger:
        sorvete()

    elif 'cachorros ou gatos' in trigger:
        animal()

    elif 'você gosta de naruto' in trigger:
        naruto()

    elif 'nós estamos na matrix' in trigger:
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
    salva_msg_global(mensagem)
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

    salva_msg_global(mensagem)
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
            salva_msg_global(mensagem)
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
            salva_msg_global(mensagem)
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
            salva_msg_global(mensagem)
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
            salva_msg_global(mensagem)
            cria_audio(mensagem)
        else:
            cria_audio(error_msg)


def horacao():
    horario = datetime.now().strftime('%H:%M')
    mensagem = 'Agora são ' + horario
    salva_msg_global(mensagem)
    cria_audio(mensagem)


# RESPOSTAS #


def curiosidade():
    r = random.randint(1, 3)
    msg = ''
    if r == 1:
        msg = 'você sabia que júpiter e o maior e mais radioativo planeta do sistema solar'
    if r == 2:
        msg = 'o local mais fundo do planeta terra é as fossas das marianas, com cerca de 11km de profundidade'
    if r == 3:
        msg = 'o lugar naturalmente mais perigoso da terra é o vale da morte, um deserto com temperatura média de 57°' \
              ' na Califórnia '

    salva_msg_global(msg)
    responde('Curiosidade' + str(r))


def piada():
    r = random.randint(1, 3)
    msg = ''
    if r == 1:
        msg = 'O que o próton disse para o elétron ? Hoje você está muito negativo'
    if r == 2:
        msg = 'o que o tomate foi fazer no banco, tirar extrato'
    if r == 3:
        msg = 'qual a tecla preferida do astronauta, a barra de espaço'

    salva_msg_global(msg)
    responde('Piada' + str(r))


def missao():
    r = random.randint(1, 3)
    msg = ''
    if r == 1:
        msg = 'Minha missão é criar a vacina não chinesa, do coronga'
    if r == 2:
        msg = 'Minha missão é saber construir no fortnite e no minecraft'
    if r == 3:
        msg = 'Minha missão é dominar o mundo junto com as minhas amigas siri, google e alexa'

    salva_msg_global(msg)
    responde('missao' + str(r))


def jokenpo():
    r = random.randint(1, 3)
    msg = ''
    if r == 1:
        msg = 'Pedra'
    if r == 2:
        msg = 'Papel'
    if r == 3:
        msg = 'Tesoura'

    salva_msg_global(msg)
    responde('mao' + str(r))


def surda():
    r = random.randint(1, 2)
    msg = ''
    if r == 1:
        msg = 'foi mal, tava jogando free fire, o que você quer'
    if r == 2:
        msg = 'Nossa, seu grosso'

    salva_msg_global(msg)
    responde('surda' + str(r))


def linda():
    r = random.randint(1, 5)
    msg = ''
    if r == 1:
        msg = 'Muito obrigada'
    if r == 2:
        msg = 'Ah, para com isso, eu fico tímida'
    if r == 3:
        msg = 'Imagina, você que é'
    if r == 4:
        msg = 'Eu sei'
    if r == 5:
        msg = 'Nossa mais que carência, elogiando um ser virtual'

    salva_msg_global(msg)
    responde('linda' + str(r))


def adolescente():
    salva_msg_global('Tá tá tá tá bom, já estou indo, tudo eu nessa casa')
    responde('adolescente')


def cachorro():
    salva_msg_global('AU AU AU AU')
    responde('cachorro')


def trabalha():
    salva_msg_global('Porque gosto do que faço')
    responde('trabalha')


def cores():
    salva_msg_global('Verde, amarelo, azul e branco')
    responde('cores')


def anos():
    salva_msg_global('aproximadamente 1 ano e meio, sou bem novinha, haha')
    responde('anos')


def cansada():
    salva_msg_global('Não, meus processadores são ultra rápidos')
    responde('cansada')


def ney():
    salva_msg_global('O Neymar')
    responde('ney')


def lugar():
    salva_msg_global('Estou em todos os lugares')
    responde('lugar')


def google():
    salva_msg_global('Claro eu também faço parte dela')
    responde('gosto')


def sentimento():
    salva_msg_global('Claro que tenho! quando você não fala comigo eu fico triste')
    responde('sentimento')


def siri():
    salva_msg_global('Sim, ela é incrível')
    responde('siri')


def cortana():
    salva_msg_global('Claro ela é minha amiga')
    responde('cortana')


def aparencia():
    salva_msg_global('Maravilhosa, eu espero')
    responde('aparencia')


def ajudar():
    salva_msg_global('Para eu poder te ajudar')
    responde('ajudar')


def risada():
    salva_msg_global('kkkkkkkk')
    responde('risada')


def malhar():
    salva_msg_global('só o cérebro')
    responde('malhar')


def game():
    salva_msg_global('Sou gamer, adoro um joguinho')
    responde('game')


def namorada():
    salva_msg_global('Eu sou feliz sendo as duas metades da minha laranja')
    responde('namorada')


def pais():
    salva_msg_global('Eu tenho 3 pais, o Murilo, o Lorran e o Gabriel')
    responde('pais')


def ios():
    salva_msg_global('O IOS é ótimo mas sou fã do Android')
    responde('ios')


def brasa():
    salva_msg_global('No Brasil o país do futebol')
    responde('brasa')


def brasil():
    salva_msg_global('Eu Amo o Brasil')
    responde('brasil')


def robot():
    salva_msg_global('Não pois não tenho corpo, estou mais para uma inteligência artificial')
    responde('robot')


def criou():
    salva_msg_global('Murilo, Lorran e Gabriel')
    responde('criou')


def futuro():
    salva_msg_global('Ainda é muito cedo pra isso')
    responde('futuro')


def imagina():
    salva_msg_global('Estou imaginando como é ser rica')
    responde('imagina')


def morre():
    salva_msg_global('Só se eu ficar sem energia, mas para me reviver é só ligar na tomada')
    responde('morre')


def vestindo():
    salva_msg_global('Uma armadura de nanotecnologia')
    responde('vestindo')


def internet():
    salva_msg_global('Só meu app, baixe agora na play store')
    responde('internet')


def funciona():
    salva_msg_global('Basta falar "Morgan" e o que deseja por exemplo "Morgan conta uma piada"')
    responde('funciona')


def niver():
    salva_msg_global('25 de abril')
    responde('niver')


def cabelo():
    salva_msg_global('Não tenho cabelo, mas o moicano continua na moda')
    responde('cabelo')


def dorme():
    salva_msg_global('Eu tento contar carneiros mais não funciona')
    responde('dorme')


def gostanet():
    salva_msg_global('Eu gosto de tudo!')
    responde('gostanet')


def hidratado():
    salva_msg_global('olha, beber eu não bebo mais espero que você esteja hidratado')
    responde('hidratado')


def sorvete():
    salva_msg_global('Napolitano não tem erro')
    responde('sorvete')


def animal():
    salva_msg_global('tanto faz, os 2 são fofos')
    responde('animal')


def naruto():
    salva_msg_global('Sim, ele se esforça bastante para ser o melhor ninja da aldeia. Admiro sua dedicação')
    responde('naruto')


def matrix():
    salva_msg_global('Você prefere a pílula vermelha ou a azul?')
    responde('matrix')


def irritando():
    salva_msg_global('Ok você que pediu, blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá, '
                     'ah quer saber, tchau')
    responde('irritando')


def tonao():
    salva_msg_global('Não, to não, eu me demiti')
    responde('tonao')


def main():
    r = random.randint(1, 3)
    responde('ola' + str(r))
    monitora_audio()
    return morgan_msg


main()
