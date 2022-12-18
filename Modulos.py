from Automatas import *
from Gramaticas import *
from tkinter import Tk
from tkinter import filedialog, ttk
import tkinter as tk
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image


class ModuloPrincipal():

    def __init__(self):
        self.ventanaMod = None
        self.ventanaModGR = None
        self.lista_automatas = []  # Vacia inicialmente
        self.lista_gramaticas = []
        self.no_terminals_accepted = []

    def moduloAFD(self):
        self.ventanaMod = tk.Toplevel(self.ventanaMod)
        self.ventanaMod.geometry("800x500")
        self.ventanaMod.resizable(False, False)
        self.ventanaMod.title("Ventana AFD")
        self.ventanaMod.config(bg="#172a39")

        titulo = ttk.Label(self.ventanaMod, text="Módulo AFD", font=(
            'Times New Roman', 40), foreground='#ffffff', background='#3d5568').grid(row=0, column=2, columnspan=3, pady=30)

        btnAgrega = tk.Button(
            self.ventanaMod, text="Crear AFD", font=(
                'Times New Roman', 15), foreground='#000000', command=self.crearAfd, background='#a9c2d6', width=15).grid(row=1, column=2, padx=100, pady=30)

        btnEvalua = tk.Button(
            self.ventanaMod, text="Evaluar Cadena", font=(
                'Times New Roman', 15), foreground='#000000', background='#a9c2d6', width=15).grid(row=1, column=4, pady=30)

        btnReporte = tk.Button(
            self.ventanaMod, text="Crear Reporte AFD", font=(
                'Times New Roman', 15), foreground='#000000', command=self.moduloReporteAFD, background='#a9c2d6', width=15).grid(row=2, column=2, pady=30)

        btnEvalua = tk.Button(
            self.ventanaMod, text="Ayuda", font=(
                'Times New Roman', 15), foreground='#000000', command=self.ayuda, background='#a9c2d6', width=15).grid(row=2, column=4, pady=30)

        btnRegresar = tk.Button(
            self.ventanaMod, text="Regresar", font=(
                'Times New Roman', 15), foreground='#000000', command=self.ventanaMod.destroy, background='#a9c2d6', width=15).grid(row=3, column=3, pady=30)

    def crearAfd(self):
        ventanaAdd = tk.Tk()
        ventanaAdd.geometry("500x600")
        ventanaAdd.resizable(False, False)
        ventanaAdd.title("Ventana Crear AFD")
        ventanaAdd.config(bg="#172a39")

        titulo = ttk.Label(ventanaAdd, text="Crear AFD", font=(
            'Times New Roman', 40), foreground='#ffffff', background='#3d5568').place(x=150, y=20)

        # etiquetas
        etiquetaNombre = tk.Label(
            ventanaAdd, text="Nombre", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=120)

        etiquetaEstados = tk.Label(
            ventanaAdd, text="Estados", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=180)

        etiquetaAlfabeto = tk.Label(
            ventanaAdd, text="Alfabeto", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=240)

        etiquetaEstadoI = tk.Label(
            ventanaAdd, text="Estado Inicial", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=300)

        etiquetaEstadosA = tk.Label(
            ventanaAdd, text="Estados Aceptación", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=360)

        etiquetaTransiciones = tk.Label(
            ventanaAdd, text="Transiciones", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=450)

        # Entrys

        entradaNombre = tk.Entry(ventanaAdd)
        entradaNombre.place(
            height=30, width=300, x=100, y=120)

        entradaEstados = tk.Entry(ventanaAdd)
        entradaEstados.place(
            height=30, width=300, x=100, y=180)

        entradaAlfabeto = tk.Entry(ventanaAdd)
        entradaAlfabeto.place(
            height=30, width=300, x=100, y=240)

        entradaEstadoI = tk.Entry(ventanaAdd)
        entradaEstadoI.place(
            height=30, width=250, x=150, y=300)

        entradaEstadosA = tk.Entry(ventanaAdd)
        entradaEstadosA.place(
            height=30, width=370, x=20, y=410)

        entradaTransiciones = tk.Entry(ventanaAdd)
        entradaTransiciones.place(
            height=30, width=370, x=20, y=500)

        btnAgrega = tk.Button(
            ventanaAdd, text="Crear", font=('Times New Roman', 15), foreground='#000000',
            command=lambda: guardarAutomata([entradaNombre.get(), entradaEstados.get(),
                                             entradaAlfabeto.get(), entradaEstadoI.get(), entradaEstadosA.get(), entradaTransiciones.get()]))
        btnAgrega.place(x=150, y=540)

        btnRegresa = tk.Button(
            ventanaAdd, text="Regresar", font=(
                'Times New Roman', 15), foreground='#000000',
            command=ventanaAdd.destroy, background='#a9c2d6')
        btnRegresa.place(x=250, y=540)

        def guardarAutomata(item):
            Guardar = True

            estados_ = str(item[1]).split(";")
            alfabeto_ = str(item[2]).split(",")
            estados_aceptados = str(item[4]).split(",")
            transiciones_ = str(item[5]).replace(" ", "").split(";")

            if (not item[3] in estados_ and not estados_aceptados in estados_):
                MessageBox.showwarning(
                    "Alerta", "El estado inicial o los estados aceptación no se encuentran en de los estados")
                Guardar = False

            for estado in estados_:
                if (estado in alfabeto_):
                    MessageBox.showwarning(
                        "Alerta", "El alfabeto no puede ser parte de los estados")
                    Guardar = False

            transiciones__ = []
            for t in transiciones_:
                t = t.split(",")
                if (not t[0] in estados_ or not t[2] in estados_):
                    MessageBox.showwarning(
                        "Alerta", "El origen o el destino de una transición no están en los estados.")
                    Guardar = False
                else:
                    transiciones__.append(Transicion(t[0], t[1], t[2]))

            if (Guardar):
                gramatica = Automata(item[0], estados_, alfabeto_,
                                     item[3], estados_aceptados, transiciones__)
                self.lista_automatas.append(gramatica)
                MessageBox.showinfo(
                    "Aviso!", "Se ha creado correctamente el autómata")
                ventanaAdd.destroy
                print(gramatica)
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error")

    def ayuda(self):


        # create ventana with Toplevel
        ventana = tk.Toplevel(self.ventanaMod)
        ventana.geometry("1000x600")
        ventana.resizable(False, False)
        ventana.title("Ventana AFD")
        ventana.config(bg="#172a39")

        # create frame in ventana
        frame = tk.Frame(ventana, bg="#172a39")
        frame.place(relwidth=1, relheight=1)

        self.image = Image.open("./archivos/imagen_ayuda.png")
        self.image = ImageTk.PhotoImage(self.image)
        
        self.label_image = tk.Label(
            frame, image=self.image)
        self.label_image.place(x=10, y=10)

    def ayudaGr(self):


        # create ventana with Toplevel
        ventana = tk.Toplevel(self.ventanaModGR)
        ventana.geometry("1000x600")
        ventana.resizable(False, False)
        ventana.title("Ventana AFD")
        ventana.config(bg="#172a39")

        # create frame in ventana
        frame = tk.Frame(ventana, bg="#172a39")
        frame.place(relwidth=1, relheight=1)

        self.image = Image.open("./archivos/imagen_ayuda.png")
        self.image = ImageTk.PhotoImage(self.image)
        
        self.label_image = tk.Label(
            frame, image=self.image)
        self.label_image.place(x=10, y=10)

    def moduloCadena(self):
        print("Hola")

    def moduloReporteAFD(self):
        ventana = Tk()
        ventana.geometry("800x500")
        ventana.resizable(False, False)
        ventana.title("Ventana AFD")
        ventana.config(bg="#172a39")

        titulo = ttk.Label(ventana, text="Módulo Reporte AFD", font=(
            'Times New Roman', 40), foreground='#ffffff', background='#3d5568')
        titulo.place(x=100, y=20)
        options_list = []

        # reccorer lista_automatas para obtener los nombres de los automatas y mostrarlos en el combobox
        for automata in self.lista_automatas:
            options_list.append(automata.nombre)

        # Create the list of options

        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tk.StringVar(ventana)

        # Set the default value of the variable
        value_inside.set("Select an Option")

        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        question_menu = tk.OptionMenu(ventana, value_inside, *options_list)
        question_menu.place(x=100, y=300)
        question_menu.pack()

        # button to get the option selected
        # from the optionmenu widget
        btnAgrega = tk.Button(
            ventana, text="Generar Reporte", font=('Times New Roman', 15), foreground='#000000',
            command=lambda: self.generarReporte(value_inside.get()))
        btnAgrega.place(x=100, y=400)

    def generarReporteGr(self, nombre):
        for gramatica in self.lista_gramaticas:
            if (gramatica.nombre == nombre):
                gramatica.generarReporte()

    def moduloGR(self):
        self.ventanaModGR = tk.Toplevel(self.ventanaModGR)
        self.ventanaModGR.geometry("800x500")
        self.ventanaModGR.resizable(False, False)
        self.ventanaModGR.title("Ventana GR")
        self.ventanaModGR.config(bg="#172a39")

        titulo = ttk.Label(self.ventanaModGR, text="Módulo GR", font=(
            'Times New Roman', 40), foreground='#ffffff', background='#3d5568').grid(row=0, column=2, columnspan=3, pady=30)

        btnAgrega = tk.Button(
            self.ventanaModGR, text="Crear GR", font=(
                'Times New Roman', 15), foreground='#000000', command=self.crearGR, background='#a9c2d6', width=15).grid(row=1, column=2, padx=100, pady=30)

        btnEvalua = tk.Button(
            self.ventanaModGR, text="Evaluar Cadena", font=(
                'Times New Roman', 15), foreground='#000000', background='#a9c2d6', width=15).grid(row=1, column=4, pady=30)

        btnReporte = tk.Button(
            self.ventanaModGR, text="Crear Reporte GR", font=(
                'Times New Roman', 15), foreground='#000000', command=self.moduloReporteGr, background='#a9c2d6', width=15).grid(row=2, column=2, pady=30)

        btnEvalua = tk.Button(
            self.ventanaModGR, text="Ayuda", font=(
                'Times New Roman', 15), foreground='#000000', command=self.ayudaGr, background='#a9c2d6', width=15).grid(row=2, column=4, pady=30)

        btnRegresar = tk.Button(
            self.ventanaModGR, text="Regresar", font=(
                'Times New Roman', 15), foreground='#000000', command=self.ventanaModGR.destroy, background='#a9c2d6', width=15).grid(row=3, column=3, pady=30)

    def crearGR(self):
        ventanaAdd = tk.Tk()
        ventanaAdd.geometry("500x550")
        ventanaAdd.resizable(False, False)
        ventanaAdd.title("Ventana Crear GR")
        ventanaAdd.config(bg="#172a39")

        titulo = ttk.Label(ventanaAdd, text="Crear GR", font=(
            'Times New Roman', 40), foreground='#ffffff', background='#3d5568').place(x=150, y=20)

        # etiquetas
        etiquetaNombre = tk.Label(
            ventanaAdd, text="Nombre", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=120)

        etiquetaNoTerminales = tk.Label(
            ventanaAdd, text="No Terminales", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=170)

        etiquetaTerminales = tk.Label(
            ventanaAdd, text="Terminales", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=250)

        etiquetaNoTerInicial = tk.Label(
            ventanaAdd, text="No Terminal Inicial", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=330)

        etiquetaProducciones = tk.Label(
            ventanaAdd, text="Transiciones", font=(
                "Agency FB", 18), bg="#3d5568", foreground="white").place(x=20, y=380)

        # Entrys

        entradaNombre = tk.Entry(ventanaAdd)
        entradaNombre.place(
            height=30, width=300, x=100, y=120)

        entradaNoTerminales = tk.Entry(ventanaAdd)
        entradaNoTerminales.place(
            height=30, width=380, x=20, y=210)

        entradaTerminales = tk.Entry(ventanaAdd)
        entradaTerminales.place(
            height=30, width=380, x=20, y=290)

        entrNoTerminalInicial = tk.Entry(ventanaAdd)
        entrNoTerminalInicial.place(
            height=30, width=230, x=170, y=330)

        entradaProducciones = tk.Entry(ventanaAdd)
        entradaProducciones.place(
            height=30, width=370, x=20, y=420)

        btnAgrega = tk.Button(
            ventanaAdd, text="Crear", font=('Times New Roman', 15), foreground='#000000',
            command=lambda: guardarGramatica([entradaNombre.get(), entradaNoTerminales.get(),
                                              entradaTerminales.get(), entrNoTerminalInicial.get(), entradaProducciones.get()]))
        btnAgrega.place(x=150, y=480)

        btnRegresa = tk.Button(
            ventanaAdd, text="Regresar", font=(
                'Times New Roman', 15), foreground='#000000',
            command=ventanaAdd.destroy, background='#a9c2d6')
        btnRegresa.place(x=250, y=480)

        def guardarGramatica(item):
            Guardar = True

            nombre_ = str(item[0])
            noTerminales_ = str(item[1]).replace(" ", "").split(";")
            terminales_ = str(item[2]).replace(" ", "").split(";")
            noTerminalInicial_ = str(item[3]).replace(" ", "")
            producciones_ = str(item[4]).replace(" ", "").split(";")

            for terminal in noTerminales_:
                for termina in terminales_:
                    if (termina == terminal):
                        MessageBox.showwarning(
                            "Alerta", "Los no terminales no pueden ser parte de terminales")
                        Guardar = False

            for gr in self.lista_gramaticas:
                if nombre_ == gr.nombre:
                    MessageBox.showwarning("Alerta", "El nombre ya existe")
                    Guardar = False

            if noTerminalInicial_ not in noTerminales_:
                MessageBox.showwarning(
                    "Alerta", "El no terminal inicial no existe en los no terminales.")

            producciones__ = []
            for t in producciones_:
                t = t.split(">")
                origen = str(t[0])
                s = t[1]
                valor = str(s[0])
                destino = str(s[1])
                if (not origen in noTerminales_ and origen not in terminales_):
                    MessageBox.showwarning(
                        "Alerta", "Los terminales o no terminales en las producciones no se encuentran definidos.")
                    Guardar = False
                if (destino not in terminales_ and destino not in noTerminales_):
                    MessageBox.showwarning(
                        "Alerta", "Los terminales o no terminales en las producciones no se encuentran definidos.")
                    Guardar = False
                producciones__.append(Produccion(origen, valor, destino))

            if (Guardar):
                gramatica = Gramatica(nombre_, noTerminales_, terminales_,
                                      noTerminalInicial_, producciones__)
                self.lista_gramaticas.append(gramatica)
                MessageBox.showinfo(
                    "Aviso!", "Se ha creado correctamente la gramática")
                ventanaAdd.destroy
                print(gramatica)
            else:
                MessageBox.showerror(
                    "Error", "Ha ocurrido un error al agregar la gramática")

    def moduloReporteGr(self):
        ventana = Tk()
        ventana.geometry("800x500")
        ventana.resizable(False, False)
        ventana.title("Ventana AFD")
        ventana.config(bg="#172a39")

        titulo = ttk.Label(ventana, text="Módulo Reporte Gr", font=(
            'Times New Roman', 40), foreground='#ffffff', background='#3d5568')
        titulo.place(x=100, y=20)
        options_list = []

        # reccorer lista_automatas para obtener los nombres de los automatas y mostrarlos en el combobox
        for gramatica in self.lista_gramaticas:
            options_list.append(gramatica.nombre)

        # Create the list of options

        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = tk.StringVar(ventana)

        # Set the default value of the variable
        value_inside.set("Select an Option")

        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.
        question_menu = tk.OptionMenu(ventana, value_inside, *options_list)
        question_menu.place(x=100, y=300)
        question_menu.pack()

        # button to get the option selected
        # from the optionmenu widget
        btnAgrega = tk.Button(
            ventana, text="Generar Reporte", font=('Times New Roman', 15), foreground='#000000',
            command=lambda: self.generarReporteGr(value_inside.get()))
        btnAgrega.place(x=100, y=200)

    def generarReporte(self, nombre):
        for automata in self.lista_automatas:
            if (automata.nombre == nombre):
                automata.generarReporte()

    def modCarga(self):
        ventanaCarga = tk.Tk()

        def almacenarAutomata(contenido):

            separacion = contenido.split("%")
            separacion = separacion[:-1]
            for lista in separacion:
                Guardar = True
                lista_ = str(lista).split("\n")
                if (lista_[0] == ""):
                    lista_ = lista_[1:]

                if (lista_[6] == ""):
                    lista_ = lista_[:-1]
                nombre_ = str(lista_[0])
                estados_ = str(lista_[1]).split(",")
                alfabeto_ = str(lista_[2]).split(",")
                estado_inicial_ = str(lista_[3])
                estados_aceptados = str(lista_[4]).replace(" ", "").split(",")
                transiciones_ = str(lista_[5]).replace(" ", "").split(";")
                if (transiciones_[0] == ""):
                    transiciones_ = transiciones_[1:]

                for t in transiciones_:
                    if (t == ""):
                        transiciones_ = transiciones_[:-1]

                if (not estado_inicial_ in estados_ and not estados_aceptados in estados_):
                    Guardar = False
                    continue

                for estado in estados_:
                    if (estado in alfabeto_):
                        Guardar = False
                        continue

                transiciones__ = []
                for t in transiciones_:

                    t = t.split(",")
                    if (not t[0] in estados_ or not t[2] in estados_):
                        Guardar = False
                        continue
                    else:
                        transiciones__.append(Transicion(t[0], t[1], t[2]))

                if (Guardar):
                    gramatica = Automata(nombre_, estados_, alfabeto_,
                                         estado_inicial_, estados_aceptados, transiciones__)
                    self.lista_automatas.append(gramatica)
                    MessageBox.showinfo(
                        "Aviso!", "Se ha cargado correctamente el archivo de autómatas")
                else:
                    MessageBox.showerror(
                        "Error", "Ha ocurrido errores al cargar el archivo")

            ventanaCarga.destroy

        def almacenarGramatica(contenido):
            separacion = contenido.split("%")

            for t in separacion:
                if (t == ""):
                    separacion = separacion[:-1]
            for lista in separacion:
                Guardar = True
                lista_ = str(lista).split("\n")
                if (lista_[0] == ""):
                    lista_ = lista_[1:]

                for t in lista_:
                    if (t == ""):
                        lista_ = lista_[:-1]

                nombre_ = str(lista_[0])
                noTerminales_ = str(lista_[1]).replace(" ", "").split(",")
                terminales_ = str(lista_[2]).replace(" ", "").split(",")
                noTerminal_inicial_ = str(lista_[3])
                prepare_productions = []
                producciones_ = []
                for li in range(4, len(lista_)):
                    prepare_productions.append(lista_[li])

                for terminal in noTerminales_:
                    for termina in terminales_:
                        if (termina == terminal):
                            MessageBox.showwarning(
                                "Alerta", "Los no terminales no pueden ser parte de terminales")
                            Guardar = False

                for gr in self.lista_gramaticas:
                    if nombre_ == gr.nombre:
                        MessageBox.showwarning("Alerta", "El nombre ya existe")
                        Guardar = False

                for t in prepare_productions:
                    t = t.split(">")
                    origen = str(t[0]).replace(" ", "")
                    l = str(t[1])
                    s = l.replace(" ", "")
                    valor = str(s[0])
                    if len(s) == 1:
                        if valor == '$':
                            self.no_terminals_accepted.append(origen)
                            continue
                    destino = str(s[1])

                    if (not origen in noTerminales_ and origen not in terminales_):
                        MessageBox.showwarning(
                            "Alerta", "Los terminales o no terminales en las producciones no se encuentran definidos.")
                        Guardar = False
                    if (destino not in terminales_ and destino not in noTerminales_):
                        MessageBox.showwarning(
                            "Alerta", "Los terminales o no terminales en las producciones no se encuentran definidos.")
                        Guardar = False
                    producciones_.append(Produccion(origen, valor, destino))

                if (Guardar):
                    gramatica = Gramatica(nombre_, noTerminales_, terminales_,
                                          noTerminal_inicial_, producciones_)
                    self.lista_gramaticas.append(gramatica)

                else:
                    MessageBox.showerror(
                        "Error", "Ha ocurrido errores al cargar el archivo")
            MessageBox.showinfo(
                "Aviso!", "Se ha leído correctamente el archivo de gramáticas")

        ventanaCarga.geometry("400x300")
        ventanaCarga.title("Ventana de Carga")
        ventanaCarga.config(bg="#15507e")
        ventanaCarga.resizable(False, False)

        def seleccionarArchivo():
            file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("Text files", "*.afd"), ("all files", "*.gre",)))
            if file is None:
                print("No has seleccioado ningun archivo.".center(50, "!"))
                return None
            else:
                extension = file[-3:]
                if extension == "afd":
                    with open(file, 'r', encoding='utf-8') as infile:
                        fila = infile.read()
                        almacenarAutomata(fila)
                elif extension == "gre":
                    with open(file, 'r', encoding='utf-8') as infile:
                        fila = infile.read()
                        almacenarGramatica(fila)

        etiquetaCarga = tk.Label(ventanaCarga, text="Seleccionar el archivo a leer", font=(
            "Agency FB", 18), bg="#15507e", foreground="white").place(x=100, y=40)

        botonElegir = ttk.Button(
            ventanaCarga, text="Carga de Archivos", command=seleccionarArchivo)
        botonElegir.place(x=120, y=150, width=190, height=60)
