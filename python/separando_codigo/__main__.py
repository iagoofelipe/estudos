from tkinter import *
from menu import Menu

class Application:
    
    def __init__(self):
        self.root = Tk()

        self.root.geometry('600x500')
        self.__container_center()
        self.menu = Menu(self)

        self.root.mainloop()

    def __container_center(self):
        self.container_center = Frame(self.root, background='green')
        self.container_center.place(relheight=1, relwidth=3/4, relx=1/4, rely=0)

        self.text_center = Label(self.container_center)
        self.text_center.place(rely=.5, relx=.5)

        self.prhases = ['Olá', 'Mundo', '!']
        self._iter_prhases = iter(self.prhases)


if __name__ == '__main__':
    Application()
