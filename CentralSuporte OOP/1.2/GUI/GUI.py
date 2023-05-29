from tkinter import *
from tkinter import font

from saf.GUI import GUI_saf

class Application:

    def __init__(self):
        self.root = Tk()
        self.bg_color = 'lightgray'
        self.width_height = (700, 600)
        self.root.iconbitmap('images/icon.ico') # icone da janela
        self.root.resizable(False, False) # responsividade
        self.root.title('Central Suporte')
        self.root.config(background=self.bg_color)
        self.__centralize()
        self.__font()

        self.functions = {}

        self.root.mainloop()


    def __centralize(self):
        width, height = self.width_height

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))


    def __font(self):
        self.defaultFont = font.nametofont("TkDefaultFont") 
        self.defaultFont.configure(family="Bahnschrift SemiBold Condensed", size=15, weight=font.BOLD) 

    # será utilizado para funções 
    def _container_center(self):
        self.container_center = Frame(self.root)
        self.container_center.place(relx=0.15, rely=0, relheight=1, relwidth=0.85)



    # def _frame_saf(self):
    #     self._container_center() # limpando antigas widgets da tela
    #     GUI_saf(self)


    # def _frame_bioac(self):
    #     self._container_center() # limpando antigas widgets da tela

    #     self.frame_bioac = Label(self.container_center, justify='center', text='OOOI BioAC')
    #     self.frame_bioac.place(relx=0.5, rely=0.5)

    # def _frame_wpp(self):
    #     self._container_center() # limpando antigas widgets da tela

    #     self.frame_bioac = Label(self.container_center, justify='center', text='OOOI wpp')
    #     self.frame_bioac.place(relx=0.5, rely=0.5)


Application()