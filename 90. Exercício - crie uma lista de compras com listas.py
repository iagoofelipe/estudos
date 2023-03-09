import os
lista = []
#---lista de compras---#
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao not in ('i','a','l'):
        os.system('cls')
        print('Opção inválida')
        continue

    if opcao == 'i':
        inserir = input('\nValor: ')
        lista.append(inserir)
        os.system('cls')
    
    elif opcao == 'a':
        indices = range(len(lista))
        while True:
            try:
                indice_apagar = int(input('\nÍndice a ser apagado: '))
                
                if indice_apagar not in indices:
                    os.system('cls')
                    print('Índice não encontrado!')
                break

            except:
                os.system('cls')
                print('Apenas números inteiros são aceitos!')
                continue

    elif opcao == 'l':
        ...
        
