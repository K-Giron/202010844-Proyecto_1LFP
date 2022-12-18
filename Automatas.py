import os

class Automata:
    def __init__(self, nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones # origen, valor y destino
    
    def generarReporte(self):
        print("Generando reporte...", self.nombre, self.estados, self.alfabeto, self.estado_inicial, self.estados_aceptacion, self.transiciones)
        dot = f'digraph {self.nombre} {"{"} \n'
        # add padding to graph
        dot += f'layout=dot; rankdir=LR; shape=circle \n'
        dot += f'{self.estado_inicial} [shape = doublecircle]; \n'
        for estado in self.estados:
            if estado in self.estados_aceptacion:
                dot += f'{estado} [shape = doublecircle]; \n'
            else:
                dot += f'{estado} [shape = circle]; \n'
        dot += f'Inicio [shape = plaintext]; \n'	
        dot += f'Inicio -> {self.estado_inicial}; \n'

        for transicion in self.transiciones:
            dot += f'{transicion.origen} -> {transicion.entrada} [label = "{transicion.destino}"]; \n'
        
        dot += f'"Nombre: {self.nombre} \n'
        dot += f'Estados: '
        # recorrer estados
        for estado in self.estados:
            dot += f'{estado},'

        dot += f'\n Alfabeto: '
        # recorrer alphabet
        for letra in self.alfabeto:
            dot += f'{letra},'

        dot += f'\n Estados de aceptacion: '
        # recorrer accepting_estados
        for estado in self.estados_aceptacion:
            dot += f'{estado},'

        dot += f'\n Estado inicial: {self.estado_inicial} \n'

        dot += f'Transiciones: \n'
        for transicion in self.transiciones:
            dot += f'{transicion.origen} -> {transicion.entrada};{transicion.destino} \n'
        dot += f'" [shape=box] {"}"}'

        document = open(f'archivos/{self.nombre}.dot', 'w')
        document.write(dot)
        document.close()

        os.system(f'dot.exe -Tpng archivos/{self.nombre}.dot -o archivos/{self.nombre}.png')

        return True
        

class Transicion:
    def __init__(self, origen, entrada, destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino
    
    def __str__(self):
        return f"({self.origen}, {self.entrada}; {self.destino})"

    