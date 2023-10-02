perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opcoes': ['1','4','5','22'],
        'resposta': '4'
    },
    {
        'pergunta': 'Quanto é 10*20?',
        'opcoes': ['10','20','100','200'],
        'resposta': '200'
    },
    {
        'pergunta': 'Qual nome das cargas positivas no núcleo de um átomo?',
        'opcoes': ['Prótons', 'Nêutrons', 'Elétrons'],
        'resposta': 'Prótons'
    },
]

for pergunta in perguntas:
    print(pergunta['pergunta'])
    pergunta['valid_options'] = []
    for i, value in enumerate(pergunta['opcoes']):
        print(f' {i}. {value}')
        pergunta['valid_options'].append(str(i))

    resposta = input("\nresposta: ")
    while resposta not in pergunta['valid_options']:
        print("Resposta não está entre as opções!")
        resposta = input("\nresposta: ")

    if pergunta['opcoes'][int(resposta)] == pergunta['resposta']:
        print("Correto!")
    else:
        print("Incorreto :(\n")