class Agenda:

    def __init__(self):
        self.width_num = 44
        self.contacts = {0:['Iago', '1234', 'iago@email.com', 'iago_tt', 'iago_insta']}

    def line_sep(self, width):
        return '-' * width

    def menu(self):
        """ menu inicial, contendo as opções disponíveis """

        print(self.line_sep(self.width_num))
        print('Bem-vindo a sua agenda telefônica!'.center(self.width_num))
        print('\n1 - NOVO CONTATO',
              '2 - CONSULTAR CONTATO',
              '3 - ATUALIZAR CONTATO',
              '4 - REMOVER CONTATO',
              '5 - RELATÓRIO\n',
              sep="\n")
        
        chosen_option = input('Digite o número da opção escolhida: ')

        while chosen_option not in ['1', '2', '3', '4', '5']:
            print('\nOpção inválida!')
            chosen_option = input('Digite o número da opção escolhida: ')

        return int(chosen_option)
    

    def new_contact(self):
        """ adicionando novos contatos à self.contacts """

        name = input('Digite o nome: ')

        while len(name) == 0: # campo com preenchimento obrigatório
            name = input('Digite o nome (campo obrigatório): ')

        phone = input('Digite o telefone: ')
        email = input('Digite o e-mail: ')
        twitter = input('Digite o twitter: ')
        instagram = input('Digite o instagram: ')
        key = len(self.contacts)

        self.contacts[key] = [name, phone, email, twitter, instagram]
        print('\nContato salvo com êxito!')


    def upgrade_contact(self):
        """ atualizando contatos """
        
        if len(self.contacts) == 0:
            print('\nNenhum contato cadastrado!')
        
        else:
            text_structure = '{ID:>5}{NAME:>11}{PHONE:>20}{EMAIL:>25}{TT:>25}{INSTA:>25}'

            print(self.line_sep(111), '\n')
            print(text_structure.format(ID="ID", NAME="Nome", PHONE="Telefone", EMAIL="E-mail", TT="Twitter", INSTA="Instagram"), '\n')

            for key in self.contacts:
                print(text_structure.format(key, *self.contacts[key]))

    # def __report(self):
    #     return None if len(self.contacts) == 0 else 

print(Agenda().upgrade_contact())