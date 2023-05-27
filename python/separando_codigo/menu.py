from tkinter import *
import webbrowser

class Menu:

    def __init__(self, master_class):
        self.master_class = master_class
        self.root = self.master_class.root

        self.__container_menu()

    def __container_menu(self):
        self.container_menu = Frame(self.root, background='yellow')
        self.container_menu.place(relheight=1, relwidth=1/4)

        # Button container menu
        self.button_container_menu = Button(self.container_menu)
        self.button_container_menu['text'] = 'Botão Menu'
        self.button_container_menu['bd'] = 0
        self.button_container_menu['background'] = 'purple'
        self.button_container_menu['command'] = self.fbutton_container_menu
        self.button_container_menu.place(relx=1/3, rely=1/3)

        # Button text center
        self.button_text_center = Button(self.container_menu)
        self.button_text_center['text'] = 'Mudar Texto'
        self.button_text_center['bd'] = 0
        self.button_text_center['background'] = 'purple'
        self.button_text_center['command'] = self.fbutton_text
        self.button_text_center.place(relx=1/3, rely=2/3)

    
    def fbutton_container_menu(self):
        webbrowser.open('https://www.kabum.com.br/')
    

    def fbutton_text(self):
        self.master_class.text_center['text'] = next(self.master_class._iter_prhases)

        if self.master_class.text_center['text'] == self.master_class.prhases[-1]:
            self.master_class._iter_prhases = iter(self.master_class.prhases)

