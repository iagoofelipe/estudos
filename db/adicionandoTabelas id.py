import pymysql

#Conexão com servidor
conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database= 'twdbd'
    )

cursor = conexao.cursor()
cursor.execute(f"CREATE TABLE comalexandria(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), arma VARCHAR(255))")

