import os
#---Calculando o primeiro dígito do CPF---#
while True:
    cpf = input('Digite o CPF (APENAS NÚMEROS): ')
    cpf_int = []
    
    if cpf.isalnum() and len(cpf) == 11: 
        for i in cpf: # adicionar em uma lista como int, por int não ser iterável
            i = int(i)
            cpf_int.append(i)

    else: # caso não esteja no padrão
        os.system('cls')
        print('Apenas números\n')
        continue
    
    break

#---Multiplica os 9 primeiros em contagem regressiva de 10 e soma os resultados---#
indice, soma_dos_resultados = 0, 0

for i in range(10,1,-1):
    soma_dos_resultados += cpf_int[indice] * i
    indice += 1

#---Multiplica a soma por 10 e faz o módulo desse resultado---#
resto_da_soma = (soma_dos_resultados * 10) % 11
primeiro_digito = 0 if resto_da_soma > 9 else resto_da_soma  # segue a regra de Se > 9 = 0 , do contrário será o próprio valor

print(primeiro_digito)