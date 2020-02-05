class Nodo:

    def __init__(self, dato):
        self.next = None
        self.dato = dato

    def show(self):
        print(self.dato)

    def __str__(self):
        return str(self.dato)        


class Lista:

    def __init__(self):
        self.primero = None
        self.cantidad = 0

    def push(self, elemento, index=0):
        nuevo = Nodo(elemento)
        if index == 0 or index > self.cantidad:
            nuevo.next = self.primero
            self.primero = nuevo
        else:
            nodo = self.pop()
            list = Lista()
            index -= 1
            for x in range(index):
                list.push(nodo)
                nodo = self.pop()
            self.push(nuevo)
            while not list.isEmpty(): 
                self.push(nodo)   
                nodo = list.pop()
                
            self.push(nodo)    
        self.cantidad += 1
            
    def pop(self, index=0):
        if index <= 0 or index > self.cantidad:
            aux = self.primero
            if self.primero is not None:
                self.primero = self.primero.next
        else:
            list = Lista() 
            index += 1
            for x in range(index):
                aux = self.pop()
                list.push(aux)
            aux = list.pop()    
            while not list.isEmpty():
                nodo = list.pop()
                self.push(nodo) 
        self.cantidad -= 1
        f=None
        if aux is not None:
            if aux.dato is not None:
                f=aux
        else:
            f=None    
        return f

    def peek(self, index=0):
        if index == 0 or index > self.cantidad:
            aux = self.primero
        else:
            list = Lista()
            index += 1
            for x in range(index):
                aux = self.pop()
                list.push(aux)  
            while not list.isEmpty():
                nodo = list.pop()
                self.push(nodo) 
        return aux

    def isEmpty(self):
        return self.primero is None

    def isNotEmpty(self):
        return self.cantidad != 0

    def show(self):
        aux = self.primero
        while aux is not None:
            print(aux.dato)
            aux = aux.next
