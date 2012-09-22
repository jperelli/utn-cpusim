#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

  Simulador de Algoritmos de planificación de la CPU

  Liberado bajo GNU GPL por:
    Ing. Julián Perelli
    Cátedra de Sistemas Operativos
    UTN - FRLP - 2012

 Posibles prerequisitos:
   apt-get install python

 Correr con:
   ./plan.py

"""

class Estado(object):

    #Variables de la clase
    none      = '0'
    inicio    = 'i'
    listo     = 'l'
    espera    = 'e'
    fin       = 'f'
    ejecucion = 'x'

    def __init__(self):
        self.valor = Estado.none

    def __str__(self):
        return self.valor

    def set(self, e):
        """
            TODO: chequear que se pueda pasar del estado "self.estado" a "e"
            sino, tirar excepcion
            TODO: chequear que "e" sea un "estado"
            TODO: ver como se crea un operador de comparacion para objetos __eq__?
        """
        paso = False
        if e != self.valor:
            paso = True
            self.valor = e
        return paso


class Sistema(object):

    def __init__(self, planificador):
        self.procs = []
        self.planificador = planificador
        self.vecINT = []

    def __str__(self):
        return "Sistema"

    def agregarProceso(self, proc):
        """
            Agrega un proceso al planificador
            TODO: chequear que "proc" sea de la clase "Proceso"
        """
        self.procs.append(proc)
        return proc

    def cpuVacia(self, procActual):
        """
            Devuelve True si ningun proceso estan en Estado.ejecucion
                     False si algun proceso esta en Estado.ejecucion
        """
        vacia = True
        for p in self.procs:
            if not vacia or p.estado.valor == Estado.ejecucion and p!=procActual:
                vacia = False
        return vacia

    def terminado(self):
        """
            Devuelve True si todos los procesos estan en Estado.fin
                     False si algun proceso no esta en Estado.fin
        """
        fin = True
        for p in self.procs:
            if not fin or p.estado.valor != Estado.fin:
                fin = False
        return fin

    def log(self, string):
        print string
        return string

    def correr(self):
        res = []
        t = 0
        self.log("---INICIO---")
        while not self.terminado():
            self.log(">>t=%s" % t)

            # borra las ints
            self.ints = []

            # inicio de procesos
            for p in self.procs:
                if p.inicio == t:
                    self.log("inicia: " + p.nombre)
                    self.planificador.iniciar(p)
                    self.ints.append("CP" + p.nombre)

            # inicio de ES
            for p in self.procs:
                if p.estado.valor != Estado.ejecucion and p.accion(p.avance) = 'ES':
                    self.ints.append("ES" + p.nombre)
                    self.planificador.inicioES(p)

            # terminacion de ES
            for p in self.procs:
                if p.estado.valor = Estado.espera and p.accion(p.avance) = 'CPU':
                    self.ints.append("AI" + p.nombre)
                    self.planificador.finES(p)

            # avance de los que estan en CPU o espera
            for p in self.procs:
                if (p.estado.valor = Estado.ejecucion and p.accion(p.avance) = 'CPU')
                    or (p.estado.valor = Estado.espera and p.accion(p.avance) = 'ES'):
                    self.ints.append("AI" + p.nombre)
                    self.planificador.salir

            if not acciones:

                if cpuVacia():
                    sig = self.planificador.siguiente()
                    self.planificador.asignarCPU(sig)
                else:
                    #avanzar a los procs que esten en CPU y ES y crear las INT correspondientes
                    pass

            t += 1
        return 'fin'


class PlanificadorFCFS:

    def __init__():
        self.listo = []

    def iniciar(self, proceso):
        proceso.estado.set(Estado.inicio)
        self.listo.append(proceso)
        proceso.estado.set(Estado.listo)

    def siguiente(self, eliminar=False):
        if self.listo:
            if eliminar:
                self.listo = self.listo[1:]
            return self.listo[0]
        else:
            return None

    def asignarCPU(self, proceso):
        self.listo.
        proceso.estado.set(Estado.ejecucion)
        return self.siguiente(True)

    def inicioES(self, proceso):
        self.listo.
        proceso.estado.set(Estado.espera)
        return True

    def finES(self, proceso):
        self.listo.
        proceso.estado.set(Estado.listo)


class Proceso():
    def __init__(self, nombre, inicio=0):
        self.inicio   = inicio
        self.acciones = []
        self.nombre   = nombre
        self.estado   = Estado()
        self.avance   = 0

    def __str__(self):
        return self.nombre

    def agregarAccion(self, accion, tiempo):
        if accion != 'CPU' and accion != 'ES':
            raise Exception('accion debe ser "CPU" o "ES"')
        assert isinstance(tiempo,(int,)), "tiempo debe ser un numero entero"
        for i in range(0, tiempo):
            self.acciones.append( accion )
        return self


if __name__ == '__main__':
    S = Sistema(PlanificadorFCFS())
    Pa = Proceso('A')
    Pa.agregarAccion('CPU', 2)
    Pa.agregarAccion('ES', 1)
    Pa.agregarAccion('CPU', 5)
    Pa.agregarAccion('ES', 2)
    Pa.agregarAccion('CPU', 3)
    Pa.agregarAccion('ES', 1)
    Pb = Proceso('B')
    Pb.agregarAccion('CPU', 2)
    Pb.agregarAccion('ES', 1)
    Pc = Proceso('C')
    Pc.agregarAccion('CPU', 2)
    Pc.agregarAccion('ES', 1)
    Pd = Proceso('D')
    Pd.agregarAccion('CPU', 2)
    Pd.agregarAccion('ES', 1)
    S.agregarProceso(Pa)
    S.agregarProceso(Pb)
    S.agregarProceso(Pc)
    S.agregarProceso(Pd)
    S.correr()
