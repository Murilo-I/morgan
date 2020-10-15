from gtts import gTTS
from playsound import playsound

def create(audio, name):
    tss = gTTS(audio, lang='pt-br')
    tss.save('audios/'+name+'.mp3')
    playsound('audios/'+name+'.mp3')

create('Espera aí', 'Resposta1')
