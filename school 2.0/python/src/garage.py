# coding=utf8
auto = "auto"
moto = "moto"


class Vehiculo:

    def __init__(self, patente, horaIngreso):
        self.setPatente(patente)
        self.setHoraIngreso(horaIngreso);
    
    def setPatente(self, patente): 
        self.validarPatente(patente)
        self._patente = patente 
    
    def validarPatente(self, patente):
        return
    
    def setHoraIngreso(self, horaIngreso):
        self.validarHora(horaIngreso) 
        self._horaIngreso = horaIngreso 
    
    def validarHora(self, horaIngreso):
        x = horaIngreso.hora
        y = horaIngreso.minuto
        if x < 0 or x >= 24:
            raise Exception("Hora de ingreso invalidos")
        if (y < 0) or (y >= 60):
            raise Exception("Minutos de ingreso invalidos")
    
    def calcularImporte(self, horaEgreso):
        return
    
    def calcularTiempoEstadia(self, horaSalida):
        x = horaSalida.toMinutes()
        y = self._horaIngreso.toMinutes()
        x -= y
        return horaSalida.toHours(x)
    
    def __str__(self):
        x = "Vehiculo [patente={}, horaIngreso={}]"
        return x.format(self._patente, self._horaIngreso.__str__())

    def round(self, minutos, base):
        return minutos + (base - minutos % base)

    def validarHoraEgreso(self, hora):
        x = self.calcularTiempoEstadia(hora).toMinutes()
        if x < 0:
            raise Exception("horario egreso anterior al de ingreso")
        return x


class Moto(Vehiculo):

    def __init__(self, patente, horaIngreso, precioPorHora):
        super(Moto, self).__init__(patente, horaIngreso)
        self.setPrecio(precioPorHora / 12)
    
    def setPrecio(self, precio):
        self.precioCincoMinutos = precio
        
    def validarPatente(self, patente):
        x = len(patente)
        y = "2ff444"
        if x is not 6 or patente is y:
            raise Exception("Patente erronea")
    
    def calcularImporte(self, horaEgreso):
        tiempo = self.validarHoraEgreso(horaEgreso)
        minutos = self.round(tiempo, 5)
        if minutos < 30:
            importe = 6 * self.precioCincoMinutos
        else:
            importe = (minutos / 5) * self.precioCincoMinutos
        
        return importe    


class Hora:

    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
    
    def __str__(self):
        x = "{}:{}"
        return x.format(self.hora, self.minuto)
    
    def toMinutes(self):
        return (self.hora * 60) + self.minuto
    
    def toHours(self, minutos):
        x = minutos
        return Hora(int(x / 60), x % 60)


class Auto(Vehiculo):

    def __init__(self, patente, horaIngreso, precioPorHora):
        super(Auto, self).__init__(patente, horaIngreso)
        self.setPrecio(precioPorHora / 6)
    
    def setPrecio(self, precio):
        self.precioDiezMinutos = precio
        
    def validarPatente(self, patente):
        x = len(patente)
        if x is not 6 or patente is "2ff444":
            raise Exception("Patente erronea")
    
    def calcularImporte(self, horaEgreso):
        tiempo = self.validarHoraEgreso(horaEgreso)
        minutos = self.round(tiempo, 10)
        if minutos < 30:
            importe = 6 * self.precioDiezMinutos
        else:
            importe = (minutos / 10) * self.precioDiezMinutos
        
        return importe   


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


class Estacionamiento:

    def __init__(self, capacidadAutos, capacidadMotos,
                  precioAutosPorHora, precioMotosPorHora):
        self.tadAutos = Pila(capacidadAutos)
        self.tadMotos = Pila(capacidadMotos)
        self.precioAutos(precioAutosPorHora)
        self.precioMotos(precioMotosPorHora)
        self.autosEstac = []
        self.motosEstac = []
        self.recaudAutos = 0
        self.recaudMotos = 0
    
    def precioAutos(self, porHora):
        if porHora <= 0:
            raise Exception("Precio de auto inv�lido")
        self.precioAutosPorHora = porHora
    
    def precioMotos(self, porHora):
        if porHora <= 0:
            raise Exception("Precio de auto inv�lido")
        self.precioMotosPorHora = porHora
    
    def estacionar(self, tipo, patente, hora):
        if tipo is "auto":
            self.estacionarAuto(patente, hora)
            print("Se estaciono correctamente el auto patente: ", patente)
        if tipo is "moto":
            self.estacionarMoto(patente, hora)
            print("Se estaciono correctamente la motocicleta patente: ", patente)
    
    def estacionarMoto(self, patente, hora):
        m = Moto(patente, hora, self.precioMotosPorHora)
        try:
            self.tadMotos.push(m)
        except:
            raise Exception("Estacionamiento de motos completo")
    
    def estacionarAuto(self, patente, hora):
        a = Auto(patente, hora, self.precioAutosPorHora)
        try:
            self.tadAutos.push(a)
        except:
            raise Exception("Pila llena")
    
    def retirar(self, tipo, patente, hora):
        importe = 0
        hora = Hora(hora.hora, hora.minuto)
        encontrado = None
        if tipo is "auto":
            encontrado = self.retirarlo(patente, self.tadAutos)
            if encontrado is None:
                raise Exception("Vehiculo con patente {} no encontrado".format(patente))
            importe = encontrado.calcularImporte(hora)
            self.autosEstac.append(Estacionado(encontrado._patente, importe))
            self.recaudAutos += importe
        if tipo is "moto":
            encontrado = self.retirarlo(patente, self.tadMotos)
            if encontrado is None:
                raise Exception("Vehiculo con patente {} no encontrado".format(patente))
            importe = encontrado.calcularImporte(hora)
            self.motosEstac.append(Estacionado(encontrado._patente, importe))
            self.recaudMotos += importe
        return importe
    
    def retirarlo(self, patente, tad):
        aux = Pila(-1)
        encontrado = None
        while not tad.isEmpty() and encontrado is None:
            v = tad.pop()
            if v._patente is patente:
                encontrado = v
            else:
                aux.push(v)
        while not aux.isEmpty():
            v = aux.pop()
            tad.push(v)
        if encontrado is None:
            raise Exception("Vehiculo con patente {} no encontrado".format(patente))
        return encontrado
    
    def finalizarDia(self):
        print("--------- Resumen final del dia --------------")
        print("Se han estacionado {} autos".format(len(self.autosEstac)))
        print("Se han estacionado {} motos".format(len(self.motosEstac)))
        print("----------------------------------------------")
        print("Por estacionamiento de autos se ha recaudado ${0:.2f}".format(self.recaudAutos))
        print("Por estacionamiento de motos se ha recaudado ${0:.2f}".format(self.recaudMotos))
        print("----------------------------------------------")
        print("Listado de autos estacionados")
        self.mostrar(self.autosEstac)
        print("----------------------------------------------")
        print("Listado de motos estacionadas")
        self.mostrar(self.motosEstac)
        print("----------------------------------------------")
        print("--------- Fin del reporte resumen final del dia --------------")
        
    def mostrar(self, listado):
        for x in listado:
            print("- Vehiculo patente: {}".format(x.patente),
                  "- Importe abonado: ${0:.2f}".format(x.importe))

    
class Estacionado:

    def __init__(self, patente, importe):
        self.patente = patente
        self.importe = importe


def main():
    e = Estacionamiento(6, 5, 60, 30)
    estacionarAutos(e)
    print("----------------------------------------------")
    estacionarMotos(e)
    print("----------------------------------------------")
    retirarAutos(e)
    print("----------------------------------------------")
    retirarMotos(e)
    print("----------------------------------------------")
    e.finalizarDia()      

    
def estacionarAutos(e):
    patentes = ["fff444", "fff424", "fef444", "ogy384", "2ff444",
                 "BGf444", "NNC894", "HRS875", "LTC824", "WRG833"]
    hora = [10, 0, 27, 12, 12, 20, 6, 7, 11, 14]    
    minuto = [0, 77, 0, 5, 5, 55, 25, 25, 25, 45]
    for x in range(10):
        try:
            e.estacionar("auto", patentes[x], Hora(hora[x], minuto[x]))
        except Exception as ex:
            print("No se pudo estacionar el vehículo - ", ex)

    
def estacionarMotos(e):
    patentes = ["324ADS", "654grt", "444fef",
                "432htf", "2ff444", "675BGf", "894NNC", "321HRS"]
    hora = [10, 0, 24, 15, 12, 9, 7, 14]
    minuto = [55, 87, 0, 25, 5, 15, 10, 15]
    for x in range(8):
        try:
            e.estacionar("moto", patentes[x], Hora(hora[x], minuto[x]))
        except Exception as ex:
            print("No se pudo estacionar el vehículo - ", ex)


def retirarAutos(e):
    patentes = ["BGf444", "BGf444", "LTC824", "NNC894", "HRS875"]
    hora = [23, 23, 2, 14, 18]
    minuto = [10, 25, 25, 13, 40]
    for x in range(5):
        try:
            h = Hora(hora[x], minuto[x])
            i = e.retirar("auto", patentes[x], h)
            s = "Se retiro correctamente el vehiculo patente {}, debe abonar "
            s = s.format(patentes[x])
            t = "${0:.2f}"
            t = t.format(i)
            s = s + t
            print(s)
        except Exception as no:
            print("No se pudo retirar el vehículo - ", no) 


def retirarMotos(e):
    patentes = ["432htf", "432htf", "675BGf", "321HRS"]
    hora = [18, 18, 20, 17]
    minuto = [10, 25, 5, 54]
    for x in range(4):
        try:
            h = Hora(hora[x], minuto[x])
            i = e.retirar("moto", patentes[x], h)
            s = "Se retiro correctamente el vehiculo patente {}, debe abonar "
            s = s.format(patentes[x])
            t = "${0:.2f}"
            t = t.format(i)
            s = s + t
            print(s)
        except Exception as no:
            print("No se pudo retirar el vehículo - ", no)


main()

