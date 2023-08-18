import numpy as np

class pila:
    def __init__(self, dim):
        self.__tope = -1
        self.__dim = dim
        self.__arr = np.empty(dim)

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

def torres_de_hanoi(n):
    pila1 = pila(n)
    pila2 = pila(n)
    pila3 = pila(n)
    
    # Llenar la pila1 con discos de mayor a menor
    for i in range(n, 0, -1):
        pila1.insertar(i)
    
    movimientos_realizados = 0
    movimientos_minimos = 2**n - 1
    
    print("Estado inicial:")
    print("Pila 1:", pila1.__arr)
    print("Pila 2:", pila2.__arr)
    print("Pila 3:", pila3.__arr)
    
    while not pila1.vacio() or not pila2.vacio():
        print("\nMovimiento", movimientos_realizados + 1)
        print("Pila 1:", pila1.__arr)
        print("Pila 2:", pila2.__arr)
        print("Pila 3:", pila3.__arr)
        
        origen = int(input("Ingrese la pila de origen (1, 2, 3): "))
        destino = int(input("Ingrese la pila de destino (1, 2, 3): "))
        
        if origen == destino:
            print("Movimiento inválido. La pila de origen y destino son iguales.")
            continue
        
        if origen < 1 or origen > 3 or destino < 1 or destino > 3:
            print("Pila inválida. Debe ser 1, 2 o 3.")
            continue
        
        if origen == 1:
            disco = pila1.suprimir()
        elif origen == 2:
            disco = pila2.suprimir()
        else:
            disco = pila3.suprimir()
        
        if destino == 1:
            if pila1.vacio() or pila1.__arr[pila1.__tope] > disco:
                pila1.insertar(disco)
                movimientos_realizados += 1
            else:
                print("Movimiento inválido. No se puede colocar un disco sobre uno más pequeño.")
                if origen == 1:
                    pila1.insertar(disco)
                elif origen == 2:
                    pila2.insertar(disco)
                else:
                    pila3.insertar(disco)
        elif destino == 2:
            if pila2.vacio() or pila2.__arr[pila2.__tope] > disco:
                pila2.insertar(disco)
                movimientos_realizados += 1
            else:
                print("Movimiento inválido. No se puede colocar un disco sobre uno más pequeño.")
                if origen == 1:
                    pila1.insertar(disco)
                elif origen == 2:
                    pila2.insertar(disco)
                else:
                    pila3.insertar(disco)
        else:
            if pila3.vacio() or pila3.__arr[pila3.__tope] > disco:
                pila3.insertar(disco)
                movimientos_realizados += 1
            else:
                print("Movimiento inválido. No se puede colocar un disco sobre uno más pequeño.")
                if origen == 1:
                    pila1.insertar(disco)
                elif origen == 2:
                    pila2.insertar(disco)
                else:
                    pila3.insertar(disco)
    
    print("\n¡Felicitaciones! Has completado el juego.")
    print("Número de movimientos realizados:", movimientos_realizados)
    print("Número mínimo de movimientos requeridos:", movimientos_minimos)

# Pedir al usuario el número de discos
num_discos = int(input("Ingrese el número de discos: "))
torres_de_hanoi(num_discos)
