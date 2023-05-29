from tkinter import *

class _Container_menu:

    def __init__(self, master_class, functions) -> None:
        self.master_class = master_class
        self.root = master_class.root

        self.container_menu()

    def container_menu(self):
        backgroud = '#444444'
        button_color = '#bcbcbc'
        button_clicked_color = '#999999'

        self.menu = Frame(self.root, background=backgroud)
        self.menu.place(relx=0, rely=0, relheight=1, relwidth=0.15)

        self.buttons_container = Frame(self.menu, background='white')
        self.buttons_container.place(relheight=0.452, relwidth=1, rely=0.274)

        self.button_saf = Button(self.buttons_container, justify='center', text='SAF', bd=0, background=button_color, activebackground=button_clicked_color, command=self.functions['saf'])
        self.button_saf.place(relheight=0.35, relwidth=1, rely=0)
        
        self.button_bioac = Button(self.buttons_container, justify='center', text='BioAC', bd=0, background=button_color, activebackground=button_clicked_color, command=self.functions['bioac'])
        self.button_bioac.place(relheight=0.30, relwidth=1, rely=0.355)

        self.button_wpp = Button(self.buttons_container, justify='center', text='WhatsApp', bd=0, background=button_color, activebackground=button_clicked_color, command=self.functions['wpp'])
        self.button_wpp.place(relheight=0.35, relwidth=1, rely=0.66)