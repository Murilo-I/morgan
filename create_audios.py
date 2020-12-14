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
create('Tá tá tá tá bom, já estou indo, tudo eu nessa casa', 'adolescente')
create('Ok você que pediu, blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá, ah quer saber tchau',
       'irritando')
create('Pedra', 'mao1')
create('Papel', 'mao2')
create('Tesoura', 'mao3')
create('Minha missão é criar a vacina não chinesa, do coronga', 'missao1')
create('Minha missão é saber construir no fortnite e no minecraft', 'missao2')
create('Minha missão é dominar o mundo junto com as minhas amigas siri, google e alexa', 'missao3')
