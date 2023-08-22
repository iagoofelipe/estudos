from mysql.connector import connect

#Conexão com servidor
def createdb(listin=list):
    conexao = connect(
        host = 'localhost',
        user = 'root',
        database= 'twdbd'
    )

    for dbname in listin:
        cursor = conexao.cursor()
        cursor.execute(f"CREATE TABLE {dbname} (nome VARCHAR(255),arma VARCHAR(255))")
    
    conexao.commit()

createdb(listin=['comhilltop','comreino','comsalvadores'])