import subprocess, json

class Registros:
    """ Dados armazenados no Editor de Registro do Windows """

    def __init__(self):
        self.diretorio = r'HKEY_LOCAL_MACHINE\SOFTWARE\CentralSuporte'
        self.registros = {}

        __class__.getReg(self)

    def getReg(self) -> dict:
        """ lendo dados de registro """
        output = subprocess.check_output(rf'reg query {self.diretorio}').decode(errors='ignore').replace(f'\r\n{self.diretorio}\r\n    ', '').split('\r\n')

        for linha in output:
            linha = linha.strip().split('    REG_SZ    ') # removendo espaço no início e separando chave de dados
            
            if linha == ['']:
                pass
            else:
                self.registros[linha[0]] = linha[1]

    def setReg(self) -> None:
        pass


class Json:
    """ manipulando arquivos json """

    def getJson(arq_json):
        try:
            with open(arq_json, 'r', encoding='utf8') as f:
                return json.load(f)
        
        except FileNotFoundError:
            return None
        
    def setJson(dados: dict, fileName):
        with open(fileName, 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))