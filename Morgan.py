import speech_recognition as sr
from playsound import playsound

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
                    responde('Resposta1')
                    # comandos a executar #
                    break

            except sr.UnknownValueError:
                print("Morgan could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return trigger

def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')

monitora_audio()



