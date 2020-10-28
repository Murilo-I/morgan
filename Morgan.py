import speech_recognition as sr
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
from gtts import gTTS
import random
import webbrowser as browser

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
    print('Morgan' + mensagem)
    playsound('audios/mensagem.mp3')


def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()

    elif 'toca' in trigger and 'eletronica' in trigger:
        playlists('eletronica')

    elif 'toca' in trigger and 'funk' in trigger:
        playlists('funk')

    elif 'toca' in trigger and 'sertanejo' in trigger:
        playlists('sertanejo')

    elif 'toca' in trigger and 'rock' in trigger:
        playlists('rock')

    elif 'toca' in trigger and 'rap' in trigger:
        playlists('rap')

    elif 'toca' in trigger and 'pop smoke' in trigger:
        playlists('pop smoke')

    elif 'toca' in trigger and 'post malone' in trigger:
        playlists('post malone')

    elif 'toca' in trigger and 'kevinho' in trigger:
        playlists('kevinho')

    elif 'toca' in trigger and 'luan santana' in trigger:
        playlists('luan santana')

    elif 'toca' in trigger and 'marshmello' in trigger:
        playlists('marshmello')

    elif 'toca' in trigger and 'eminem' in trigger:
        playlists('eminem')

    elif 'toca' in trigger and 'wesley safadão' in trigger:
        playlists('wesley safadão')

    elif 'toca' in trigger and 'mc livinho' in trigger:
        playlists('mc livinho')

    elif 'toca' in trigger and 'ed sheeran' in trigger:
        playlists('ed sheeran')

    elif 'toca' in trigger and 'shawn mendes' in trigger:
        playlists('shawn mendes')

    elif 'toca' in trigger and 'samba' in trigger:
        playlists('samba')

    elif 'toca' in trigger and 'pagode' in trigger:
        playlists('pagode')


    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('Comando inválido:', mensagem)
        r = random.randint(2, 3)
        responde('Resposta' + str(r))


# FUNÇÕES COMANDOS #

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&g=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    manchetes = []
    for item in noticias.findAll('item')[:9]:
        manchetes.append(item)

    r = random.randint(0, 9)
    mensagem = manchetes[r].title.text
    cria_audio(mensagem)


def playlists(album):
    if album == 'pop smoke':
        browser.open('https://www.youtube.com/watch?v=Q9pjm4cNsfc&list=PLrqfOeU4oaWzrCWvuyju4wuGjaJ0N5L3A&index=1')

    if album == 'eletronica':
        browser.open('https://www.youtube.com/watch?v=2zToEPpFEN8&list=PL_Q15fKxrBb5d4FzxegXGGkW2eAgtukpi&index=1')

    if album == 'funk':
        browser.open('https://www.youtube.com/watch?v=Tun92VU2OkU&list=PLCwAHfhr-Gc82BO57__8Y-wEvZz8ytlHG&index=1')

    if album == 'sertanejo':
        browser.open('https://www.youtube.com/watch?v=M76qUQTt_Sw&list=RDQMaN3fxIo2Kwk&index=1')

    if album == 'rock':
        browser.open('https://www.youtube.com/watch?v=kXYiU_JCYtU&list=PLZ1dJqY6KWOXGGeIlZqleztqta23wHMGG&index=1')

    if album == 'rap':
        browser.open('https://www.youtube.com/watch?v=JFm7YDVlqnI&list=PL-FVH5VWgRPHNz24zZ5_FLHQWoidN6O1d&index=1')

    if album == 'post malone':
        browser.open('https://www.youtube.com/watch?v=ApXoWvfEYVU&list=PLegvV8yC11jbsUdqKEkIazprdTm71fU1z&index=1')

    if album == 'kevinho':
        browser.open('https://www.youtube.com/watch?v=WAb1xxYzycw&list=PLbnysjjM_VIm3wMCA6_sBs5wkefVBTfG8&index=1')

    if album == 'luan santana':
        browser.open('https://www.youtube.com/watch?v=PcXtzbdCd-E&list=PL952uGL-ahB_MvfTLvExCr1nrLKsONuQQ&index=1')

    if album == 'marshmello':
        browser.open('https://www.youtube.com/watch?v=ALZHF5UqnU4&list=PLEMoDqX-7M9Ro8XuRRmprhNO2_4_rj7nP&index=1')

    if album == 'eminem':
        browser.open('https://www.youtube.com/watch?v=_Yhyp-_hX2s&list=PLC0w3lEHx2SEisFu76dsAC1JxqjWZOYr1&index=1')

    if album == 'wesley safadão':
        browser.open('https://www.youtube.com/watch?v=Jtler_CFqHI&list=PL92KYhulRUL9K3eITtBpqDPvb5hFa0Tx8&index=1')

    if album == 'mc livinho':
        browser.open('https://www.youtube.com/watch?v=Sn0wA_ERHVU&list=PL4dYBPEeVh609FNO7_0aLefydncIDdGHr&index=1')

    if album == 'ed sheeran':
        browser.open('https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLaq655wqcKDlaw569c2frEOlsF_S5HYZl&index=1')

    if album == 'shawn mendes':
        browser.open('https://www.youtube.com/watch?v=Pkh8UtuejGw&list=PLOYP-X0Ialymfu4X9sl4skhNRh8K2GoRz&index=1')

    if album == 'samba':
        browser.open('https://www.youtube.com/watch?v=eHSIhLG-Clw&list=PLfmShFzlmLLE0onNn2yxUP6VnHm-ufRIs&index=1')

    if album == 'pagode':
        browser.open('https://www.youtube.com/watch?v=c4XeTP11EI8&list=PLws-Q6lwJkI1jq4kJbugdcAJryK2u_vi1&index=1')


def main():
    while True:
        monitora_audio()


main()
