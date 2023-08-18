import numpy as np

class pila:
    __tope=int
    __dim=int
    __arr=None
    def __init__(self, dim):
        self.__tope=-1
        self.__dim=dim
        self.__arr=np.empty(dim)

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
            print("La pila está vacia. No se puede suprimir.")
        else:
            objeto = self.__arr[self.__tope]
            self.__arr[self.__tope] = None
            self.__tope -= 1
            return objeto

    def mostrar(self):
        print("Contenido de la pila:")
        for i in range(self.__tope + 1):
            print(self.__arr[i])

    def multiplicar(self):
        total=1
        for i in range(self.__tope + 1):
            total*=self.__arr[i]
        return total


if __name__ == "__main__":
    numb=int(input("Ingresar numero: "))
    p = pila(numb)
    for i in range(numb):
        if i != 0:
            p.insertar(i)
    p.mostrar()
    fac=p.multiplicar()
    print(f"El factorial de {numb} es: {fac}")
