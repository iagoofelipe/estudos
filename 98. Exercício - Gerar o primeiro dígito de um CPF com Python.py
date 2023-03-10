#---Calculando o primeiro dígito do CPF---#
while True:
    cpf = input('Digite o CPF (000.000.000-00): ')
    
    try:
        if cpf[3] == cpf[7] == "." and cpf[11] == "-":
            cpf_sem_ponto = ''.join(cpf.split("."))
            cpf = ''.join(cpf_sem_ponto.split("-"))
            cpf = int(cpf)
    except:
        ...    

    print(cpf)



#coletar CPF e somar os 9 primeiros dígitos
#multiplicar em contagem regressiva de 10
#somar resultados e multiplicar por 10
#módulo de 11, se resto > 9   0  do contrário __self__
