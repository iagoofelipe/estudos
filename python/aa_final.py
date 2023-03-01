#variáveis e funções que serão utilizadas por todo o código e entre funções

contatos = {}
resposta_s_n = ['s', 'n', 'Sim', 'Nao', 'S', 'N']
resposta_s = ['s', 'Sim', 'S']
resposta_n = ['n', 'Nao', 'N']

def resposta_sim_nao(resposta):
  while resposta not in resposta_s_n:
    print('\nDigite "S" para sim e "N" para não!')
    resposta = input('(S/N): ')
  
  resposta_loop = resposta
  return resposta_loop

def menu_inicial():

  """essa é a função do menu inicial do programa, onde o usuário encontra as opções e
  é direcionado para as demais funcionalidades do mesmo"""
  
  print('-'*44,end='\n')
  print(f'{"Bem-vindo a sua agenda telefônica!":^44}', end='\n')
  print('\n1 - NOVO CONTATO', '2 - CONSULTAR CONTATO',
        '3 - ATUALIZAR CONTATO', '4 - REMOVER CONTATO',
        '5 - RELATÓRIO\n', sep="\n")
  
  opcao_menu = eval(input('Digite o número da opção escolhida: '))
  opcoes = [1,2,3,4,5]
  
  while opcao_menu not in opcoes:
    print('\nOpção inválida!')
    opcao_menu = eval(input('Digite o número da opção escolhida: '))

  return opcao_menu

def consultar_contato():
  print('-'*44,end='\n')
  
  """essa função serve para consultar o contato com o nome, gerando um relatório na 
  tela com os contatos encontrados a partir do nome digitado"""
    
  nome = input('Digite o nome: ')
  resultado_consulta = False

  for i in contatos:
    if nome == contatos[i][0]:
      resultado_consulta = True

  for indice, i in enumerate(contatos):
    if indice == 0 and resultado_consulta == True:
      print('-'*111, end='\n')
      print("Chave"+f'{"Nome":>11}{"Telefone":>20}{"E-mail":>25}{"Twitter":>25}{"Instagram":>25}')
      print()
    
    if nome == contatos[i][0]:
      print(str(i)+'{0:>15}{1:>20}{2:>25}{3:>25}{4:>25}'.format(*contatos[i]))
    
    if i == list(contatos.keys())[-1] and resultado_consulta == True:
      print('-'*111)
      

  return nome, resultado_consulta

def adicionar_contato():
  
  """essa função serve para adicionar um novo contato, a qual consulta o nome digitado 
  pelo usuário e gera o relatório, permitindo a inclusão de contatos com o mesmo nome"""

  nome_resultado_consulta = consultar_contato()
  
  nome = nome_resultado_consulta[0]
  resultado_consulta = nome_resultado_consulta[1]

  resposta_loop = 's'

  if resultado_consulta == True:
    resposta = input('\nDeseja criar um novo contato com o mesmo nome?(S/N): ')
    resposta_loop = resposta_sim_nao(resposta)

  if resposta_loop in resposta_s:
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')
    twitter = input('Digite o twitter: ')
    instagram = input('Digite o instagram: ')

    chave = len(contatos)+1
    lista_chaves = list(contatos.keys())
    
    while chave in lista_chaves:
      chave += 1

    contatos[chave] = [nome, telefone, email, twitter, instagram]

    print('\nContato salvo com êxito!')

def atualizar_contato():

  """essa função serve para atualizar os contatos, pesquisando e gerando o relatório na tela para
  o usuário escolher o desejado"""

  resultado_consulta = consultar_contato()
  if resultado_consulta[1] == True:
    chave = int(input('Digite a chave do contato que deseja atualizar (para cancelar, digite 0): '))
    while chave not in contatos.keys() and chave != 0:
      print('\nDigite uma chave válida!')
      chave = int(input('Digite a chave do contato que deseja atualizar (para cancelar, digite 0): '))
  
  if chave == 0 or resultado_consulta[1] == False:
    if resultado_consulta[1] == False:
      print('\nNenhum contato encontrado!')
    print('\nOperação cancelada com êxito!')
  
  elif resultado_consulta[1] == True and chave in contatos.keys():
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o e-mail: ')
    twitter = input('Digite o twitter: ')
    instagram = input('Digite o instagram: ')

    contatos[chave] = [nome, telefone, email, twitter, instagram]
    print('\nContato atualizado com sucesso!')

def remover_contato():

  """essa função serve para remover um contato previamente cadastrado, a qual consulta
  através de outra função e retorna o resultado, que é utilizado como parâmetro para as
  demais funcionalidades"""

  resultado_consulta = consultar_contato()
  
  if resultado_consulta[1] == True:
    chave = int(input('Digite a chave do contato para a remoção (para cancelar, digite 0): '))
    while chave not in contatos.keys() and chave != 0:
      print('\nDigite uma chave válida!')
      chave = int(input('Digite a chave do contato para a remoção (para cancelar, digite 0): '))
  
  if chave == 0 or resultado_consulta[1] == False:
    if resultado_consulta[1] == False:
      print('\nNenhum contato encontrado!')
    print('\nRemoção cancelada com êxito!')
  
  elif resultado_consulta[1] == True and chave in contatos.keys():
    contatos.pop(chave)
    print('\nContato removido com sucesso!')

def relatorio():
  """essa função serve para gerar o relatório dos contatos e informações cadastradas,
  imprimindo na tela, após o primeiro laço for, estão as linhas de código para a geração
  do relatório em arquivo .txt"""

  for indice, i in enumerate(contatos):
    if indice == 0:
      print('-'*111, end='\n')
      print("Chave"+f'{"Nome":>11}{"Telefone":>20}{"E-mail":>25}{"Twitter":>25}{"Instagram":>25}')
      print()
    print(str(i)+'{0:>15}{1:>20}{2:>25}{3:>25}{4:>25}'.format(*contatos[i]))
    if i == list(contatos.keys())[-1]:
      print('-'*111)

  #relatório gerado quando a função é executada, a qual gera o .txt com os contatos cadastrados
  with open('relatorio.txt', 'w') as txt:
    for i in contatos:
      txt.write("{0}, {1}, {2}, {3}, {4}\n".format(*contatos[i]))

  #relatório gerado quando a função é executada, a qual gera o .txt com os contatos cadastrados de forma
  #mais organizada
  with open('relatorioEstruturado.txt', 'w') as txt:
    for indice, i in enumerate(contatos):
      if indice == 0:
        txt.write('-'*111)
        txt.write("\nChave"+f'{"Nome":>11}{"Telefone":>20}{"E-mail":>25}{"Twitter":>25}{"Instagram":>25}')
        txt.write('\n')
      txt.write('\n'+str(i)+'{0:>15}{1:>20}{2:>25}{3:>25}{4:>25}'.format(*contatos[i]))
      if i == list(contatos.keys())[-1]:
        txt.write('\n'+'-'*111)

def adicionar_mult_contatos():
  qte = int(input('\nDigite a quantidade de contatos a serem adicionados: '))
  for i in range(qte):
    adicionar_contato()

"""essa parte serve para permitir a interação entre as funções do programa e o menu inicial"""

while True:
  opcao_menu = menu_inicial()

  if len(contatos.keys()) == 0 and opcao_menu != 1:
    print('-'*44)
    print('\nNenhum contato cadastrado!\n')
    print('-'*44)
  
  elif opcao_menu == 1:
    adicionar_mult_contatos()
  
  elif opcao_menu == 2:
    resultado_consulta = consultar_contato()
    if resultado_consulta[1] == False:
      print('\nContato não encontrado!')
  
  elif opcao_menu == 3:  
    atualizar_contato()
  
  elif opcao_menu == 4:
    remover_contato()
  
  elif opcao_menu == 5:
    relatorio()
  
  resposta = input('\nDeseja retornar ao menu inicial?(S/N): ')
  print()
  resposta_loop = resposta_sim_nao(resposta)
  
  if resposta_loop in resposta_s:
    continue
  elif resposta_loop in resposta_n:
    print('-'*44)    
    print('\nFim do programa! :)')
    print('-'*44)
    break