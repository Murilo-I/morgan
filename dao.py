from models import Usuario
from flask import flash
import bcrypt

SQL_USUARIO_POR_ID = 'SELECT username, email, senha from usuario where username = %s'
SQL_USUARIO_POR_EMAIL = 'SELECT username, email, senha from usuario where email = %s'
SQL_ATUALIZA_SENHA = 'UPDATE usuario SET senha=%s where username = %s'
SQL_CRIA_USUARIO = 'INSERT into usuario (username, email, senha) values (%s, %s, %s)'


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, user, eh_cadastrado):
        cursor = self.__db.connection.cursor()
        senha = user.senha
        encript = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
        if eh_cadastrado:
            cursor.execute(SQL_ATUALIZA_SENHA, (encript, user.id))
            flash('Senha alterada com sucesso!')
        else:
            try:
                cursor.execute(SQL_CRIA_USUARIO, (user.id, user.email, encript))
                flash(user.id + ' cadastrado com sucesso!')
            except:
                flash('Username ou email já cadastrado')
        self.__db.connection.commit()

    def buscar_por_id(self, user_id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, [user_id])
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    def busca_por_email(self, user_email):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_EMAIL, [user_email])
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
