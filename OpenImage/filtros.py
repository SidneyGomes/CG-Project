import random
import numpy as np
from PIL import Image
from enum import Enum


class FilterTypes(Enum):
    SOBEL = "Sobel"
    PASSA_ALTA_BASICO = "Passa Alta Basico"
    MEDIANA = "Mediana"
    MEDIA = "Media"
    ROBERTS = "Roberts"
    ROBERTS_CRUZADO = "Roberts Cruzado"
    PREWITT = "Prewitt"
    ALTO_REFORCO = "Alto Reforco"
    

class Filters():

    
    def __init__(self):
        self.imagem = None
        self.imagemFiltrada = []


    #Recebe qual filtro sera aplicado e a matriz com a imagem para aplicaro o filtro
    def convolucao(self, filterType, imagem):

        self.imagem = imagem
        
        for i in range(len(self.imagem)):
            imagemFiltrada_aux = []
            for j in range(len(self.imagem)):
                linha =  i - 1
                coluna = j - 1

                matriz_meio_pixel = []
                for k in range(3):
                    matriz_meio_pixel_aux = []
                    for l in range(3):
                        if (linha + k >= 0 and linha + k <  len(self.imagem)) and (coluna + l >= 0 and coluna + l < len(self.imagem)):
                            matriz_meio_pixel_aux.append(self.imagem[linha + k][coluna + l])
                        else:
                            matriz_meio_pixel_aux.append(0)

                    matriz_meio_pixel.append(matriz_meio_pixel_aux)


                if(filterType == FilterTypes.PASSA_ALTA_BASICO.value):
                    imagemFiltrada_aux.append(self.passa_alta(matriz_meio_pixel))
                elif(filterType == FilterTypes.MEDIA.value):
                    imagemFiltrada_aux.append(self.media(matriz_meio_pixel))
                elif(filterType == FilterTypes.MEDIANA.value):
                    imagemFiltrada_aux.append(self.mediana(matriz_meio_pixel))
                elif(filterType == FilterTypes.ROBERTS.value):
                    imagemFiltrada_aux.append(self.roberts(matriz_meio_pixel))
                elif(filterType == FilterTypes.ROBERTS_CRUZADO.value):
                    imagemFiltrada_aux.append(self.roberts_cruzado(matriz_meio_pixel))
                elif(filterType == FilterTypes.SOBEL.value):
                    imagemFiltrada_aux.append(self.sobel(matriz_meio_pixel))
                elif(filterType == FilterTypes.PREWITT.value):
                    imagemFiltrada_aux.append(self.prewitt(matriz_meio_pixel))
                      

            self.imagemFiltrada.append(imagemFiltrada_aux)

        return self.imagemFiltrada

    def convolucao_alto_reforco(self, imagem, a):
        self.imagem = imagem
        
        for i in range(len(self.imagem)):
            imagemFiltrada_aux = []
            for j in range(len(self.imagem)):
                linha =  i - 1
                coluna = j - 1

                matriz_meio_pixel = []
                for k in range(3):
                    matriz_meio_pixel_aux = []
                    for l in range(3):
                        if (linha + k >= 0 and linha + k <  len(self.imagem)) and (coluna + l >= 0 and coluna + l < len(self.imagem)):
                            matriz_meio_pixel_aux.append(self.imagem[linha + k][coluna + l])
                        else:
                            matriz_meio_pixel_aux.append(0)

                    matriz_meio_pixel.append(matriz_meio_pixel_aux)


                imagemFiltrada_aux.append(self.alto_reforco(matriz_meio_pixel, a))

            self.imagemFiltrada.append(imagemFiltrada_aux)

        return self.imagemFiltrada
        
    
    def passa_alta(self, multiplica_matriz):

        mascara = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
        
        soma = 0
        for k in range(len(mascara)):
            for l in range(len(mascara)):
                soma += (multiplica_matriz[k][l] * mascara[k][l])

        if soma > 255:
            soma = 255
        elif soma < 0:
            soma = 0

        return soma

    
    #Mediana dos elementos da centralizacao do pixel
    def mediana(self, multiplica_matriz):

        matriz_ordenada = []
        for i in range(len(multiplica_matriz)):
            for j in range(len(multiplica_matriz)):
                matriz_ordenada.append(multiplica_matriz[i][j])

        matriz_ordenada.sort()
    

        return matriz_ordenada[len(matriz_ordenada) // 2]


    def media(self, multiplica_matriz):

        mascara = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]   
                
        soma = 0
        for i in range(len(multiplica_matriz)):
            for j in range(len(multiplica_matriz)):
                soma += multiplica_matriz[i][j] * mascara[i][j]

                
        if soma > 255:
            soma = 255
        elif soma < 0:
            soma = 0

        return round(soma)

    def roberts(self, multiplica_matriz):

        mascara_x = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]
        mascara_y = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
        

        soma_x = 0
        soma_y = 0

        for k in range(len(mascara_x)):
            for l in range(len(mascara_x)):
                soma_x += (multiplica_matriz[k][l] * mascara_x[k][l])
                soma_y += (multiplica_matriz[k][l] * mascara_y[k][l])

        magnitude = soma_x + soma_y
    
        if magnitude > 255:
            magnitude = 255
        elif magnitude < 0:
            magnitude = 0
        
        return magnitude

    def roberts_cruzado(self, multiplica_matriz):

        mascara_x = [[0, 0, 0], [0, 1, 0], [0, 0, -1]]
        mascara_y = [[0, 0, 0], [0, 0, 1], [0, -1, 0]]
        
        soma_x = 0
        soma_y = 0

        for k in range(len(mascara_x)):
            for l in range(len(mascara_x)):
                soma_x += (multiplica_matriz[k][l] * mascara_x[k][l])
                soma_y += (multiplica_matriz[k][l] * mascara_y[k][l])

        magnitude = soma_x + soma_y
    
        if magnitude > 255:
            magnitude = 255
        elif magnitude < 0:
            magnitude = 0
        
        return magnitude


    def alto_reforco(self, multiplica_matriz, a):

        a = 9 * a - 1

        mascara = [[-1, -1, -1], [-1, a, -1], [-1, -1, -1]]


        soma = 0
        for i in range(len(multiplica_matriz)):
            for j in range(len(multiplica_matriz)):
                soma += multiplica_matriz[i][j] * mascara[i][j]


        if soma > 255:
            soma = 255
        elif soma < 0:
            soma = 0
        
        return round(soma)


    def prewitt(self, multiplica_matriz):

        mascara_x = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
        mascara_y = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        

        soma_x = 0
        soma_y = 0
        for k in range(len(mascara_x)):
            for l in range(len(mascara_x)):
                soma_x += (multiplica_matriz[k][l] * mascara_x[k][l])
                soma_y += (multiplica_matriz[k][l] * mascara_y[k][l])


        magnitude = soma_x + soma_y

        if magnitude > 255:
            magnitude = 255
        elif magnitude < 0:
            magnitude = 0

        return magnitude

    def sobel(self, multiplica_matriz):

        mascara_x = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        mascara_y = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        
        soma_x = 0
        soma_y = 0

        for k in range(len(mascara_x)):
            for l in range(len(mascara_x)):
                soma_x += (multiplica_matriz[k][l] * mascara_x[k][l])
                soma_y += (multiplica_matriz[k][l] * mascara_y[k][l])


        magnitude = soma_x + soma_y

        if magnitude > 255:
            magnitude = 255
        elif magnitude < 0:
            magnitude = 0

        return magnitude
        
        
        
                
                
        
        
        

        
        

    


