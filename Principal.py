from tkinter import *
from tkinter import ttk
import tkinter as tk
from Modulos import *

''' PANTALLA PRINCIPAL DE LA APLCIACION'''


class PantallaPrincipal():
    def __init__(self):
        self.moduloMain = ModuloPrincipal()
        self.ventana = Tk()
        self.ventana.resizable(True, False)  # Redimensionar la ventana
        self.ventana.title('Pantalla Principal')  # Titulo de la ventana
        self.ventana.geometry('1100x700')  # Tamaño de la ventana
        self.Centrar(self.ventana, 1000, 700)  # Centrar la ventana
        self.ventana.config(bg='#172a39')
        self.Ventana()  # Llamar a la ventana
        self.a= ModuloPrincipal()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()  # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth()  # Ancho de la pantalla

        x = (ancho_pantalla // 2) - (ancho // 2)  # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2)  # Posicion de la ventana
        r.geometry(f'+{x}+{y}')  # Posicion de la ventana

    def Ventana(self):
        # Se coloca sobre la ventana
        self.frame = Frame(height=1000, width=800)
        self.frame.config(bg='#3d5568')
        self.frame.pack(padx=40, pady=40, fill=tk.X)

        Label(self.frame, text="Lenguajes Formales y de Programación ", font=(
            'Times New Roman', 40), fg='#ffffff', bg='#3d5568', width=40).place(x=-100, y=10)
        Label(self.frame, text="Sección: N", font=('Times New Roman', 20),
              fg='#ffffff', bg='#3d5568', width=40).place(x=-140, y=125)
        Label(self.frame, text="Carné: 202010844 ", font=('Times New Roman',
              20), fg='#ffffff', bg='#3d5568', width=40).place(x=-100, y=200)
        Label(self.frame, text="Kevin José de la Cruz Girón ", font=(
            'Times New Roman', 20), fg='#ffffff', bg='#3d5568', width=40).place(x=-50, y=275)

        # self.content = StringVar()
        # Entry(self.frame, textvariable=self.content,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=150)

        Button(self.frame, text="Módulo AFD", command=self.modAFD, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).place(x=200, y=350)

        Button(self.frame, text="Módulo GR", command=self.modGR, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).place(x=400, y=350)
        
        Button(self.frame, text="Cargar Archivos", command=self.modCarga, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=30).place(x=220, y=425)
        
        Button(self.frame, text="Salir", command=self.frame.quit, font=(
            'Times New Roman', 15), fg='#000000', bg='#a9c2d6', width=15).place(x=300, y=500)

        self.frame.mainloop()

    def modAFD(self):
        self.moduloMain.moduloAFD()
        
    def modGR(self):
        self.moduloMain.moduloGR()

    def modCarga(self):
        self.moduloMain.modCarga()


PantallaPrincipal()
