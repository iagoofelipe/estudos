# instâncias e variáveis
from _all.Geral import isFile, diretorio
from GUI.GUI import Application
from GUI.Menu import _Container_menu

class CentralSuporte:
    """ objeto com verificações iniciais, processos e métodos necessários """
    def __init__(self):

        self.result_ver_inicial = self.verificacao_inicial()
        self.diretorio = diretorio
        self.arquivos_necessarios = ['base_gestao.csv','credentials.json','nomes.csv.gz']
        self.diretorio_padrao = '/_all/_files'


    def verificacao_inicial(self) -> dict:
        """ verificação inicial de arquivos necessários """
        result = {}

        for arquivo in self.arquivos_necessarios:
            
            fileName = f'{self.diretorio_padrao}\\{arquivo}'
            result[arquivo] = isFile(fileName)

        return result


if __name__ == '__main__':
    obj = CentralSuporte()

    # caso falte algum arquivo obrigatório
    for fileName in obj.result_ver_inicial:
        
        if not obj.result_ver_inicial[fileName]:
            exit(f'\nArquivo "{fileName}" não encontrado!')

    app = Application()

    _Container_menu(app, app.functions)