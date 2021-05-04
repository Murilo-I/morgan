# Morgan
## Virtual Assistant


Projeto desenvolvido e testado no **python 3.6** (alguns módulos só funcionam nessa versão). 

Este projeto é uma assistente virtual, e foi feita utilizando as APIs do Google GTTS e a SpeechRecognition, por ter sido desenvolvida num sistema operaciconal **Windows**, usamos as bibliotecas **playsound** e pyaudio para reproduzirmos as respostas da Morgan. Em casos de sistemas **IOS/Linux**, é preciso substituir o playsound pelo **subprocess**. 
Além de funcionar no console através do arquivo Morgan.py, ao rodar o arquivo web_morgan.py, um servidor local em flask irá subir na porta 5000 do seu computador. As páginas são responsivas e são duas principais, a index.html por onde você irá chamar a Morgan através do click no botão microfone que aparecerá na tela, e a tela de login e suas variante como cadastro e troca de senha.

O banco de dados usado é o Mysql, para tal a biblioteca flask_mysqldb foi utilizada. Apoós **configurar seu usuário e senha** nos arquivos web_morgan.py e prepara_banco.py, basta **rodar o prepara_banco** que o um banco de dados será criado e 3 usuários serão inseridos.

Após isso basta se divertir conversando com a Morgan, e em caso do porquê a Morgan, e não a Alexa, a Siri ou a própria Google a qual esta serviu de base. A Morgan conta com respostas originais, tem que ouvir para descobrir.

###### PS.: Este README é só um início, a assistente ainda está sendo desenvolvida e em breve estará funcionando plenamente, com uma versão de chat mobile([mobile_morgan](https://github.com/Murilo-I/mobile_morgan.git)) e uma melhor documentação.
