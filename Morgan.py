import speech_recognition as sr
from playsound import playsound
from requests import get
from bs4 import BeautifulSoup
from gtts import gTTS

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
                    print('Comando: ', trigger)
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Morgan could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return trigger

def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')

def cria_audio(mensagem):
    tss = gTTS(mensagem, lang='pt-br')
    tss.save('audios/mensagem.mp3')
    playsound('audios/mensagem.mp3')


def executa_comandos(trigger):
    if 'notícias' in (trigger):
        ultimas_noticias()

        # FUNÇÕES COMANDOS #

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&g=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item') [:1]:
        mensagem = item.title.text
        cria_audio(mensagem)

def main():
    while True:
        monitora_audio()

main()





