from gtts import gTTS

tss = gTTS('Olá, meu nome é Morgan, tudo bom com você?', lang='pt-br')
tss.save('audios/hello.mp3')
