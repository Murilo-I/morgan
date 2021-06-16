from gtts import gTTS
from playsound import playsound


def create(audio, name):
    tss = gTTS(audio, lang='pt-br')
    tss.save('audios/' + name + '.mp3')
    playsound('audios/' + name + '.mp3')


create('Estou pronta', 'ola1')
create('Como posso te ajudar?', 'ola2')
create('Você me chamou?', 'ola3')
create('Um momento', 'Resposta1')
create('Não sou paga para isso', 'Resposta2')
create('Não posso te ajudar com isso', 'Resposta3')
create('Desculpa, poderia repetir', 'naoEntendi1')
create('repete aí que eu não entendi', 'naoEntendi2')
create('Tava jogando, o que você disse mesmo', 'naoEntendi3')
create('Desculpa, não entendi o que você falou', 'naoEntendi4')
create('Oi? fala de novo', 'naoEntendi5')
