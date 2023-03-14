import pymysql

#Conexão com servidor
def createdb(listin=list):
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database= 'twdbd'
    )

    for dbname in listin:
        cursor = conexao.cursor()
        cursor.execute(f"CREATE TABLE {dbname}(nome VARCHAR(255),arma VARCHAR(255))")

createdb(listin=['comhilltop','comreino','comsalvadores'])