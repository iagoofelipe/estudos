import os
cpf_int, indice, soma_resultados = [], 0, 0
#---Calculando o primeiro dígito do CPF---#
while True:
    cpf = input('Digite o CPF (000.000.000-00): ')
    
    try:
        se_no_padrao = cpf[3] == cpf[7] == "." and cpf[11] == "-" and len(cpf) == 14 # verificar se está no padrão 000.000.000-00
        
        if se_no_padrao: 
            cpf = cpf.replace('-','').replace('.','') # remove o "." e "-"
            
            for i in cpf: # adicionar em uma lista como int, por int não ser iterável
                i = int(i)
                cpf_int.append(i)

        else: # caso não esteja no padrão
            raise Exception('Fora do padrão')
        break

    except IndexError:
        os.system('cls')
        print('Fora do padrão (000.000.000-00)\n'.center(50))
        continue
    
    except ValueError:
        os.system('cls')
        print('Fora do padrão (000.000.000-00)\n'.center(50))
        continue

#---Multiplica os 9 primeiros em contagem regressiva de 10 e soma os resultados---#
for i in range(10,1,-1):
    soma_resultados += cpf_int[indice] * i
    indice += 1

#---Multiplica a soma por 10 e faz o módulo desse resultado---#
modulo_da_soma = (soma_resultados * 10) % 11
primeiro_digito = 0 if modulo_da_soma > 9 else modulo_da_soma  # segue a regra de Se > 9 = 0 , do contrário será o próprio valor

print(primeiro_digito)