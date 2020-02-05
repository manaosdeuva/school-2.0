from List import Lista

ingresada='i'
rechazada='r'
aceptada='a'

class Solicitud:

    def __init__(self,ids=0,alumno=None,carrera=0,materia="a",estado=None):
        self.num=ids
        self.alumno=alumno
        self.carrera=carrera
        self.materia=materia
        self.estado=estado      
    
    def __str__(self):
        return "{} {} {}".format(self.num,self.alumno.nombre,self.estado)

class Curso:

    def __init__(self,id=' ',carrera=0,materia='a',cupo=0):
        self.alumnos=[]
        self.id = id
        self.materia=materia
        self.cupo=cupo
        self.carrera=carrera
    
    def __str__(self):
        return "{}".format(self.id)
    
    def add(self,alumno):
        self.alumnos.append(alumno)
        
    def push(self,legajo=0,nombre=" ",promedio=0.1,porcentaje=100,tipo="c"):
        if tipo == "c":
            b=Alumno(legajo,nombre,promedio)
        else:
            b=Becado(legajo,nombre,promedio,porcentaje,tipo)
        self.add(b)
        
    def aprobado(self):
        aprobado = False
        if len(self.alumnos) < self.cupo:
            aprobado = True
        return aprobado
    def alumnos(self):
        return self.alumnos

class Alumno:

    def __init__(self,legajo=0,nombre="",promedio=0.1):
        self.legajo=legajo
        self.nombre=nombre
        self.promedio=promedio

    def __str__(self):
        return nombre

class Regular(Alumno):
    def __init__(self,legajo,nombre,promedio):
        Alumno.__init__(self,legajo,nombre,promedio)
    def aprobado(self):
        aprobado = False
        if self.promedio>6:
            aprobado = True
        return aprobado

class Becado(Alumno):

    def __init__(self,legajo=0,nombre=" ",promedio=0.1,porcentaje=100,tipo="a"):
        Alumno.__init__(self, legajo, nombre, promedio)
        self.legajo=legajo
        self.nombre=nombre
        self.promedio=promedio
        self.tipo=tipo
        self.porcentaje=100
    def aprobado(self):
        aprobado = False
        if self.tipo == 'a':
            aprobado = True
        else:
            if self.porcentaje == 100:
                if self.promedio > 5:
                    aprobado = True
        return aprobado

class Materia:

    def __init__(self, idm="", nombre='', hsPorSemana=0):
        self.idm = idm
        self.nombre = nombre
        self.hsPorSemana = hsPorSemana

    def __str__(self):
        return self.idm        

class Carrera:
    def __init__(self, idca=0, nombre=""):
        self.idca = idca
        self.nombre = nombre

    def __str__(self):
        return '{} {}'.format(self.idca,self.nombre)

class ListaC(Lista):
    def __init__(self):
        Lista.__init__(self)

    def comparar(self,carrera,materia):
        printval = self.primero
        i=0
        while printval is not None and i == 0:
            if printval.dato.carrera is carrera:
                if printval.dato.materia is materia:
                    i=1
                else:
                    printval = printval.next
            else:
                printval = printval.next
        if printval is None:
            return None
        else:
            return printval.dato

    def eliminar(self,id):
        print(self.pop(0))
        return None

    def alu(self,alumno,index):
        curso=self.pop(index)
        curso.alumnos=alumno
        self.push(curso,index)
            
class ListaS(Lista):
    def __init__(self):
        Lista.__init__(self)

class Instituto:

    def __init__(self):
        self.solicitudes = ListaS()
        self.cursos = ListaC()
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
        
    def adds(self,ids=0,alumno=None,carrera=0,materia="a",estado=None):
        s=Solicitud(ids,alumno,carrera,materia,estado)
        self.pushs(s)

    def pop(self, lista="s", index=0):
        if lista == "s":
            f = self.solicitudes
        else:
            f = self.cursos    
        c = f.pop(index)
        if c is None:
            c = "Lista vacia"
        return c

    def crearSolicitud(self,alumno,carrera,materia):
        s = Solicitud(self.solicitudes.cantidad,alumno,carrera,materia,'i')
        c = self.checkSolicitud(s)
        if c is not None:
            if c.aprobado():
                s.estado = 'a'
            else:
                if s.alumno.aprobado():
                    s.estado = 'a'
                else:
                    s.estado = 'r'
        self.pushs(s)
        
    def checkSolicitud(self,solicitud):
        curso = self.cursos.comparar(solicitud.carrera,solicitud.materia)
        return curso
    
    def eliminarCurso(self,curso):
        eliminado = self.cursos.eliminar(curso)
        if eliminado is not None:
            a=eliminado.alumnos
            for x in a:
                self.crearSolicitud(x,eliminado.carrera,eliminado.materia)  
    def informarTot(self):
        materia = self.cargarMaterias()
        indice=0
        for m in self.materias:
            print('{}: {}'.format(m.nombre,materia[indice]))
            indice+=1
        carrera = self.cargarCarreras()
        indice = 0
        for c in self.carreras:
            print('{}: {}'.format(c.nombre,carrera[indice]))
            indice+=1

def alumnos():
    a=[Regular(0,'Gabriel Sanchez',6.9),Becado(1,'Gabriel Molina',6.2,99,"b"),Regular(2,"Andres",7.5)]
    return a
def materias():
    m = ('vdciza','nersdj','lyhifb','thgwwf','nhgqwg','jvopwh','edwbpy',
           'cktzjq','tdghft','vsayki','waoqcy','bzypwh','pwvomn','xghrjf',
           'oecskp','ejljnm','sactfq','wbrjlc','tbvvmk','wtcenn','hvtmaq',
           'emuoec','svildz','nipqus','nlknfo','mjzrll','adzemq','advtjh',
           'hfvvmv','ifliqf')
    horas = (87,77,64,104,117,143,20,69,161,96,121,110,21,148,126,
             59,103,5,93,73,153,135,155,140,28,138,55,76,116,3)
    materias = []
    for x in range(30):
        materias.append(Materia(m[x],"mat",horas[x]))
    return materias

def carreras():
    k = ['artes','bibliotecología','antropológicas','educación',
        'filosofía','geografía','historia','letras','prof. artes',
        'prof. bibliotecología','prof. antropológicas',
        'prof. educación','prof. filosofía','prof. geografía',
        'prof. historia','prof. letras']
    carreras=[]
    for x in range(15):
        carreras.append(Materia(x,k[x]))
    return carreras

def cursos(m):
    idc = ('eaha','ajsl','rxno','iwxs','jvtk','enxe','omht','ljbb',
           'mddz','iuel','lvuz','tlyo','cmpp','ekta','cjkx','aljv',
           'cijm','veco','nwbe','rrvi','keju','tzab','ylji','axps',
           'svuc','bdxj','reeu','ibnk','stkm','wwll')
    return (Curso(idc[0],0,m,69),
         Curso(idc[1],0,m,69),
         Curso(idc[2],0,m,69),
         Curso(idc[3],0,m,69),
         Curso('este',0,m,69))

def main():
    ort = Instituto()
    ort.materias = materias()
    ort.carreras = carreras()
    c = cursos(ort.materias[0])
    for x in c:
        ort.pushc(x)
    a = alumnos()
    ort.cursos.alu(a,0)
    ort.eliminarCurso('eaha')
    ort.solicitudes.show()
    ort.cursos.show()
    for x in ort.carreras:
        print(x.__str__())
    for x in ort.materias:
        print(x.__str__())
    #ort.informarTot()

print("-----------")
main()
print("-----------")
