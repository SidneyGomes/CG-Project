from pixel import put_pixel
import math

def reta_dda(x1, y1, x2, y2, centralizacao, img):  # Reta do algoritmo dda

    delta_x = abs(x2 - x1);
    delta_y = abs(y2 - y1)

    delta_final = max(delta_x, delta_y)

    x_inc = (x2 - x1) / delta_final
    y_inc = (y2 - y1) / delta_final

    x = x1
    y = y1

    put_pixel(round(x) + centralizacao, centralizacao - round(y), img)

    for i in range(delta_final):
        x += x_inc
        y += y_inc

        put_pixel(round(x) + centralizacao, centralizacao - round(y), img)


def reta_mid_point(x1, y1, x2, y2, centralizacao, img): # Reta do algoritmo ponto medio

        dx = abs(x2 - x1);
        dy = abs(y2 - y1);

        x = x1;
        y = y1;

        put_pixel(x + centralizacao, centralizacao -y, img);

        if((x1 < x2)and(y1 <= y2)):

            if(dx >= dy):

                d = 2*dy - dx
                indiceE = 2*dy
                incNE = 2*(dy - dx)

                while (x < x2):
                    if (d <= 0) :
                        d = d + indiceE
                        x = x + 1

                    else:
                        d = d + incNE
                        x = x + 1
                        y = y + 1

                    put_pixel(x + centralizacao, centralizacao -y, img);

            elif(dx < dy):

                d = dy - 2*dx
                indiceE = 2*(dy - dx)
                incNE = 2*(-dx)

                while (y < y2):

                    if (d < 0):
                        d = d + indiceE
                        x = x + 1
                        y = y + 1

                    else:
                        d = d + incNE;
                        y = y + 1;

                    put_pixel(x + centralizacao, centralizacao -y, img);

        elif(x1 >= x2) and (y1 < y2):

            if dx <= dy:

                d = dy - 2*dx
                indiceE = 2*(dy - dx)
                incNE = 2*(-dx)

                while (y < y2):

                    if (d < 0):
                        d = d + indiceE
                        x = x - 1
                        y = y + 1

                    else:
                        d = d + incNE
                        y = y + 1

                    put_pixel(x + centralizacao, centralizacao -y, img);

            elif(dx > dy):

                d = 2 * dy - dx
                indiceE = 2 * dy
                incNE = 2 * (dy - dx)

                while (x > x2) :
                    if (d <= 0) :
                        d = d + indiceE
                        x = x - 1

                    else:
                        d = d + incNE
                        x = x - 1
                        y = y + 1

                    put_pixel(x + centralizacao, centralizacao -y, img);

        elif((x1 > x2)and(y1 >= y2)):
            if(dx >= dy):

                d = 2*dy - dx
                indiceE = 2*dy
                incNE = 2*(dy - dx)

                while (x > x2):
                    if (d <= 0):
                        d = d + indiceE
                        x = x - 1

                    else:
                        d = d + incNE
                        x = x - 1
                        y = y - 1

                    put_pixel(x + centralizacao, centralizacao -y, img);

            elif(dx < dy):
                d = dy - 2*dx
                indiceE = 2*(dy - dx)
                incNE = 2*(-dx)

                while (y > y2):
                    if (d < 0):
                        d = d + indiceE;
                        x = x - 1;
                        y = y - 1;

                    else:
                        d = d + incNE
                        y = y - 1

                    put_pixel(x + centralizacao, centralizacao -y, img);

        elif((x1 <= x2)and(y1 > y2)):

            if(dx <= dy):
                d = dy - 2*dx
                indiceE = 2*(dy - dx)
                incNE = 2*(-dx)

                while (y > y2):
                    if (d < 0):
                        d = d + indiceE
                        x = x + 1
                        y = y - 1

                    else:
                        d = d + incNE
                        y = y - 1


                    put_pixel(x + centralizacao, centralizacao -y, img);

            elif(dx > dy):
                d = 2*dy - dx
                indiceE = 2*dy
                incNE = 2*(dy - dx)


                while (x < x2):
                    if (d <= 0):
                        d = d + indiceE
                        x = x + 1

                    else:
                        d = d + incNE
                        x = x + 1
                        y = y - 1

                    put_pixel(x + centralizacao, centralizacao -y, img);







