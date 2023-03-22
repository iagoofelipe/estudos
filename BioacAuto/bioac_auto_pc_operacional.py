import pyautogui as ag
from time import sleep
import csv
dict_base = {}

# lendo arquivo csv
with open('teste.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        cpf_agr, nome, email = linha[0].split(';')
        indice = len(dict_base)

        dict_base[indice + 1] = (nome,cpf_agr,email)

cnpj = '19.860.129000106'
cpf_solicitante = '03462721143'

def solicitar(nome,cpf_agr,email):
    # cnpj
    sleep(2)
    ag.click(103,533)
    ag.write(cnpj)

    #cpf solicitante
    ag.click(103,471)
    sleep(1)
    ag.write(cpf_solicitante)

    sleep(5)
    ag.click(451,659)
    sleep(2)

    # campo assunto
    ag.click(90,464) 
    sleep(0.5)

    # habilitar
    ag.click(90,186) 
    sleep(1)
    ag.scroll(-1000)
    sleep(2)

    # nome completo
    ag.click(62,200) 
    sleep(1)
    ag.write(nome)

    # cpf
    ag.click(62,266) 
    sleep(1)
    ag.write(cpf_agr)

    # email
    ag.click(62,331) 
    sleep(2)
    ag.write(email)

    # empresa
    ag.click(62,399) 
    sleep(1)
    ag.write("AR CERTFY")


    # detalhes demanda
    sleep(1)
    ag.click(62,474) 
    ag.write(f"Informo que o mesmo ja teve o seu dossie anexado no sistema SCDS. Aproveito para solicitar a liberacao de acesso do AGR mencionado no Bio-AC.\nCPF: {cpf_agr}\nNOME: {nome}\nE-MAIL: {email}")

    # enviar
    sleep(1)
    ag.click(433,656)
    sleep(2)

    # copiar protocolo
    ag.click(631,440)
    sleep(2)
    ag.keyDown('shift')
    ag.click(746,437)
    sleep(2)
    ag.keyUp('shift')
    ag.hotkey('ctrl','c')
    
    # abrindo excel para colar
    ag.click(803,745,interval=1)
    sleep(2)
    ag.hotkey('ctrl','v','enter')
    sleep(2)
    
    # voltando tela de solicitação
    ag.click(64,150,interval=1)
    sleep(2)
    ag.hotkey('ctrl','r')


for i in dict_base:
    nome, cpf, email = dict_base[i]
    solicitar(nome,cpf,email)
    
    with open('solicitados.txt','a') as arquivo:
        arquivo.write(nome + '\n')


# Pegando coordenadas do mouse
# while True:
#     sleep(1)
#     x, y = ag.position()
#     print (f'{x},{y}')