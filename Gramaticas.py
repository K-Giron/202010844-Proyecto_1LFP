import os

class Gramatica:
    def __init__(self, nombre, no_terminales, terminales, no_terminal_inicial, producciones):
        self.nombre = nombre
        self.no_terminales = no_terminales
        self.terminales = terminales
        self.no_terminal_inicial = no_terminal_inicial
        self.producciones = producciones

    def generarReporte(self):
        dot = f'digraph {self.nombre} {"{"} \n'
        # add padding to graph
        dot += f'layout=dot; rankdir=LR; shape=circle \n'
        dot += f'{self.no_terminal_inicial} [shape = doublecircle]; \n'
        for estado in self.no_terminales:
            dot += f'{estado} [shape = circle]; \n' 

        dot += f'Inicio [shape = plaintext]; \n'
        dot += f'Inicio -> {self.no_terminal_inicial}; \n'

        for produccion in self.producciones:
            dot += f'{produccion.origen} -> {produccion.destino} [label = "{produccion.entrada}"]; \n'

        dot += f'"Nombre: {self.nombre} \n'
        dot += f'No terminales: '
        # recorrer estados
        for estado in self.no_terminales:
            dot += f'{estado},'

        dot += f'\n Terminales: '
        # recorrer alphabet
        for letra in self.terminales:
            dot += f'{letra},'

        dot += f'\n No terminal inicial: {self.no_terminal_inicial} \n'

        dot += f'Producciones: \n'
        for produccion in self.producciones:
            dot += f'{produccion.origen} -> {produccion.entrada} {produccion.destino} \n'
        dot += f'" [shape=box] {"}"}'

        document = open(f'archivos/{self.nombre}.dot', 'w')
        document.write(dot)
        document.close()

        os.system(
            f'dot.exe -Tpng archivos/{self.nombre}.dot -o archivos/{self.nombre}.png')

        return True

class Produccion:
    def __init__(self, origen, entrada, destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino

    def __str__(self):
        return f"({self.origen}, {self.entrada}; {self.destino})"
