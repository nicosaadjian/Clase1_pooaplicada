class Fila:
    def __init__(self): 
        self.fila = []
        
    def agregarPersona(self, persona):
        self.fila.append(persona)
        print(self.fila)
        
    def personaAtendida(self):
        filaInvertida = self.fila[::-1]
        personasAtendidas = self.fila[0] 
        filaInvertida.pop()
        self.fila = filaInvertida[::-1]
        print("Que pase el/la siguiente")
        print(self.fila)
        print("Personas atendidas: ", personasAtendidas)
    
    
fila = Fila()
fila.agregarPersona("Luis")
fila.agregarPersona("Maria")
fila.agregarPersona("Pedro")
fila.agregarPersona("Carlos")
fila.personaAtendida()
fila.personaAtendida()
fila.personaAtendida()
