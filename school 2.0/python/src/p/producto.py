# coding=utf8


class Producto:

    def __init__(self, codigo, nombre, descripcion):
        self.setCodigo(codigo)
        self.setNombre(nombre)
        self.setDescripcion(descripcion)
    
    def setCodigo(self, codigo):
        if codigo is None:
            raise Exception("El codigo no puede ser nulo")
        self.codigo = codigo
        
    def setNombre(self, nombre):
        if nombre is None:
            raise Exception("El nombre no puede ser nulo")
        self.nombre = nombre
    
    def setDescripcion(self, descripcion):
        if descripcion is None:
            raise Exception("La descripcion no puede ser nula")
        self.descripcion = descripcion
        
    def setEtiqueta(self, etiqueta):
        self.etiqueta = etiqueta


class ProductoEstandar(Producto):

    def __init__(self, codigo, nombre, descripcion):
        super(ProductoEstandar, self).__init__(codigo, nombre, descripcion)
        self.setEtiqueta("Producto Estandar")
    
    def mostrar(self):
        print(self.__str__())
    
    def __str__(self):
        return " * {} [Codigo:{}, Nombre:{}, Descripcion:{}, Etiqueta:{}]".format(self.etiqueta, self.codigo, self.nombre, self.descripcion, self.etiqueta)


class ProductoFragil(Producto):

    def __init__(self, codigo, nombre, descripcion):
        super(ProductoFragil, self).__init__(codigo, nombre, descripcion)
        self.setEtiqueta("Producto Fragil")
    
    def mostrar(self):
        print(self.__str__())
    
    def __str__(self):
        return " * {} [Codigo:{}, Nombre:{}, Descripcion:{}, Etiqueta:{}]".format(self.etiqueta, self.codigo, self.nombre, self.descripcion, self.etiqueta)


class Pila:

    def __init__(self, limite):
        self.limite = limite
        self.elementos = []
        self.cantidad = 0
    
    def push(self, elemento):
        if self.isFull():
            raise Exception("Pila llena")
        self.elementos.append(elemento)
        self.cantidad += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Pila vacia")
        self.cantidad -= 1
        return self.elementos.pop()
    
    def isFull(self):
        return len(self.elementos) == self.limite
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Pila vacia")
        return self.elementos[len(self.elementos)]
    
    def isEmpty(self):
        return self.cantidad == 0
    
    def __str__(self):
        return self.elementos.__str__()

    
class Sistema:

    def __init__(self, maxEstandar, maxFragil):
        if maxEstandar < 0 or maxFragil < 0:
            raise Exception("tamanio deposito invalido")
        self.pilaEstandar = Pila(maxEstandar)
        self.pilaFragil = Pila(maxFragil)
        self.retirados = []
        self.fragiles = 0
        self.estandar = 0
    
    def addProduct(self, p):
        if p is None:
            raise Exception("el producto no puede ser nulo")
        if p.etiqueta is "Producto Estandar":
            if self.pilaEstandar.isFull():
                raise Exception("El deposito estandar esta lleno")
            self.pilaEstandar.push(p)
            self.estandar += 1
        if p.etiqueta is "Producto Fragil":
            if self.pilaFragil.isFull():
                raise Exception("El deposito fragil esta lleno")
            self.pilaFragil.push(p)
            self.fragiles += 1
    
    def retirar(self, codigo, tipo):
        encontrado = None
        if codigo is None:
            raise Exception("El codigo no puede ser nulo")
        if tipo is None:
            raise Exception("Tipo de Producto invalido")
        if tipo is "Fragil":
            if self.pilaFragil.isEmpty():
                raise Exception("No hay productos fragiles")
            encontrado = self.buscarProducto(codigo, self.pilaFragil)
            self.retirados.add(encontrado)
        if tipo is "Estandar":
            if self.pilaEstandar.isEmpty():
                raise Exception("No hay productos estandar")
            encontrado = self.buscarProducto(codigo, self.pilaEstandar)
            self.retirados.add(encontrado)
    
    def buscarProducto(self, codigo, tad):
        aux = Pila(-1)
        encontrado = None
        while not tad.isEmpty() and encontrado is None:
            p = tad.pop()
            if p.codigo is codigo:
                encontrado = p
            else:
                aux.push(p)
        while not aux.isEmpty():
            p = aux.pop()
            tad.push(p)
        if encontrado is None:
            raise Exception("Producto no encontrado")
        return encontrado
    
    def mostrar(self):
        print("Se han retirado ", len(self.retirados))
        for x in self.retirados:
            x.mostrar()
        print("Se ingresaron {} Productos Estandar y se ingresaron {} Productos Fragiles"
              .format(self.estandar, self.fragiles))


MSG_HUBO_UN_PROBLEMA_SACANDO_UN_PRODUCTO = "Hubo un problema sacando un producto: "
MSG_SE_RETIRO_CORRECTAMENTE_EL_PRODUCTO = "Se retiro correctamente el producto"
MSG_NO_SE_PUDO_AGREGAR_EL_PRODUCTO_ESTANDAR = "No se pudo agregar el producto Estandar: "
MSG_NO_SE_PUDO_AGREGAR_EL_PRODUCTO_FRAGIL = "No se pudo agregar el producto fragil: "
MSG_SE_INGRESO_CORRECTAMENTE_EL_PRODUCTO = "Se ingreso correctamente el producto"


def main():

    # print(MSG_HUBO_UN_PROBLEMA_SACANDO_UN_PRODUCTO)
    s = Sistema(4, 3)
    s = addEstandar(s)
    print("-------------------------------------------------------------")
    s = addFragil(s)
    print("-------------------------------------------------------------")
    s = retirar(s)
    print("-------------------------------------------------------------")
    s.mostrar()
    print(s.pilaEstandar.elementos)
    # ProductoEstandar("n", "i", "gga").mostrar()
    
    
def addEstandar(s):
    codigo = ["Estandar1", "Estandar2", None, "Un codigo loco", "Estandar5", "Estandar6", "Estandar99"] 
    nombre = ["Goma", "Silla", "Bolsa de Arena", None, "Barra de acero", "Caja carton", "Caja carton"] 
    descripcion = ["Goma de auto", "Silla ergon�mica", "Arenas del desierto", "Gran producto en oferta", "Ideal para edificios", "medida �nica", "medida �nica"]
    for x in range(7):
        try:
            s.addProduct(ProductoEstandar(codigo[x], nombre[x], descripcion[x]))
            print(MSG_SE_INGRESO_CORRECTAMENTE_EL_PRODUCTO)
        except Exception as e:
            print(e)
    return s


def addFragil(s):
    codigo = ["Fragil1", "Fragil2", None, "Un codigo", "Fragil5", "Fragil6"] 
    nombre = ["Ventana", "Florero", "Ventanas", None, "Jarron", "Espejo"] 
    descripcion = ["Ventana Fragil", "Florero hindu", "Ventanas Fragiles", "Ventanas Fragiles", "Dinastia Ming", "Espejo Magico"]
    s.addProduct(ProductoFragil(codigo[1], nombre[1], descripcion[1]))
    for x in range(6):
        try:
            s.addProduct(ProductoFragil(codigo[x], nombre[x], descripcion[x]))
            print(MSG_SE_INGRESO_CORRECTAMENTE_EL_PRODUCTO)
        except Exception as e:
            print(e)
    return s

    
def retirar(s):
    e = "Estandar"
    f = "Fragil"
    n = None
    codigo = ["Estandar2", None, "codigo", "Estandar6", "Fragil2", "Sin Codigo"]
    tipo = [e, e, n, e, f, f]
    for x in range(6):
        try:
            s.retirar(codigo[x], tipo[x])
            print(MSG_SE_RETIRO_CORRECTAMENTE_EL_PRODUCTO)
        except Exception as e:
            print(e)
    return s


main()
