from gtts import gTTS
from playsound import playsound

def create(audio, name):
    tss = gTTS(audio, lang='pt-br')
    tss.save('audios/'+name+'.mp3')
    playsound('audios/'+name+'.mp3')

create('o lugar naturalmente mais perigoso da terra é o vale da morte, um deserto com temperatura média de 57° na Califórnia', 'Curiosidade3')

