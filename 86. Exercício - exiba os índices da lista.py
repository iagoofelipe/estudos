lista, contagem = ['Iago', 'Marta',1,2,3,4, 'Pedro'], 0

# for item in lista:
#     print(f'índice: {contagem} item: {item}')
#     contagem += 1

# lista_enumerada = list(enumerate(lista))
# for i in lista_enumerada:
#     print(i[0], i[1])

for indice, nome in enumerate(lista):
    print(indice, nome)