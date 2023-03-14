import pymysql

#Conexão com servidor
conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database= 'twdbd'
    )

cursor = conexao.cursor()
cursor.execute("CREATE TABLE tabela1(nome VARCHAR(255),arma VARCHAR(255))")