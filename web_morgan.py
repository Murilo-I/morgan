from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL
from models import Usuario
from daos import UsuarioDao

# CONFIGURAÇÕES #

app = Flask(__name__)
app.secret_key = 'MORGAN'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Mysql8018"
app.config['MYSQL_DB'] = "morgan"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
dao = UsuarioDao(db)


# INTEGRAÇÃO WEB #

@app.route('/')
def naweb():
    return redirect(url_for('index'))


@app.route('/morgan_assistant')
def index():
    return render_template('aboutus.html')


@app.route('/morgan_assistant/registrar')
def registrar():
    return render_template('cadastro.html')


@app.route('/morgan_assistant/criar', methods=['POST'])
def criar():
    username = request.form['username']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(username, email, senha)
    eh_cadastrado = request.form.get('cadastrado')
    dao.salvar(usuario, eh_cadastrado)
    return redirect(url_for('index'))


@app.route('/morgan_assistant/login')
def login():
    proxima_pagina = request.args.get('logado')
    return render_template('login.html', logado=proxima_pagina)


@app.route('/morgan_assistant/autenticar', methods=['POST'])
def autenticar():
    usuario = dao.buscar_por_id(request.form['username'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.id + ' logou com sucesso!')
            proxima_pagina = request.form['logado']
            return redirect(proxima_pagina)
    else:
        flash('Falha no login, tente novamente!')
        return redirect(url_for('login'))


@app.route('/morgan_assistant/mudar_senha')
def mudar_senha():
    return render_template('alteracaosenha.html')


app.run(debug=True)