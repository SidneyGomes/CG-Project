import random, math
from tkinter import *

import normalizedconvertions
from retas import *
from circuferencias import *
from normalizedconvertions import *

width, height = 600, 600
centralizacao = 300
window = Tk()
window.geometry('1200x1000')
window.resizable(False, False)
window.title("Computacao Grafica - Projeto")
img = None
canvas = None


# Create Initial Screen
class CartesianPlane:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.label_change = None

    def graph(self):  # Cria  o desenho das linhas do plano cartesiano
        for i in range(600):
            img.put("#ffffff", (self.width // 2, i))
            img.put("#ffffff", (i, self.height // 2))

    def change_label(self, x, y):
        self.label_change["text"] = "X: %d Y: %d" % (x - centralizacao, centralizacao - y)

    def mouse_position(self, event):  # Evento que busca captura o evento do mouse sendo movido na tela e muda o label do text
        x, y = event.x, event.y
        self.change_label(x, y);


class DrawReta:

    def __init__(self):
        self.watch_screen = 0
        self.flag_coordinates = False
        self.label_x_y = None
        self.label_x1 = None
        self.label_y1 = None
        self.entry_x1 = None
        self.entry_y1 = None
        self.label_x2 = None
        self.label_y2 = None
        self.entry_x2 = None
        self.entry_y2 = None
        self.btn = None
        self.btn_2 = None
        self.cartesianPlane = CartesianPlane()

    def reset(self):
        self.__init__()

    def create_view(self):
        global canvas, img
        
        window.geometry('1200x1000')

        list = window.grid_slaves()
        for i in list:
            i.destroy()


        self.label_x_y = Label(window, text="X: 0 Y: 0", font='Times 14')
        self.cartesianPlane.label_change = self.label_x_y
        self.label_x_y.grid(row=3, column=5)

        self.label_x1 = Label(window, text="X1: ", font='Times 14')
        self.label_x1.grid(row=0, column=0)

        self.label_y1 = Label(window, text="Y1: ", font='Times 14')
        self.label_y1.grid(row=0, column=2)

        self.entry_x1 = Entry(window, width=10)
        self.entry_x1.grid(row=0, column=1)
        self.entry_y1 = Entry(window, width=10)
        self.entry_y1.grid(row=0, column=3)

        self.label_x2 = Label(window, text="X2: ", font='Times 14')
        self.label_x2.grid(row=1, column=0)
        self.label_y2 = Label(window, text="Y2: ", font='Times 14')
        self.label_y2.grid(row=1, column=2)

        self.entry_x2 = Entry(window, width=10)
        self.entry_x2.grid(row=1, column=1)
        self.entry_y2 = Entry(window, width=10)
        self.entry_y2.grid(row=1, column=3)

        if self.watch_screen == 1:
            self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: reta_dda(int(self.entry_x1.get()), int(self.entry_y1.get()),
                                                       int(self.entry_x2.get()),
                                                       int(self.entry_y2.get()), centralizacao, img))
        else:
            self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: reta_mid_point(int(self.entry_x1.get()), int(self.entry_y1.get()),
                                                       int(self.entry_x2.get()),
                                                       int(self.entry_y2.get()), centralizacao, img))
        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn_2 = Button(window, text='Clear', bd='5', command=self.clean)
        self.btn_2.grid(row=2, column=2)

        canvas = Canvas(window, width=width, height=height, bg="#000000")
        canvas.grid(row=3, column=4)

        img = PhotoImage(width=width, height=height)
        canvas.create_image((width // 2, height // 2), image=img, state="normal")

        self.cartesianPlane.graph() # Desenha as linhas do plano cartesiano

    def clean(self):
        img.blank()
        canvas.create_image((width // 2, height // 2), image=img, state="normal")
        self.reset()

        if self.watch_screen == 1:
            self.create_view_dda()
        else:
            self.create_view_mid_point()

        self.entry_x1.delete(0, "end")
        self.entry_y1.delete(0, "end")
        self.entry_x2.delete(0, "end")
        self.entry_y2.delete(0, "end")
        self.cartesianPlane.graph()


    #Desenha com o clique do mouse a reta dda
    def draw_reta_mouse(self, event):
        if not self.flag_coordinates:
            self.entry_x1.delete(0, "end")
            self.entry_y1.delete(0, "end")
            self.entry_x1.insert(0, event.x - centralizacao)
            self.entry_y1.insert(0, centralizacao - event.y)
            self.flag_coordinates = True

        else:
            self.entry_x2.delete(0, "end")
            self.entry_y2.delete(0, "end")
            self.entry_x2.insert(0, event.x - centralizacao)
            self.entry_y2.insert(0, centralizacao - event.y)
            self.flag_coordinates = False

            reta_dda(int(self.entry_x1.get()), int(self.entry_y1.get()), int(self.entry_x2.get()),
                     int(self.entry_y2.get()), centralizacao, img)


    #Desenha com o clique do mouse a reta do ponto medio
    def draw_reta_mid_point_mouse(self, event):
        if not self.flag_coordinates:
            self.entry_x1.delete(0, "end")
            self.entry_y1.delete(0, "end")
            self.entry_x1.insert(0, event.x - centralizacao)
            self.entry_y1.insert(0, centralizacao - event.y)
            self.flag_coordinates = True
        else:
            self.entry_x2.delete(0, "end")
            self.entry_y2.delete(0, "end")
            self.entry_x2.insert(0, event.x - centralizacao)
            self.entry_y2.insert(0, centralizacao - event.y)
            self.flag_coordinates = False

            reta_mid_point(int(self.entry_x1.get()), int(self.entry_y1.get()), int(self.entry_x2.get()),
                           int(self.entry_y2.get()), centralizacao, img)

    def create_view_dda(self):  # Tela  1
        btn = Button(window, text='Draw', bd='5',
                     command=lambda: reta_dda(int(self.entry_x1.get()), int(self.entry_y1.get()),
                                              int(self.entry_x2.get()),
                                              int(self.entry_y2.get()), centralizacao, img))
        self.watch_screen = 1
        self.create_view() #cria o desenho do plano cartesiano chamando a funcao
        canvas.bind("<Motion>", self.cartesianPlane.mouse_position)
        canvas.bind("<Button-1>", self.draw_reta_mouse)

    def create_view_mid_point(self):  # Tela  2
        btn = Button(window, text='Draw', bd='5',
                     command=lambda: reta_mid_point(int(self.entry_x1.get()), int(self.entry_y1.get()),
                                                    int(self.entry_x2.get()),
                                                    int(self.entry_y2.get()), centralizacao, img))
        self.watch_screen = 2
        self.create_view()
        canvas.bind("<Motion>", self.cartesianPlane.mouse_position)
        canvas.bind("<Button-1>", self.draw_reta_mid_point_mouse)


class DrawPixel():
    def __init__(self):
        self.label_x1 = None
        self.labe1_y1 = None
        self.entry_x1 = None
        self.entry_y1 = None
        self.btn_clear = None
        self.btn = None
        self.label_x_y = None
        self.cartesianPlane = CartesianPlane()
        
    def create_view(self):
        global canvas, img
        
        window.geometry('1200x1000')

        list = window.grid_slaves()
        for i in list:
            i.destroy()

        self.label_x1 = Label(window, text="X1: ", font='Times 14')
        self.label_x1.grid(row=0, column=0)
        self.label_y1 = Label(window, text="Y1: ", font='Times 14')
        self.label_y1.grid(row=1, column=0)

        self.label_x_y = Label(window, text="X: 0 Y: 0", font='Times 14')
        self.cartesianPlane.label_change = self.label_x_y
        self.label_x_y.grid(row=3, column=5)
        
        self.entry_x1 = Entry(window, width=10)
        self.entry_x1.grid(row=0, column=1)

        self.entry_y1 = Entry(window, width=10)
        self.entry_y1.grid(row=1, column=1)

        self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: put_pixel(float(self.entry_x1.get()) + centralizacao, centralizacao - float(self.entry_y1.get()) , img)) 

        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn_clear = Button(window, text='Clear', bd='5',
                              command=self.clean)

        self.btn_clear.grid(row=2, column=2, padx=10, pady=10)


        
        canvas = Canvas(window, width=width, height=height, bg="#000000")
        canvas.grid(row=3, column=4)

        img = PhotoImage(width=width, height=height)
        canvas.create_image((width // 2, height // 2), image=img, state="normal")

        self.cartesianPlane.graph() # Desenha as linhas do plano cartesiano

        canvas.bind("<Button-1>", self.on_button_hold)
        canvas.bind("<B1-Motion>", self.on_button_hold)

    def on_button_hold(self, event):

        if((event.x >= 0 and event.x <= 600) and (event.y >= 0  and event.y <= 600)):
            put_pixel(event.x, event.y, img)
            self.label_x_y["text"] = "X: %d Y: %d" % (event.x - centralizacao, centralizacao - event.y)
            self.entry_x1.delete(0, "end")
            self.entry_y1.delete(0, "end")
            self.entry_x1.insert(0, event.x - centralizacao)
            self.entry_y1.insert(0, centralizacao - event.y)        

    def clean(self):
        self.__init__()
        self.create_view()
        
    
class DrawCircuferencia():

    def __init__(self):
        self.label_a = None
        self.label_b = None
        self.entry_a = None
        self.entry_b = None
        self.label_x1 = None
        self.label_y1 = None
        self.entry_x1 = None
        self.entry_y1 = None
        self.label_raio = None
        self.entry_raio = None
        self.btn = None
        self.btn_clear = None
        self.cartesianPlane = CartesianPlane()

    def create_view(self):
        global canvas, img
        
        window.geometry('1200x1000')

        list = window.grid_slaves()
        for i in list:
            i.destroy()

        self.label_x1 = Label(window, text="X1: ", font='Times 14')
        self.label_x1.grid(row=0, column=0)
        self.label_y1 = Label(window, text="Y1: ", font='Times 14')
        self.label_y1.grid(row=1, column=0)
        
        self.entry_x1 = Entry(window, width=10)
        self.entry_x1.grid(row=0, column=1)

        self.entry_y1 = Entry(window, width=10)
        self.entry_y1.grid(row=1, column=1)


        canvas = Canvas(window, width=width, height=height, bg="#000000")
        canvas.grid(row=3, column=4)

        img = PhotoImage(width=width, height=height)
        canvas.create_image((width // 2, height // 2), image=img, state="normal")

        self.cartesianPlane.graph() # Desenha as linhas do plano cartesiano


    def create_view_circu_ponto_medio(self):

        self.create_view()

        self.label_raio = Label(window, text="Raio: ", font='Times 14')
        self.label_raio.grid(row=0, column=2)
        self.entry_raio = Entry(window, width=10)
        self.entry_raio.grid(row=0, column=3)


        self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: circ_ponto_medio(float(self.entry_raio.get()), centralizacao, float(self.entry_x1.get()), float(self.entry_y1.get()), img)) 

        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn_clear = Button(window, text='Clear', bd='5',
                              command=lambda:self.clean(1)) 

        self.btn_clear.grid(row=2, column=2, padx=10, pady=10)
        


    def create_view_circu_trigonometrico(self):

        self.create_view()
        
        self.label_raio = Label(window, text="Raio: ", font='Times 14')
        self.label_raio.grid(row=0, column=2)
        self.entry_raio = Entry(window, width=10)
        self.entry_raio.grid(row=0, column=3)


        self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: circ_trigonometrico(float(self.entry_raio.get()), centralizacao, float(self.entry_x1.get()), float(self.entry_y1.get()), img)) 

        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn_clear = Button(window, text='Clear', bd='5',
                              command=lambda: self.clean(2)) 

        self.btn_clear.grid(row=2, column=2, padx=10, pady=10)
        
       
    def create_view_circu_explicita(self):
        
        self.create_view()
        
        self.label_raio = Label(window, text="Raio: ", font='Times 14')
        self.label_raio.grid(row=0, column=2)
        self.entry_raio = Entry(window, width=10)
        self.entry_raio.grid(row=0, column=3)


        self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: circ_equacao_explicita(float(self.entry_raio.get()), centralizacao, float(self.entry_x1.get()), float(self.entry_y1.get()), img)) 

        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn_clear = Button(window, text='Clear', bd='5',
                              command=lambda: self.clean(3)) 

        self.btn_clear.grid(row=2, column=2, padx=10, pady=10)
        


    def create_view_elipse(self):

        self.create_view()

        self.label_a = Label(window, text="A: ", font='Times 14')
        self.label_a.grid(row=0, column=2)
        self.label_b = Label(window, text="B: ", font='Times 14')
        self.label_b.grid(row=1, column=2)

        self.entry_a = Entry(window, width=10)
        self.entry_a.grid(row=0, column=3)
        self.entry_b = Entry(window, width=10)
        self.entry_b.grid(row=1, column=3)


        self.btn = Button(window, text='Draw', bd='5',
                              command=lambda: elipse_ponto_medio(float(self.entry_a.get()), float(self.entry_b.get()), centralizacao, float(self.entry_x1.get()), float(self.entry_y1.get()), img)) 

        self.btn.grid(row=2, column=1, padx=10, pady=10)

        self.btn_clear = Button(window, text='Clear', bd='5',
                              command=lambda: self.clean(4)) 

        self.btn_clear.grid(row=2, column=2, padx=10, pady=10)
                
        
    
    def clean(self, x):
        img.blank()

        if(x == 1):
            self.create_view_circu_ponto_medio()
        elif(x == 2):
            self.create_view_circu_trigonometrico()
        elif(x == 3):
            self.create_view_circu_explicita()
        elif(x == 4):
            self.create_view_elipse()
        
        #self.cartesianPlane.graph()
            
    def reset(self):
        self.__init__()


class DrawTransformations:
    def __init__(self):
        self.Xm = None
        self.x = None
        self.XM = None
        self.Ym = None
        self.y = None
        self.YM = None
        self.label_Xm = None
        self.label_x = None
        self.label_XM = None
        self.label_Ym = None
        self.label_y = None
        self.label_YM = None
        self.entry_Ym = None
        self.entry_y = None
        self.entry_YM = None
        self.entry_Xm = None
        self.entry_x = None
        self.entry_XM = None
        self.btn_convert = None
        self.label_result_ndc = None
        self.label_result_dc = None
        self.label_width = None
        self.label_height = None
        self.entry_width = None
        self.entry_height = None

    def result(self):
        ndcx = normalizedconvertions.ndcx(float(self.entry_Xm.get()), float(self.entry_x.get()),
                                          float(self.entry_XM.get()))
        ndcy = normalizedconvertions.ndcx(float(self.entry_Ym.get()), float(self.entry_y.get()),
                                          float(self.entry_YM.get()))
        dc = normalizedconvertions.dcx(float(self.entry_width.get()), ndcx)
        dy = normalizedconvertions.dcy(float(self.entry_height.get()), ndcy)

        self.label_result_ndc["text"] = "NdcX: %4f NdcY: %4f" % (ndcx, ndcy)
        self.label_result_dc["text"] = "Dcx: %d Dcy: %d" % (dc, dy)

    def create_view(self):
        self.clean()
        window.geometry('400x400')
        self.label_Xm = Label(window, text="Xm: ", font='Times 14')
        self.label_Xm.grid(row=0, column=0)
        self.label_x = Label(window, text="x: ", font='Times 14')
        self.label_x.grid(row=1, column=0)
        self.label_XM = Label(window, text="XM: ", font='Times 14')
        self.label_XM.grid(row=2, column=0)

        self.entry_Xm = Entry(window, width=10)
        self.entry_Xm.grid(row=0, column=1)
        self.entry_x = Entry(window, width=10)
        self.entry_x.grid(row=1, column=1)
        self.entry_XM = Entry(window, width=10)
        self.entry_XM.grid(row=2, column=1)

        self.label_Ym = Label(window, text="Ym: ", font='Times 14')
        self.label_Ym.grid(row=0, column=2)
        self.label_y = Label(window, text="y: ", font='Times 14')
        self.label_y.grid(row=1, column=2)
        self.label_YM = Label(window, text="YM: ", font='Times 14')
        self.label_YM.grid(row=2, column=2)

        self.entry_Ym = Entry(window, width=10)
        self.entry_Ym.grid(row=0, column=3)
        self.entry_y = Entry(window, width=10)
        self.entry_y.grid(row=1, column=3)
        self.entry_YM = Entry(window, width=10)
        self.entry_YM.grid(row=2, column=3)

        self.label_result_ndc = Label(window, text="NdcX:  NdcY: ", font='Times 12')
        self.label_result_ndc.grid(row=5, column=2, pady=20)
        self.label_result_dc = Label(window, text="DcX:  DcY: ", font='Times 12')
        self.label_result_dc.grid(row=6, column=2, pady=20)

        self.label_width = Label(window, text="Width: ", font='Times 14')
        self.label_width.grid(row=3, column=0)
        self.entry_width = Entry(window, width=10)
        self.entry_width.grid(row=3, column=1)
        self.label_height = Label(window, text="Height: ", font='Times 14')
        self.label_height.grid(row=3, column=2)
        self.entry_height = Entry(window, width=10)
        self.entry_height.grid(row=3, column=3)

        self.btn_convert = Button(window, text='Converter', bd='5', command=self.result)
        self.btn_convert.grid(row=4, column=2)

    def clean(self):
        
        list = window.grid_slaves()
        for i in list:
            i.destroy();


view_panel_line = DrawReta()
view_panel_circu = DrawCircuferencia()
view_panel_draw_pixel = DrawPixel()
view_panel_transformation = DrawTransformations()

# Create superior menu
menu = Menu(window)
line_menu = Menu(menu)
line_menu.add_command(label="Reta DDA", command=view_panel_line.create_view_dda)
line_menu.add_command(label="Ponto Medio", command=view_panel_line.create_view_mid_point)

transform_menu = Menu(menu)
transform_menu.add_command(label="DcX and DcY", command=view_panel_transformation.create_view)

circu_menu = Menu(menu)
circu_menu.add_command(label="Ponto Medio", command = view_panel_circu.create_view_circu_ponto_medio)
circu_menu.add_command(label="Ponto Trigonometrico", command = view_panel_circu.create_view_circu_trigonometrico)
circu_menu.add_command(label="Equacao Explicita", command = view_panel_circu.create_view_circu_explicita)
circu_menu.add_command(label="Elipse Ponto Medio", command = view_panel_circu.create_view_elipse)


menu.add("command", label="Pixel", command=view_panel_draw_pixel.create_view)
menu.add_cascade(label="Transformação", menu=transform_menu)
menu.add_cascade(label="Retas", menu=line_menu)
menu.add_cascade(label="Circuferencias", menu=circu_menu)
# End superior menu

window.config(menu=menu)

# create_view_dda()
mainloop()
