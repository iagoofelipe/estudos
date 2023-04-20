import os, sys

# calculo primeiro dígito
posicao_cpf, soma_primeiro_digito = 0, 0
# pegar números do cpf (somente números)
while True:
    try:
        cpf_str = '11111111111'#'12314276043'
        # cpf_str = input("Digite o cpf (somente números): ")
        cpf_int = int(cpf_str)
        break

    except ValueError:
        os.system("cls")
        print("Somente números!\n")

primeiro_numero_repetido = cpf_str == cpf_str[0] * len(cpf_str)

if primeiro_numero_repetido:
    print(f"Sequencial de números detectado. CPF '{cpf_str}' inválido!")
    sys.exit()

# multiplicar cada um dos 9 primeiros dígitos do cpf em contagem regressiva de 10 e multiplicar por 10 soma total final
for i in range(10,1,-1):
    
    digito = int(cpf_str[posicao_cpf])
    soma_primeiro_digito += digito * i * 10
    posicao_cpf += 1 

# obter resto da divisão da conta por 11
resto_divisao = soma_primeiro_digito % 11
resultado_primeiro = 0 if resto_divisao >= 9 else resto_divisao




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


cpf_gerado = f"{cpf_str[:9]}{resultado_primeiro}{resultado_segundo}"


if cpf_gerado == cpf_str:
    print(f"CPF {cpf_str} válido") 

else:
    print("CPF inválido")



