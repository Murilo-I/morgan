import speech_recognition as sr


def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando Comando: ")
        audio = microfone.listen(source)

    try:
        print(microfone.recognize_google(audio, language="pt-BR"))
    except sr.UnknownValueError:
        print("Morgan could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


monitora_audio()
