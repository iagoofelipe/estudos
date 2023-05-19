import tkinter as tk

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.widget1 = tk.Frame(self.root, background='#dff186')

        self.root.title('Central Suporte') # título da janela
        # self.root.attributes('-alpha', 0.5) # transparência
        self.widget1.pack()

        # adicionando texto
        self.msg = tk.Label(self.widget1, text="Primeiro widget", background='#dff186')
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        # adicionando botão
        self.sair = tk.Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

        # adicionando botão
        self.alterar_texto = tk.Button(self.widget1)
        self.alterar_texto["text"] = "Alterar texto"
        self.alterar_texto["font"] = ("Calibri", "10")
        self.alterar_texto["width"] = 10
        self.alterar_texto['command'] = self.mudarTexto
        self.alterar_texto.pack()


        self.root.iconbitmap(r'E:\Downloads\icon.ico')
        __class__.geometry(self)


    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"

        else:
             self.msg["text"] = "Primeiro widget"

        


    def mainloop(self):
        self.root.mainloop()


    def geometry(self, height=200, width=300):
            """ definindo geometria e centralizamento """

            # get the screen dimension
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # find the center point
            center_x = int(screen_width/2 - width / 2)
            center_y = int(screen_height/2 - height / 2)

            # set the position of the window to the center of the screen
            self.root.geometry(f'{width}x{height}+{center_x}+{center_y}')



if __name__ == '__main__':
    # root = tk.Tk()
    
    root = Application()
    root.geometry(300,300)
    
    root.mainloop()
