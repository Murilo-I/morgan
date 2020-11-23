from gtts import gTTS
from playsound import playsound


def create(audio, name):
    tss = gTTS(audio, lang='pt-br')
    tss.save('audios/' + name + '.mp3')
    playsound('audios/' + name + '.mp3')


create('O que o próton disse para o elétron ? Hoje você está muito negativo', 'Piada1')
