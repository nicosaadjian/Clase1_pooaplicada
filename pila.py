#Clase de TAD Pila
#Las funciones definidas en la clase Pila son las basicas del TAD Pila

class Pila: 
    def __init__(self):
        self.pila = []
    
    def agregarUnidad(self, unidad):
        self.pila.append(unidad)
        print(self.pila)
        
    def totalDeUnidades(self):
        contador = 0
        for unidad in self.pila:
            contador += 1
        return contador
    
    def quitarUnidad(self):
        tamanio = self.totalDeUnidades() #Tengo que llamar a self para invocar a la funcion
        if tamanio > 0:
            self.pila.pop()
            print(self.pila)
        else:
            print("Ya no hay mas unidades para quitar en la pila")
            
    def ver_tope(self):
        return self.pila[-1]
    
    def esta_vacia(self):
        print(len(self.pila) == 0)

pila = Pila()

pila.agregarUnidad("Libro1")
pila.agregarUnidad("Libro2")
pila.agregarUnidad("Libro3")
print(pila.totalDeUnidades())
pila.quitarUnidad()
pila.esta_vacia()
print(pila.ver_tope())


