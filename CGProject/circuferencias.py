from pixel import put_pixel
import math

def circ_ponto_medio(raio, centralizacao, deslocamento_x, deslocamento_y, img):
    
    x = 0.0
    y = raio
    d = 5/4 - raio
    d = int(1 - raio)

    ponto_circulo(x, y, centralizacao, deslocamento_x, deslocamento_y, img)

    while(y > x):

        if(d < 0):
            d+= (2 * x) + 3
        else:
            d += (2 * (x - y)) + 5
            y -= 1

        x += 1

        ponto_circulo(x, y, centralizacao, deslocamento_x, deslocamento_y, img)

def circ_trigonometrico(raio, centralizacao, deslocamento_x, deslocamento_y, img):

    x = 0
    y = 0

    for i in range(45):
        x = round(raio * math.cos(math.radians(i)))
        y = round(raio * math.sin(math.radians(i)))

        ponto_circulo(x, y, centralizacao, deslocamento_x, deslocamento_y, img)


def circ_equacao_explicita(raio, centralizacao, deslocamento_x, deslocamento_y, img):


    x = 0
    for i in range(int(raio) + 1):
        delta = math.pow(raio, 2)- math.pow(x, 2)

        if(delta < 0):
            continue

        y = math.sqrt(delta)
        x += 1

        simetria_ponto_circu(x, y, centralizacao, deslocamento_x, deslocamento_y, img)
    
def elipse_ponto_medio(a, b, centralizacao, deslocamento_x, deslocamento_y, img):

    x = 0
    y = b

    d1 = math.pow(b, 2) - (math.pow(a, 2) * b) + math.pow(a, 2) / 4.0

    ponto_elipse(x, y, centralizacao, deslocamento_x, deslocamento_y, img)

    while(math.pow(a, 2) * (y - 0.5) > math.pow(b, 2) * (x + 1)):
        if(d1 < 0):
            d1 += math.pow(b, 2) * (2 * x + 3)
            x += 1
        else:
            d1 += math.pow(b, 2) * (2 * x + 3) + math.pow(a, 2) *(-2 * y + 2)
            x += 1
            y -= 1

        ponto_elipse(x, y, centralizacao, deslocamento_x, deslocamento_y, img)

    d2 = math.pow(b, 2) * (x + 0.5) * (x + 0.5) + math.pow(a, 2) * (y - 1) * (y - 1) - math.pow(a, 2) * math.pow(b,2)

    while(y > 0):
        if(d2 < 0):
            d2 += math.pow(b, 2) * (2 * x + 2) + math.pow(a, 2) * (-2 * y + 3)
            x += 1
            y -= 1
        else:
            d2 += math.pow(a, 2) * (-2 * y + 3)
            y -= 1

        ponto_elipse(x, y, centralizacao, deslocamento_x, deslocamento_y, img)
            

def ponto_circulo(x, y, centralizacao, deslocamento_x, deslocamento_y, img):

    put_pixel(centralizacao + x + deslocamento_x, centralizacao + y - deslocamento_y, img)
    put_pixel(centralizacao + x + deslocamento_x, centralizacao - y - deslocamento_y, img)
    put_pixel(centralizacao - x + deslocamento_x, centralizacao - y - deslocamento_y, img)
    put_pixel(centralizacao - x + deslocamento_x, centralizacao + y - deslocamento_y, img)
    put_pixel(centralizacao + y + deslocamento_x, centralizacao + x - deslocamento_y, img)
    put_pixel(centralizacao + y + deslocamento_x, centralizacao - x - deslocamento_y, img)
    put_pixel(centralizacao - y + deslocamento_x, centralizacao - x - deslocamento_y, img)
    put_pixel(centralizacao - y + deslocamento_x, centralizacao + x - deslocamento_y, img)
 

def ponto_elipse(x, y, centralizacao, deslocamento_x, deslocamento_y, img):
    
    put_pixel(centralizacao + x + deslocamento_x, centralizacao + y - deslocamento_y, img)
    put_pixel(centralizacao + x + deslocamento_x, centralizacao - y - deslocamento_y, img)
    put_pixel(centralizacao - x + deslocamento_x, centralizacao - y - deslocamento_y, img)
    put_pixel(centralizacao - x + deslocamento_x, centralizacao + y - deslocamento_y, img)


def simetria_ponto_circu(x, y, centralizacao, deslocamento_x, deslocamento_y, img):
    put_pixel(x + centralizacao + deslocamento_x, centralizacao - y - deslocamento_y, img)
    put_pixel(x + centralizacao + deslocamento_x, centralizacao - (y * -1) - deslocamento_y, img)
    put_pixel(centralizacao - x + deslocamento_x, centralizacao + y - deslocamento_y, img)
    put_pixel(centralizacao - x + deslocamento_x, centralizacao + (y * -1) - deslocamento_y, img)


