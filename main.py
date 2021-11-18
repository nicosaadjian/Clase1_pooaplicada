class Fila:
    def __init__(self): 
        self.fila = []
        
    def agregarPersona(self, persona):
        self.fila.append(persona)
        print("Personas por atender: ", self.fila)
        
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

#Esta funcion servira para que el usuario pueda manipular la fila mediante una GUI

def funcionUsuario():
    fila = Fila()
    print("Bienvenido. Puede ingresar un numero y se agregara una persna o atenderá a la primer persona de la fila")
    print("1. Ingresar persona")
    print("2. Atender persona")
    print("3. Cerrar")
    opcion = int(input("Ingrese una opcion de la lista"))
    if(opcion == 1):
        nombrePersona = input("Ingrese el nombre del cliente")
        fila.agregarPersona(nombrePersona)
    elif(opcion == 2):
        fila.personaAtendida()
    elif(opcion == 3):
        print("Gracias por usar el sistema!")
        
funcionUsuario()
    
