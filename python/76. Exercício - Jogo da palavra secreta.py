import os

#---com o professor---#
def professor():    
    palavra_secreta = 'perfume'
    letras_acertadas, palavra_saida = '',''
    tentativas = 0

    while True:
        letra_digitada = input('Digite uma letra: ')
        
        if len(letra_digitada) != 1: # não aceitar mais de um caractere
            print('Digite apenas uma letra!\n')
            continue
        
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_saida += letra_secreta
            else:
                palavra_saida += '*'
        tentativas += 1

        print(palavra_saida, '\n')

        if '*' not in palavra_saida:
            os.system('cls')
            print('Parabéns!', f'Tentativas: {tentativas}', 
                  f'Palavra secreta: {palavra_saida}', sep='\n')
            break
        
        palavra_saida = ''



def eu():
    #---minha tentativa---#
    def to_list(string_list=str,to_str=False):
        
        """ retorna list (to_str=False) da palavra[1] e uma lista[0] com "*" para ser alterado
        retorna str (to_str=True) da palavra[1] e None[0] """
        
        retorno, palavra_ast = [],[]
        
        if to_str: # utilizar para retornar palavra_ast como str, não retorna nada em retorno
            palavra_ast, retorno = '', None
            for i in string_list:
                palavra_ast += i
                
                
                
            
        else: # utilizar para retornar string_list como lista e palavra_ast como lista "*"
            for i in string_list:
                retorno.append(i)
                palavra_ast.append('*')
            
        return palavra_ast, retorno

    palavra_secreta = 'algo muito legal' # palavra que será descoberta
    palavra_saida, ps_lista = to_list(palavra_secreta)
    tentativas = 0

    while True:
        contagem = 0
        letra = input('Digite uma letra: ')
        
        if len(letra) != 1: # não aceitar mais de um caractere
            print('Digite apenas uma letra!\n')
            continue
        
        tentativas += 1
        if letra not in ps_lista: # caso a letra digitada não esteja na lista, evita o resto do código
            print('Letra não encontrada!', f'\n{tentativas=}\n')  
        
        else:
            for i in ps_lista:
                if letra == i:
                    palavra_saida[contagem] = i
                contagem += 1
            
            palavra_saida = to_list(palavra_saida,True)[0]
            print(palavra_saida, f'\n{tentativas=}\n')
            palavra_saida = to_list(palavra_saida)[1]

        if '*' not in palavra_saida:
            print('Fimmmm!!!')
            break

# eu()
professor()