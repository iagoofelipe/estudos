from mysql.connector import connect

# conexao = connect(
#     host='localhost',
#     user='root',
#     # database='bdyoutube'
# )

# cursor = conexao.cursor()
# # comando = f'SELECT * FROM bdyoutube.vendas'
# comando = f'INSERT INTO bdyoutube.vendas (nome_produto, valor) VALUES ("morangos", 20)'

# print(cursor.rowcount)
# cursor.execute(comando)

# resultado = cursor.fetchall()
# print(resultado)


# class Database:
#     def __init__(self, db) -> None:
#         self.__conexao = connect(host='localhost', user='root')
#         self.__cursor = self.__conexao.cursor()
#         self.__db = db


#     def insert(self, table, **kwargs):
#         keys, values = '', ''

#         for __keys, __values in kwargs.items():
#             if type(__keys) == int:
#                 __keys = str(__keys)

#             if type(__values) == str:
#                 __values = f'"{__values}"'

#             elif type(__values) == int:
#                 __values = str(__values)

#             keys += __keys + ', '
#             values += __values + ', '

#         command = f'INSERT INTO {self.__db}.{table} ({keys[:-2]}) VALUES ({values[:-2]})'
#         print(command)
#         # self.__cursor.execute(command)


#     def set_db(self, __value):
#         """ defindino valor para db """
#         self.__db = __value

#     @property
#     def db(self):
#         """ nome de db selecionado """
#         return self.__db
    

# db = Database('bdyoutube')
# db.insert('vendas', nome_produto="chocolate1", valor = 15)


conexao = connect(
    host='localhost',
    user='root',
    # database='bdyoutube'
)
cursor = conexao.cursor()
cursor.execute('INSERT INTO bdyoutube.vendas (nome_produto, valor) VALUES ("chocolate3", 15)')