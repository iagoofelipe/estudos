import pyautogui as ag
from time import sleep
import csv
dict_base = {}

cnpj = '19.860.129000106'
cpf_solicitante = '03462721143'

def solicitar(nome,cpf_agr,email):
    # cnpj
    sleep(2)
    ag.click(166,663)
    ag.write(cnpj)

    #cpf solicitante
    ag.click(190,581)
    sleep(1)
    ag.write(cpf_solicitante)

    sleep(5)
    ag.click(472,811)
    sleep(2)

    # campo assunto
    ag.click(174,576) 
    sleep(0.5)

    # habilitar
    ag.click(303,251) 
    sleep(1)
    ag.scroll(-1000)
    sleep(2)

    # nome completo
    ag.click(131,188) 
    sleep(1)
    ag.write(nome)

    # cpf
    ag.click(149,280) 
    sleep(1)
    ag.write(cpf_agr)

    # email
    ag.click(131,366) 
    sleep(1)
    ag.write(email)

    # empresa
    ag.click(105,446) 
    sleep(1)
    ag.write("AR CERTFY")


    # detalhes demanda
    sleep(1)
    ag.click(90,537) 
    ag.write(f"Informo que o mesmo ja teve o seu dossie anexado no sistema SCDS. Aproveito para solicitar a liberacao de acesso do AGR mencionado no Bio-AC.\nCPF: {cpf_agr}\nNOME: {nome}\nE-MAIL: {email}")

    # enviar
    sleep(3)
    ag.click(460,764)
    sleep(2)

    # copiar protocolo
    ag.click(659,534)
    sleep(2)
    ag.keyDown('shift')
    ag.click(801,532)
    sleep(2)
    ag.keyUp('shift')
    ag.hotkey('ctrl','c')
    ag.click(706,877,interval=1)
    sleep(2)
    ag.hotkey('ctrl','v','enter')
    sleep(2)
    ag.hotkey('enter')
    sleep(2)
    ag.click(48,195,interval=1)
    sleep(2)
    ag.hotkey('ctrl','r')


with open('db.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        cpf_agr, nome, email = linha[0].split(';')
        indice = len(dict_base)

        dict_base[indice + 1] = (nome,cpf_agr,email)


with open('solicitados.txt','a') as arquivo:
    for i in dict_base:
        nome, cpf, email = dict_base[i]
        solicitar(nome,cpf,email)

        arquivo.write(nome + '\n')