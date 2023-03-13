import os
#---Calculando o primeiro dígito do CPF---#
while True:
    cpf = '74483897004'#input('Digite o CPF (APENAS NÚMEROS): ')
    
    if not cpf.isalnum() or len(cpf) != 11:
        os.system('cls')
        print('Apenas números\n')
        continue
    
    nove_digitos, soma, contagem = cpf[:9], 0, 10
    
    for digito in nove_digitos:
        soma += int(digito) * contagem * 10
        contagem -= 1

    break
modulo = soma % 11
primeiro_digito = 0 if modulo > 9 else modulo  # segue a regra de Se > 9 = 0 , do contrário será o próprio valor

print(primeiro_digito)