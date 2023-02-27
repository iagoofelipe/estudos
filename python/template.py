frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
letra_maior, qtd_letra_maior = str, 0

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra_atual = frase.count(letra_atual)
    i += 1

    if letra_atual == ' ':
        continue

    if qtd_letra_atual > qtd_letra_maior:
        qtd_letra_maior = qtd_letra_atual
        letra_maior = letra_atual


print(f'A letra que mais aparece é "{letra_maior}", com {qtd_letra_maior} repetições')