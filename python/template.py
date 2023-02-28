
db_local = {
    0 : ['IAGO','123456','iago@gmail.com'],
}

def menu():
    print('Bem-vindo a sua agenda'.center(50))
    print('','1 - Adicionar contato', '2 - Verificar/consultar contato','', sep='\n')
    while True:
        try:
            opcao = int(input('Escolha a opção desejada: '))
            if opcao not in (range(1,3)):
                raise ValueError
        
        except ValueError:
            print('Digite uma opção válida\n')
            continue
        else:
            return opcao
            break

# adicionar contato
def adicionar():
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')


# verificar existentes (consultar)
def verificar(nome=None):
    if nome == None:
        nome = input('Digite o nome: ').upper()
    
    if nome in db_local.keys():
        print('entrou ein')

# atualizar

#---iniciando menu---#
while True:
    print('-'*50)
    menu_resposta = menu()
    if menu_resposta == 1:
        verificar()

    opcao_retornar = input('\nDeseja retornar ao menu inicial [S/N]?').lower()
    
    if opcao_retornar == 's':
        continue
    
    else:
        break
