import numpy as np

class Pila:
    def __init__(self, dim):
        self.__tope = -1
        self.__dim = dim
        self.__arr = np.empty(dim, dtype=object)

    def lleno(self):
        return self.__tope == self.__dim - 1
    
    def vacio(self):
        return self.__tope == -1

    def insertar(self, objeto):
        if self.lleno():
            print("La pila está llena. No se puede realizar la inserción.")
        else:
            self.__tope += 1
            self.__arr[self.__tope] = objeto

    def suprimir(self):
        if self.vacio():
            print("La pila está vacía. No se puede suprimir.")
            return None
        else:
            objeto = self.__arr[self.__tope]
            self.__arr[self.__tope] = None
            self.__tope -= 1
            return objeto

    def mostrar(self):
        print("Contenido de la pila:")
        for i in range(self.__tope + 1):
            print(self.__arr[i])
            
    def __str__(self):
        return str(self.__arr[:self.__tope+1])

def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 desde torre {origen} a torre {destino}")
        destino.insertar(origen.suprimir())
    else:
        hanoi(n - 1, origen, destino, auxiliar)
        print(f"Mover disco {n} desde torre {origen} a torre {destino}")
        destino.insertar(origen.suprimir())
        hanoi(n - 1, auxiliar, origen, destino)

# Crear tres pilas para representar las torres
torre1 = Pila(5)
torre2 = Pila(5)
torre3 = Pila(5)

# Llenar la primera torre con discos
for i in range(5, 0, -1):
    torre1.insertar(i)

print("Estado inicial de las torres:")
print("Torre 1:", torre1)
print("Torre 2:", torre2)
print("Torre 3:", torre3)

# Resolver el juego de las Torres de Hanoi
hanoi(5, torre1, torre2, torre3)

print("\nEstado final de las torres:")
print("Torre 1:", torre1)
print("Torre 2:", torre2)
print("Torre 3:", torre3)
    
