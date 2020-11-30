from gtts import gTTS
from playsound import playsound


def create(audio, name):
    tss = gTTS(audio, lang='pt-br')
    tss.save('audios/' + name + '.mp3')
    playsound('audios/' + name + '.mp3')


create('O que o próton disse para o elétron ? Hoje você está muito negativo', 'Piada1')
create('o que o tomate foi fazer no banco, tirar extrato.', 'Piada2')
create('qual a tecla preferida do astronauta, a barra de espaço', 'Piada3')
create('você sabia que júpiter e o maior e mais radioativo planeta do sistema solar', 'Curiosidade1')
create('o local mais fundo do planeta terra é as fossas das marianas, com cerca de 11km de profundidade',
       'Curiosidade2')
create('o lugar naturalmente mais perigoso da terra é o vale da morte, um deserto com temperatura média de 57° na '
       'Califórnia', 'Curiosidade3')
create('Um momento', 'Resposta1')
create('Não sou paga para isso', 'Resposta2')
create('Não posso te ajudar com isso', 'Resposta3')
create('Alarme definido', 'Resposta4')
