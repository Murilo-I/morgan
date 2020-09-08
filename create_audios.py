from gtts import gTTS

tss = gTTS('Olá, meu nome é Morgan', lang='pt-br')
tss.save('audios/hello.mp3')