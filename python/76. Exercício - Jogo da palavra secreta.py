palavra_sec = 'perfume'
palavra_secreta, j = [], 0

for i in palavra_sec:
    palavra_secreta[j] = i
    j += 1
j = 0

tamanho_palavra = len(palavra_secreta)
palavra_digitada = '*' * tamanho_palavra

while True:
    letra_digitada = input('Digite uma letra: ')
    tamanho_letra_digitada = len(letra_digitada)

    if tamanho_letra_digitada > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        for i in palavra_secreta:
            if i == letra_digitada:
                palavra_secreta[j] = ''

