from tkinter import *

class Application:
    
    def __init__(self, root):
        """ atributos da janela """
        self.root = root

        self.root.title("Passando para classe")
        self.root.config(bg="lightgray")

        # frame esquerdo e direito
        self.frame_esquerdo = Frame()
        self.frame_esquerdo = Frame(root, width=200, height=400, bg='grey')
        self.frame_esquerdo.grid(row=0, column=0, padx=10, pady=5)

        self.frame_direito = Frame(root, width=650, height=400, bg='grey')
        self.frame_direito.grid(row=0, column=1, padx=10, pady=5)

        # carregando a imagem para ser "editada"
        self.imageLabel = Label(self.frame_esquerdo, text="Original Image")
        self.imageLabel.grid(row=0, column=0, padx=5, pady=5)

        # criando frames e labbels no frame_esquerdo
        self.image = PhotoImage(file=r"E:\git\estudos\python\tkinter\gif.gif")
        self.original_image = self.image.subsample(3,3)  # redimensionando imagem usando subsample
        self.imageLabel_left = Label(self.frame_esquerdo, image=self.original_image).grid(row=1, column=0, padx=5, pady=5)

        # Display image in right_frame
        self.imageLabel_right = Label(self.frame_direito, image=self.image)
        self.imageLabel_right.grid(row=0,column=0, padx=5, pady=5)

        # Create tool bar frame
        self.tool_bar = Frame(self.frame_esquerdo, width=180, height=185)
        self.tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        Label(self.tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(self.tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

        # Example labels that could be displayed under the "Tool" menu
        Label(self.tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
        Label(self.tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
        Label(self.tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
        Label(self.tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
        Label(self.tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)


if __name__ == '__main__':
    root = Tk()
    Application(root)
    root.mainloop()