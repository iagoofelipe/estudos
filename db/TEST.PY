import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'twdbd'

)

cursor = conexao.cursor() 
cursor.execute('ALTER TABLE comsalvadores ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')