
db_local = {
    0 : ['IAGO','123456','iago@gmail.com'],
}

def menu():
    print('Bem-vindo a sua agenda'.center(50))
    print('','1 - Adicionar contato', '2 - Verificar/consultar contato','', sep='\n')
    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao not in (range(1,3)):
                raise ValueError
        
        except ValueError:
            print('Digite uma opção válida\n')
            continue
        else:
            return opcao
            break


# verificar existentes (consultar)
def verificar(nome=None):
    if nome == None:
        
        nome = input('Digite o parâmetro de pesquisa: ').upper()
    
    primeiro = True
    for i in db_local.values():
        if nome in i:
            
            if primeiro:
                print(f'{"nome":^20} {"telefone":^20} {"email":^20}')
                primeiro = False
                
            nome = i[0]
            telefone = i[1]
            email = i[2]
            print(f'{nome:>20} {telefone:>20} {email:>20}')
        
        else:
            print('Nenhuma correspondência ')



# adicionar contato
def adicionar():
    nome = input('Digite o nome: ').upper()
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ').upper()

    verificar(nome)

# atualizar

#---iniciando menu---#
while True:
    print('-'*50)
    menu_resposta = menu()

    print('-'*50)
    if menu_resposta == 1:
        adicionar()
    elif menu_resposta == 2:
        verificar()

    print('-'*50)
    opcao_retornar = input('\nDeseja retornar ao menu inicial [S/N]?').lower()
    
    if opcao_retornar == 's':
        continue
    
    else:
        print('-'*50)
        break
