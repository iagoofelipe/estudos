import pymysql

#Conexão com servidor

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database= 'twdbd'
)

cursor = conexao.cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

