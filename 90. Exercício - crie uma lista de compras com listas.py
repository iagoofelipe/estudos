import os
lista = ['banana','maçã','tomate']
#---lista de compras---#
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opcao not in ('i','a','l','s'):
        os.system('cls')
        print('Opção inválida!\n')
        continue

    if opcao == 'i':
        inserir = input('\nValor: ')
        lista.append(inserir)
        os.system('cls')
        print('Valor inserido com sucesso!\n')
    
    elif opcao == 'a':
        while True:
            try:
                indice_apagar = int(input('\nÍndice a ser apagado: '))
                lista.pop(indice_apagar)
                os.system('cls')
                print(f'Valor de índice {indice_apagar} apagado!\n')
                break
                
            except ValueError:
                os.system('cls')
                print('Apenas números inteiros são aceitos!')
                continue
            
            except IndexError:
                os.system('cls')
                print(f'Índice {indice_apagar} não encontrado!\n')
                break

    elif opcao == 'l':
        if lista:
            os.system('cls')
            print('LISTA'.center(50,'-'))
            for indice, valor in enumerate(lista):
                print('-', indice, valor)
            print('-' * 50, '\n')
    
    elif opcao == 's':
        os.system('cls')
        print('LISTA'.center(50,'-'))
        
        for indice, valor in enumerate(lista):
            print('-', indice, valor)
        
        print('-' * 50, '\n')
        print('Finalizado')
        break