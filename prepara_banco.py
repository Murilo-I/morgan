import MySQLdb

conn = MySQLdb.connect(user='root', passwd='Mysql8024', host='127.0.0.1', port=3306)

# para desfazer o banco...
# conn.cursor().execute("DROP DATABASE `morgan`;")
# conn.commit()

criar_tabelas = '''SET NAMES latin1;
    CREATE DATABASE `morgan` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `morgan`;
    CREATE TABLE `usuario` (
      `username` varchar(55) COLLATE utf8_bin NOT NULL,
      `email` varchar(55) COLLATE utf8_bin NOT NULL UNIQUE,
      `senha` varchar(55) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`username`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO morgan.usuario (username, email, senha) VALUES (%s, %s, %s)',
      [
            ('marquês', 'marques@gmail.com', '12345678'),
            ('nicogamer', 'nicogamer@gmail.com', '12345678'),
            ('daniTheQueen', 'danisantos@gmail.com', '12345678')
      ])

cursor.execute('select * from morgan.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


# commitando senão nada tem efeito
conn.commit()
cursor.close()
