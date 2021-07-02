from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL
from models import Usuario
from daos import UsuarioDao
# from Morgan import main

# CONFIGURAÇÕES #

app = Flask(__name__)
app.secret_key = 'MORGAN'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Mysql8024"
app.config['MYSQL_DB'] = "morgan"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
dao = UsuarioDao(db)

msgs = []


# INTEGRAÇÃO WEB #


@app.route('/')
def naweb():
    return redirect(url_for('index'))


@app.route('/morgan_assistant')
def index():
    return render_template('index.html', mensagens=msgs)


@app.route('/morgan_assistant/registrar')
def registrar():
    form = ValidaFormulario(request.form)
    return render_template('cadastro.html', form=form)


@app.route('/morgan_assistant/criar', methods=['POST'])
def criar():
    form = ValidaFormulario(request.form)

    if form.validate():
        usuario = Usuario(form.username.data, form.email.data, form.senha.data)
        dao.salvar(usuario, None)
        return redirect(url_for('index'))


@app.route('/morgan_assistant/atualizar', methods=['POST'])
def atualizar():
    usuario = Usuario(request.form['username'], request.form['email'], request.form['senha'])
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


@app.route('/morgan_assistant/funcionalidades')
def funcionalidades():
    return render_template('funcionalidades.html')


@app.route('/morgan_assistant/rodar')
def rodar():
    # main()
    # msg = main()
    # msgs.append(msg)
    return redirect(url_for('index'))


app.run(debug=True)
