# Central Suporte

* 

<!-- ~~~Python
x = 4
print(x)
~~~ -->

Central Suporte, automatizando processos realizados no dia a dia

_all:
    pasta reservada para funções e arquivos gerais, utilizadas por todo código
    _files:
        (obrigatorio) base_gestao.csv - base extraida do Sistema de Gestão, possui dados dos agr's
        (opcional) bioac_cadastrar_cpf.txt - arquivo com cpf's dos agr's para cadastramento no BioAC, gerado ao extrair do bitrix ou manualmente
        (obrigatorio) credentials.json - utilizado para acessar api do Google Planilhas
        (obrigatorio) nomes.csv.gz - utilizado para definição de gênero por nome, para processos em SAF
        (opcional) para_cadastrar_saf.csv - utilizado para cadastrar em SAF. Gerado em BITRIX (na extração de dados) ou manualmente através do SAF
        (opcional) saf_cpf.txt - utilizado para consulta em saf
        ...

    Geral:
        funções úteis e gerais
        
        isFile -> se arquivo existe
        toFile -> gera arquivo com dados informados, substitui o arquivo caso já exista
        getFile -> lendo arquivos e retornando lista com dados
        parameters -> retorna lista com parametros aceitos, reservado para classes
        toDict -> retorna dicionário e caso de duplicidade, ou None em caso de KeyError
        getDadosBase -> pegando informações necessárias (cpf, nome, email) da base