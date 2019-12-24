import time
from List import Lista

ingresada = 'i'
rechazada = 'r'
aceptada = 'a'


class Solicitud:

    def __init__(self, ids=0, alumno=None, carrera=0, materia="a", estado=None):
        self.num = ids
        self.alumno = alumno
        self.carrera = carrera
        self.materia = materia
        self.estado = estado      
    
    def __str__(self):
        return "{}".format(self.num)


class Curso:

    def __init__(self, idc=' ', carrera=0, materia='a', cupo=0):
        self.alumnos = []
        self.num = idc
        self.materia = materia
        self.cupo = cupo
        self.carrera = carrera
    
    def __str__(self):
        return "{}".format(self.num)
    
    def add(self, alumno):
        self.alumnos.append(alumno)

    def push(self, legajo=0, nombre=" ", promedio=0.1, porcentaje=100, tipo="c"):
        if tipo == "c":
            b = Alumno(legajo, nombre, promedio)
        else:
            b = Becado(legajo, nombre, promedio, porcentaje, tipo)
        self.add(b)


class Alumno:

    def __init__(self, legajo=0, nombre="", promedio=0.1):
        self.legajo = legajo
        self.nombre = nombre
        self.promedio = promedio


class Becado(Alumno):

    def __init__(self, legajo=0, nombre=" ", promedio=0.1, porcentaje=100, tipo="a"):
        Alumno.__init__(self, legajo, nombre, promedio)
        self.legajo = legajo
        self.nombre = nombre
        self.promedio = promedio
        self.tipo = tipo
        self.porcentaje = 100


class Materia:

    def __init__(self, idm="", nombre='', hsPorSemana=0):
        self.idm = idm
        self.nombre = nombre
        self.hsPorSemana = hsPorSemana

    def __str__(self):
        return self.nombre    


class Carrera:

    def __init__(self, idca=0, nombre=""):
        self.idca = idca
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Instituto:

    def __init__(self):
        self.solicitudes = Lista()
        self.cursos = Lista()
        self.materias = []
        self.carreras = []

    def push(self, elemento, lista="s"):
        if lista == "s":
            self.pushs(elemento)
        else:
            self.pushc(elemento)    

    def pushc(self, elemento, index=0):
        self.cursos.push(elemento, index) 

    def pushs(self, elemento, index=0):
        self.solicitudes.push(elemento, index) 

    def adds(self, ids=0, alumno=None, carrera=0, materia="a", estado=None):
        s = Solicitud(ids, alumno, carrera, materia, estado)
        self.pushs(s)

    def buscar(self, palabra, list="s"):
        if list == "s":
            lista = self.solicitudes
        else:
            lista = self.cursos    
        laux = Lista()
        encontrado = False
        existe = None
        while lista.isNotEmpty() and not encontrado:
            paux = lista.pop()
            if paux.num == palabra:
                existe = paux
                encontrado = True
            laux.push(paux)    
        if encontrado:
            print('elemento encontrado:', existe)
        else:
            print('elemento no encontrado')    
        while laux.isNotEmpty():    
            paux = laux.pop()
            lista.push(paux)
        return existe    

    def pop(self, lista="s", index=0):
        if lista == "s":
            f = self.solicitudes
        else:
            f = self.cursos    
        c = f.pop(index)
        if c == None:
            c = "Lista vacia"    
        return c

    def show(self, list):
        if list == "s":
            lista = self.solicitudes
        else:
            lista = self.cursos    
        laux = Lista()
        while lista.isNotEmpty():
            paux = lista.pop()
            print(paux)
            laux.push(paux)      
        while laux.isNotEmpty():    
            paux = laux.pop()
            lista.push(paux)
               

    def showm(self):
        for x in self.materias:
            print(x)

    def showc(self):
        for x in self.carreras:
            print(x)

    def pushm(self, m):
        self.materias.append(m)
        
    def addc(self, c):
        self.carreras.append(c)

        
def main():
    nom = ['analista de sistemas', 'biotecnologia', 'produccion musical', 'diseño grafico', 'desarrollo de videojuegos', 'derecho', 'contador público', 'medicina',
         'quimico farmaceutico', 'profesorado', 'ingenieria civil', 'enfermeria', 'ingeneria de alimentos', 'traductorado de ingles', 'administracion de empresas']
    
    niggas = Instituto()
    
    for x in range(len(nom)):
        niggas.addc(Carrera(x, nom[x]))

    for x in range(30):
        niggas.pushm(Materia("{}".format(x), "{}".format(x), x))
    
    c = Curso('12E', 0, 'p', 14)
    a = Alumno(2, "Andres", 7.5)
    b = Becado(1, 'Gabriel', 6.2, 99, "b")
    s = Solicitud(1, a, 0, "p", 'i')
    m = Materia("p", 'programacion', 4)
    
    c.add(a)
    c.add(b)
    
    niggas.pushs(s)
    niggas.pushc(c)
    
    niggas.materias.append(m)
    niggas.adds(2, b, niggas.carreras[0], niggas.materias[-1], ingresada)
    niggas.showc()
    print("-----------")
    niggas.showm()
    print("-----------")
    niggas.show("s")
    print("-----------")
    niggas.show("c")

print("-----------")
main()              
print("-----------")
