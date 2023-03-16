import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd=''
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE twdbd')

com_sql = 'INSERT comalexandria(nome,arma) VALUES(%s,%s)'
valor = ''

cursor.execute(com_sql, valor)