from tkinter import *

root = Tk()

class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#0e2e5c')
        self.root.geometry("700x500") # geometria da janela
        self.root.resizable(True, True) # responsividade horizontal e vertical
        # self.root.maxsize(width=900, height=700)
        self.root.minsize(width=700, height=500)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd = 4, #bg = '#0e2e5c',
                            highlightbackground='lightgray', # cor da borda do frame
                            highlightthickness=2) # expessura do frame
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) # porcentagem da tela x horizontal e y vertical
      
        self.frame2 = Frame(self.root, bd = 4, #bg = '#0e2e5c',
                            highlightbackground='lightgray', # cor da borda do frame
                            highlightthickness=2) # expessura do frame
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46) # porcentagem da tela x horizontal e y vertical

    def widgets_frame1(self):
        # botão limpar
        self.bt_limpar = Button(self.frame1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # self.bt_limpar['command'] = self.limpar()

        # botão buscar
        self.bt_buscar = Button(self.frame1, text="Buscar")
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão novo
        self.bt_novo = Button(self.frame1, text="Novo")
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # botão alterar
        self.bt_alterar = Button(self.frame1, text="Alterar")
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão apagar
        self.bt_apagar = Button(self.frame1, text="Apagar")
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # label código
        self.lb_codigo = Label(self.frame1, text="Código", bg='#C0C0C0')
        self.lb_codigo.place(relx=0.01, rely=0.03)

        # input código
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.01, rely=0.15, relwidth=0.09)


        # label nome
        self.lb_nome = Label(self.frame1, text="Nome", bg='#C0C0C0')
        self.lb_nome.place(relx=0.01, rely=0.33)

        # input nome
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.01, rely=0.45, relwidth=0.98)


        # label telefone
        self.lb_telefone = Label(self.frame1, text="Telefone", bg='#C0C0C0')
        self.lb_telefone.place(relx=0.01, rely=0.60)

        # input telefone
        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx=0.01, rely=0.72, relwidth=0.48)
        

        # label cidade
        self.lb_cidade = Label(self.frame1, text="Cidade", bg='#C0C0C0')
        self.lb_cidade.place(relx=0.51, rely=0.60)

        # input cidade
        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.51, rely=0.72, relwidth=0.48)

Application()
root.mainloop()
