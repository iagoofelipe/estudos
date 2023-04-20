import random

# calculo primeiro dígito
cpf_str, posicao_cpf, soma_primeiro_digito = '', 0, 0


# multiplicar cada um dos 9 primeiros dígitos do cpf em contagem regressiva de 10 e multiplicar por 10 soma total final
for i in range(10,1,-1):
    
    digito = random.randint(0,9)
    cpf_str += str(digito)

    soma_primeiro_digito += digito * i * 10
    posicao_cpf += 1 

# obter resto da divisão da conta por 11
resto_divisao = soma_primeiro_digito % 11
resultado_primeiro = 0 if resto_divisao >= 9 else resto_divisao
cpf_str += str(resultado_primeiro)


# calculo segundo dígito
posicao_cpf, soma_segundo_digito = 0, 0
# multiplicar cada um dos 10 primeiros dígitos do cpf em contagem regressiva de 11 e multiplicar por 10 soma total final
for i in range(11,1,-1):
    
    digito = int(cpf_str[posicao_cpf])
    soma_segundo_digito += digito * i * 10
    posicao_cpf += 1 

# obter resto da divisão da conta por 11
resto_divisao = soma_segundo_digito % 11
resultado_segundo = 0 if resto_divisao >= 9 else resto_divisao
cpf_str += str(resultado_segundo)


cpf_gerado = f"{cpf_str[:9]}{resultado_primeiro}{resultado_segundo}"


if cpf_gerado == cpf_str:
    print(f"CPF {cpf_str} válido") 

else:
    print("CPF inválido")

