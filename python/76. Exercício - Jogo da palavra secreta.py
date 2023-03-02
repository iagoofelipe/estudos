palavra_secreta = 'perfume'
# contagem = 0
palavra_saida = '*' * len(palavra_secreta)

# while True:
#     letra_digitada = input('Digite uma letra: ').lower()

#     if len(letra_digitada) !=  1:
#         print('\nDigite apenas uma letra!')
#         continue

#     if letra_digitada in palavra_secreta:
#         for letra in palavra_secreta:
        
#             if letra == letra_digitada:
#                 palavra_saida += letra
#             else:
#                 palavra_saida += '*'
        
#     contagem += 1

#     print(f'Tentativas: {contagem}\n')

#     if palavra_saida == '*' * letra_digitada.count(''):
#         print('uhuu, fim :3')
#         break

"""

adivinhar palavra secreta, digitar uma letra
se != 1    não aceitar, 

"""
letra_out = 'u'
posicao = 0

for letra in palavra_secreta:
    if letra_out == letra:
        palavra_saida = f'{"*" * posicao}letra_out{"*" * (len(palavra_secreta) - posicao)}'

    posicao += 1
