from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from filtros import *

window = Tk()
window.geometry('1100x700')
window.resizable(False, False)
window.title('Processamento de imagens - Projeto 2')

class CreateView():

    def __init__(self):
        self.image1 = Image.open("noimage.jpg")
        self.seta = Image.open("seta.png")
        self.image2 = Image.open("noimage.jpg")

        self.tk_image1 = None
        self.tk_seta = None
        self.tk_image2 = None


        self.label_image1 = None
        self.label_seta = None
        self.label_image2 = None
        self.label_tipo_filtro = None


        self.entry_a = None


        self.button_abrir = None
        self.button_converter = None

        self.filters = Filters()

        self.caminho_arquivo_image1 = None


    def create(self, tipo_filtro):

        #Begin Criaçao da label onde sera aberto a primeira imagem para aplicar o filtro
            self.image1 = self.image1.resize((400, 400))
            self.tk_image1 = ImageTk.PhotoImage(self.image1)

            self.label_image1 = Label(window, image=self.tk_image1)
            self.label_image1.grid(row = 0, column = 0, padx= 10, pady = 10)
        #End
            
        #Begin Label da imagem da seta visual, nao necessario self nao é preciso salva-la pois é so para visual

            self.seta = self.seta.resize((120, 120))
            self.img_photoImage = ImageTk.PhotoImage(self.seta)
            self.label_seta = Label(window, image=self.img_photoImage)
            self.label_seta.grid(row= 0, column = 1, padx = 10, pady = 10)          
        #End

        #Begin Criacao da label onde sera a aberta a imagem convertida


            self.image2 = self.image2.resize((400, 400))
            self.tk_image2 = ImageTk.PhotoImage(self.image2)

            self.label_image2 = Label(window, image=self.tk_image2)
            self.label_image2.grid(row = 0, column = 2, padx= 10, pady = 10)
            
        #end


        #Begin botao abrir imagem para ser convertida e bota de converter 
            self.button_abrir = Button(text="Abrir", command=self.open_image)
            self.button_abrir.grid(row = 1, column =0, pady = 10)

            self.button_converter = Button(text="Converter", command=lambda: self.convert_image(tipo_filtro))
            self.button_converter.grid(row = 1, column =2, pady = 10)

        #End

        #Begin Entry do valor do alto reforco A            
            if(tipo_filtro == "Alto Reforco"):

                a_value_label = Label(window, text = "Valor de A:")
                a_value_label.grid(row = 2, column = 0, sticky="e")

                self.entry_a  = Entry(window)
                self.entry_a.grid(row = 2, column = 1, pady = 20)

        #End

        #Begin Label tipo filtro
    
            self.label_tipo_filtro = Label(window, text = tipo_filtro, font = ("Arial", 20))
            self.label_tipo_filtro.grid(row=3, column = 1, pady = 30)

    
            

    
    def open_image(self):
        #Begin abrir sistema para buscar caminho da imagem a ser convertida

            self.caminho_arquivo_image1 = filedialog.askopenfilename()

            self.image1 = Image.open(self.caminho_arquivo_image1)
            self.image1 = self.image1.resize((400, 400))
            self.tk_image1 = ImageTk.PhotoImage(self.image1)

            self.label_image1 = Label(window, image=self.tk_image1)
            self.label_image1.grid(row = 0, column = 0, padx= 10, pady = 10)


        #End

    def convert_image(self, tipo_filtro):
        # Begin converter imagem e paassar para a label imagem 2
    
            with open(self.caminho_arquivo_image1, 'r') as arquivo:
                # Verifica o formato PGM
                if arquivo.readline().strip() != 'P2':
                    raise ValueError('O arquivo não está no formato PGM P2.')

                # Ignora linhas de comentários
                linha = arquivo.readline().strip()
                while linha.startswith('#'):
                    linha = arquivo.readline().strip()

                # Lê as dimensões da imagem
                largura, altura = map(int, linha.split())

                # Lê o valor máximo do pixel
                valor_maximo = int(arquivo.readline().strip())

                # Lê os dados da imagem
                imagem_linhas = arquivo.readlines()

            # Converte os dados da imagem em uma matriz numpy
            imagem = np.array([list(map(int, linha.split())) for linha in imagem_linhas], dtype=np.uint8)

           # Converte a matriz de imagem em uma imagem PIL


            

            if(tipo_filtro == "Alto Reforco"):
                imagem = np.array(self.filters.convolucao_alto_reforco(imagem, float(self.entry_a.get())), dtype=np.uint8)
            else:
                imagem = np.array(self.filters.convolucao(tipo_filtro, imagem), dtype=np.uint8)

            imagem_pil = Image.fromarray(imagem)
    
        
        # Salva a imagem no formato PGM P2 (representação ASCII)
            with open("filtrada.pgm", 'w') as arquivo:
                    
                # Escreve o cabeçalho do arquivo
                arquivo.write('P2\n')
                arquivo.write(f'{imagem.shape[1]} {imagem.shape[0]}\n')
                arquivo.write(f'{np.max(imagem)}\n')

                # Escreve os valores dos pixels da imagem
                np.savetxt(arquivo, imagem, fmt='%d')

            
            self.image2 = Image.open("filtrada.pgm")
            self.image2 = self.image2.resize((400, 400))
            self.tk_image2 = ImageTk.PhotoImage(self.image2)

            self.label_image2 = Label(window, image=self.tk_image2)
            self.label_image2.grid(row = 0, column = 2, padx = 10, pady = 10)

            
        #End

    def command_button(self, tipo_filtro):
        if self.label_tipo_filtro != None:
            self.label_tipo_filtro.destroy()

        self.reset()
        self.create(tipo_filtro)



    def reset(self):
        self.__init__()






#Begin Create superior menu

create_view = CreateView()


menu = Menu(window)
menu_filtros = Menu(menu)



menu_filtros.add_command(label = "Media", command =lambda: create_view.command_button("Media"))
menu_filtros.add_command(label = "Mediana", command = lambda:create_view.command_button("Mediana"))
menu_filtros.add_command(label = "Passa Alta Basico", command = lambda:create_view.command_button("Passa Alta Basico"))
menu_filtros.add_command(label = "Roberts", command = lambda:create_view.command_button("Roberts"))
menu_filtros.add_command(label = "Roberts Cruzado", command =lambda: create_view.command_button("Roberts Cruzado"))
menu_filtros.add_command(label = "Alto Reforco", command =lambda: create_view.command_button("Alto Reforco"))
menu_filtros.add_command(label = "Prewitt", command =lambda: create_view.command_button("Prewitt"))
menu_filtros.add_command(label = "Sobel", command =lambda: create_view.command_button("Sobel"))



menu.add_cascade(label="Filtros", menu = menu_filtros)
window.config(menu = menu)

# End 




window.mainloop()

