while True:
    try:
        print('-'*25,end='\n\n')
        
        #---coletando dados---#
        num_1 = float(input('Digite o primeiro número: '))
        num_2 = float(input('Digite o segundo número: '))
        operador = input('Escolha um operador (+-*/): ')
        resultado = None
        
        #---realizando cálculo---#
        if operador == '+':
            resultado = num_1 + num_2
        elif operador == '-':
            resultado = num_1 - num_2
        elif operador == '*':
            resultado = num_1 * num_2
        elif operador == '/':
            resultado = num_1 / num_2
        else:
            raise ValueError
        
        print(f'\nO resultado de {num_1} {operador} {num_2} = {resultado:.1f}\n')
        
    except:
        print('\nDigite apenas números e apenas um operador válido!\n')

    #---se continuar ou não---#
    resposta = input('deseja continuar (s)? ').lower().startswith('s')
    if resposta:
        continue
    else:
        print('-'*25,end='\n\n')
        break